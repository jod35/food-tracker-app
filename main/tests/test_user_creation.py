from main.models.users import User
from main.config import TestConfig
from main.utils.database import db
from main import app


def test_user_creation():
    app.config.from_object(TestConfig)

    db.init_app(app)

    with app.app_context():
        db.create_all()

        username = 'testuser'
        email = 'testuser@gmail.com'
        password = 'test1234'

        new_user = User(username=username, email=email)

        new_user.set_password(password)

        new_user.save()

        user = User.query.filter_by(username=username).first()

        assert user.username == username
