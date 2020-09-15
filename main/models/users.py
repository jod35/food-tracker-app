from main import db
from werkzeug.security import generate_password_hash,check_password_hash

from marshmallow_sqlalchemy import ModelSchema

from marshmallow import fields


class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(255),nullable=True)
    email=db.Column(db.String(255),nullable=False)
    password=db.Column(db.Text())

    def __repr__(self):
        return "{username}'s account"

    def set_password(self,password):
        self.password=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)


    def delete_account(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

 


