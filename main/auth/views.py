from flask_jwt_extended import create_access_token
from flask import Blueprint, request, jsonify, make_response
from main.models.users import User


auth_bp = Blueprint('auth_bp', __name__)


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
