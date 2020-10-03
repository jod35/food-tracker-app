from main.models.users import User
from main.utils.database import db
from main import app
from main.config import TestConfig

app.config.from_object(TestConfig)
db.init_app(app)


with app.app_context():
    db.create_all()

    new_user = User(username='testuser', email='testuser@test.com')

    new_user.set_password('testpassword')

    new_user.save()


def test_password_reset():

    old_password = 'testpassword'

    new_password = 'newpassword'

    new_user.reset_password(old_password, new_password)

    assert new_user.check_password('newpassword') == True
