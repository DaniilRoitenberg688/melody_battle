from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migtations = Migrate(render_as_batch=True)


def init_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migtations.init_app(app, db)

    from app.routes.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/api')

    from app.routes.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/api/user')

    return app

from app.models import *
