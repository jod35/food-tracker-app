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


