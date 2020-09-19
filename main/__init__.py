from flask import Flask, jsonify
from main.utils.database import db
from main.api.views import api_bp
from main.auth.views import auth_bp
from main.config import Config
from main.models.users import User
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)


app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/auth')

db.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Not found"}
                   )


@app.errorhandler(500)
def server_error(error):
    return jsonify({"message": "Server error, our team will try yo fix this"})


@app.shell_context_processor
def make_shell_context():
    return {'app': app, 'db': db, 'User': User}
