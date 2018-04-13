from flask import Flask

from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from app.index import index as index_blueprint
    app.register_blueprint(index_blueprint, url_prefix='/')

    from app.user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/users')

    return app
