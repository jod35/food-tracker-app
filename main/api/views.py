from flask import request,make_response,Blueprint,jsonify

from main.models.users import User

api_bp=Blueprint('api_bp',__name__)

@api_bp.route('/')
def hello():
    return jsonify({"message":"Hello"})



@api_bp.route('/users',methods=['GET'])
def get_all_users():
    users=User.query.all()
    users_data=[]
    

    for user in users:
        user_data={}
        user_data['username']=user.username
        user_data['email']=user.email

        user_data['password']=user.password       
        users_data.append(user_data)

    return make_response(jsonify(
        {"users": users_data

            ,
         "success":True}))

@api_bp.route('/users',methods=['POST'])
def create_user():
    username=request.form.get('username')
    email=request.form.get('email')
    password=request.form.get('password')

    new_user=User(username=username,email=email)

    new_user.set_password(password)

    new_user.save()
    
    user={"username":new_user.username,
          "email":new_user.email,
          "password":new_user.password}

    return make_response(
            jsonify({"message":"Resource added successfully",
                "user":user}))

@api_bp.route('/users/<int:id>',methods=['GET'])
def get_user_by_id(id):
    user=User.query.get_or_404(id)

    user_data={"username":user.username,
               "email":user.email,
               "password":user.password}

    return make_response(
            jsonify({"user":user_data,
                "success":True}),200)

@api_bp.route('/users/<int:id>',methods=['DELETE'])
def delete_user_account(id):
    user_to_delete=User.query.get_or_404(id)

    user_to_delete.delete_account()

    return make_response(jsonify(
        {"user":{"username":user_to_delete.username,
        "email":user_to_delete.email,
        "password":user_to_delete.password},
        "message":"User deleted successfully",
        "success":True}),200)
