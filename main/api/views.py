from flask import request, make_response, Blueprint, jsonify
from main.models.users import User, UserSchema
from flask_jwt_extended import jwt_required
from main.utils.database import db

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/')
def hello():
    return jsonify({"message": "Hello"})


# Get all users

@api_bp.route('/users', methods=['GET'])
@jwt_required
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

    new_user.set_password(password)

    user_schema = UserSchema()

    user = user_schema.dump(new_user)

    return make_response(
        jsonify({"message": "Resource added successfully",
                 "success": True}), 201)

# fetch a user by their id


@api_bp.route('/users/<int:id>', methods=['GET'])
@jwt_required
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
@jwt_required
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
