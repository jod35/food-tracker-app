from main.models.users import User
from main.config import TestConfig
from main.utils.database import db
from main import app


app.config.from_object(TestConfig)

db.init_app(app)


def test_user_creation():

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


def test_password_hashing():
    with app.app_context():
        db.create_all()

        new_user = User(username='test', email='test@test.com')

        password = 'password'

        new_user.set_password(password)

        new_user.save()

        assert new_user.check_password('password') == True
