from flask import Blueprint
from flask_restful import Api, Resource

from app import db

user = Blueprint('user', __name__)
api = Api(user)


class UserApi(Resource):
    def get(self, user_id=None):
        if user_id:
            return "user_id: " + user_id
        else:
            return "user lists"

    def post(self):
        return "create user"


api.add_resource(UserApi, '/', '/<user_id>')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Interval, primary_key=True)
    username = db.Column(db.String(64))
