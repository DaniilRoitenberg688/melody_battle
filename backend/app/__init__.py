from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS
from yandex_music import Client

db = SQLAlchemy()
migtations = Migrate(render_as_batch=True)
client = Client('y0__xCzoIXBBRje-AYgiaff0xJwhAZ4ws8q4msdbAt1YNOCH_CsrA').init()


def init_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(Config)
    db.init_app(app)
    migtations.init_app(app, db)

    from .routes.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/api')

    from .routes.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/api/user')

    from .routes.melody_battles import bp as melody_bp
    app.register_blueprint(melody_bp, url_prefix='/api/melody_battle')

    return app

from app.models import *
