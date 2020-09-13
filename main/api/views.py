from flask import request,make_response,Blueprint,jsonify

from main.models.users import User

api_bp=Blueprint('api_bp',__name__)

@api_bp.route('/')
def hello():
    return jsonify({"message":"Hello"})

