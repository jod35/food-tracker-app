from flask import request, make_response, Blueprint, jsonify

from main.models.users import User, UserSchema

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/')
def hello():
    return jsonify({"message": "Hello"})


@api_bp.route('/users', methods=['GET'])
def get_all_users():
    get_users = User.query.all()

    user_schema = UserSchema(many=True)

    users = user_schema.dump(get_users)

    return make_response(jsonify(
        {"users": users,
         "success": True}))


@api_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if data['username']:
        username = data['username']

    if data['email']:
        email = data['email']

    if data['password']:
        password = data['password']

    new_user = User(username=username,
                    email=email,
                    )

    new_user.set_password(password)

    user_schema = UserSchema()

    user = user_schema.dump(new_user.save())

    return make_response(
        jsonify({"message": "Resource added successfully",
                 "user": user}))


@api_bp.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get_or_404(id)

    user_data = {"username": user.username,
                 "email": user.email,
                 "password": user.password}

    return make_response(
        jsonify({"user": user_data,
                 "success": True}), 200)


@api_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user_account(id):
    user_to_delete = User.query.get_or_404(id)

    user_to_delete.delete_account()

    return make_response(jsonify(
        {"user": {"username": user_to_delete.username,
                  "email": user_to_delete.email,
                  "password": user_to_delete.password},
         "message": "User deleted successfully",
         "success": True}), 200)
