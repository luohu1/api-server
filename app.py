from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)


class UserApi(Resource):
    def get(self, user_id=None):
        if user_id:
            return "user_id: " + user_id
        else:
            return "user lists"

    def post(self):
        return "create user"


class Index(Resource):
    def get(self):
        return "Hello World!"


api.add_resource(Index, '/')
api.add_resource(UserApi, '/users/', '/users/<user_id>')

if __name__ == '__main__':
    app.run(debug=True)
