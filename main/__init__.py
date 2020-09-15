from flask import Flask,jsonify
from main.utils.database import db
from main.api.views import api_bp
from main.config import Config
from main.models.users import User


app =Flask(__name__)
app.config.from_object(Config)


app.register_blueprint(api_bp,url_prefix='/')


db.init_app(app)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"message":"Not found"}
            )

@app.errorhandler(500)
def server_error(error):
    return jsonify({"message":"Server error, our team will try yo fix this"})

@app.shell_context_processor
def make_shell_context():
    return {'app':app,'db':db,'User':User}
    
