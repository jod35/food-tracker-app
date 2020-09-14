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

@api_bp.route('/users',methods=['POST'])
def create_user():
    username=request.form.get('username')
    email=request.form.get('email')
    password=request.form.get('password')

    new_user=User(username=username,email=email)

    new_user.set_password(password)

    new_user.save()

    user_schema=UserSchema()

    user=UserSchema.dump(new_user)

    return make_response(
            jsonify({"message":"Resource added successfully",
                "user":user}


