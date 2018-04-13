from flask import Flask

from app.index import index as index_blueprint
from app.user import user as user_blueprint

app = Flask(__name__)

app.register_blueprint(index_blueprint, url_prefix='/')
app.register_blueprint(user_blueprint, url_prefix='/users')
