import os

user =os.environ.get("MYSQL_USER") or 'jona'
password=os.environ.get("MYSQL_PASSWORD") or 'nathanoj35'



class Config:
    SECRET_KEY="JAN6AIBSBDYUDN"
    SQLALCHEMY_DATABASE_URI="sqlite:///site.db"
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class DevConfig(Config):
    DEBUG=True
