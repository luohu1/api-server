from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/users', methods=["GET"])
def get_user_lists():
    return "user lists"


@app.route('/users', methods=["POST"])
def create_user():
    return "create user"


@app.route('/users/<user_id>', methods=["GET"])
def get_user(user_id):
    return "user_id: " + user_id


if __name__ == '__main__':
    app.run(debug=True)
