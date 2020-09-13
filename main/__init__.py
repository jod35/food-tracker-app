from flask import Flask
from main.utils.database import db
from main.api.views import api_bp
from main.config import Config

def create_app():

    app =Flask(__name__)


    app.register_blueprint(api_bp,url_prefix='/')



    db.init_app(app)

    return app
    
