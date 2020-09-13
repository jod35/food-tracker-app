from flask import Flask
from main.utils.database import db
from main.api.views import api_bp
from main.config import Config


app =Flask(__name__)
app.config.from_object(Config)


app.register_blueprint(api_bp,url_prefix='/')



db.init_app(app)

@app.shell_context_processor
def make_shell_context():
    return {'app':app}
    
