from flask_jwt_extended import create_access_token
from flask import Blueprint, request, jsonify, make_response
from main.models.users import User, UserSchema
from main.utils.database import db
from flask_jwt_extended import jwt_required

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/users', methods=['POST'])
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

# login route


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data['username']

    password = data['password']

    user_to_login = User.query.filter_by(username=username).first()

    if user_to_login and user_to_login.check_password(password):
        token = create_access_token(identity=username)

        return make_response(
            jsonify({
                "message": "User Logged In successfully",
                "access_token": token,
                "success": True
            }), 200
        )

    else:
        return make_response(
            jsonify({
                "message": "Invalid Login",
                "success": False
            }), 400
        )


# change password
@auth_bp.route('/users/<int:id>', methods=['PATCH'])
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

# update a user account
# update a users' credentials


@auth_bp.route('/users/<int:id>', methods=['PUT'])
@jwt_required
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
