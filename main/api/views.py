from flask import request,make_response,Blueprint,jsonify

from main.models.users import User,UserSchema

api_bp=Blueprint('api_bp',__name__)

@api_bp.route('/')
def hello():
    return jsonify({"message":"Hello"})



@api_bp.route('/users',methods=['GET'])
def get_all_users():
    users=User.query.all()

    user_schema=UserSchema()

    user=user_schema.dump(users)

    return make_response(jsonify(
        {"userss": users,
         "success":True}))


