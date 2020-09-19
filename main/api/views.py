from flask import request, make_response, Blueprint, jsonify

from main.models.users import User, UserSchema
from main.utils.database import db

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/')
def hello():
    return jsonify({"message": "Hello"})


# Get all users
@api_bp.route('/users', methods=['GET'])
def get_all_users():
    get_users = User.query.all()

    user_schema = UserSchema(many=True)

    users = user_schema.dump(get_users)

    return make_response(jsonify(
        {"users": users,
         "success": True}))

# create a user account


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

    return make_response(
        jsonify({"message": "Resource added successfully",
                 "success": True}), 201)

# fetch a user by their id


@api_bp.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get_or_404(id)

    user_data = {"username": user.username,
                 "email": user.email,
                 "password": user.password}

    return make_response(
        jsonify({"user": user_data,
                 "success": True}), 200)

# delete a user account


@api_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user_account(id):
    user_to_delete = User.query.get_or_404(id)

    user_schema = UserSchema()

    print(user_to_delete)

    user_to_delete.delete_account()

    user = user_schema.dump(user_to_delete)

    return make_response(jsonify(
        {"user": user,
         "message": "User deleted successfully",
         "success": True}), 200)


# update a user account
@api_bp.route('/users/<int:id>', methods=['PUT'])
def update_user_info(id):
    user_to_update = User.query.get_or_404(id)
    user_schema = UserSchema(only=['id', 'username', 'email'])

    data = request.get_json()

    if data['username']:
        user_to_update.username = data['username']

    if data['email']:
        user_to_update.email = data['email']

    db.session.add(user_to_update)
    db.session.commit()

    user = user_schema.dump(user_to_update)

    return make_response(
        jsonify({
            "message": "Account Info update successfully",
            "user": user,
            "success": True
        }), 200
    )

# reset a password


@api_bp.route('/users/<int:id>', methods=['PATCH'])
def reset_password(id):
    data = request.get_json()

    user_to_update = User.query.get_or_404(id)

    if data['old_password']:
        old_password = data['old_password']

    if data['new_password']:
        new_password = data['new_password']

    if user_to_update.check_password(old_password) and new_password:
        user_to_update.password = new_password
        db.session.commit()
        return make_response(
            jsonify(
                {
                    "message": "Password Reset Successfull",
                    "success": True
                }
            )
        )

    else:
        return make_response(jsonify({"Please provide the last password you used."}))
