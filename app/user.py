from flask import Blueprint
from flask_restful import Api, Resource

user = Blueprint('user', __name__)
api = Api(user)


class Index(Resource):
    def get(self):
        return "Hello World!"


class UserApi(Resource):
    def get(self, user_id=None):
        if user_id:
            return "user_id: " + user_id
        else:
            return "user lists"

    def post(self):
        return "create user"


api.add_resource(UserApi, '/', '/<user_id>')
