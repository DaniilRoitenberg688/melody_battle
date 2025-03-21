from flask import Blueprint, jsonify, request
from app.models import User
from app.errors import MissingData
from app.helpers import create_response
from app import db

bp = Blueprint('user', __name__)


@bp.route('', methods=['POST'])
@create_response
def create_user():
    data: dict = request.json
    login = data.get('login')
    email = data.get('email')
    password = data.get('password')
    user = User()

    if not login or not email or not password:
        raise MissingData('not enough data in register data')

    user.login = login
    user.email = email
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201
