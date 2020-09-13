import os

user =os.environ.get("MYSQL_USER")
password=os.environ.get("MYSQL_PASSWORD")



class Config:
    SECRET_KEY="JAN6AIBSBDYUDN"
    SQLALCHEMY_DATABASE_URI="mysql+pymysql:///{}:{}@localhost/food_db".format(user,password)
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False

