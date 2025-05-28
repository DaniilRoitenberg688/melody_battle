from flask import Blueprint, jsonify, request, current_app
from app.models import User
from errors import MissingData, ValidationError, NotUniqError
from werkzeug.exceptions import NotFound
from app.helpers import create_response, requires_user
from app import db
import jwt
import time

bp = Blueprint('user', __name__)


@bp.route('/register', methods=['POST'])
@create_response
def create_user():
    data: dict = request.json
    login = data.get('login')
    email = data.get('email')
    password = data.get('password')
    user = User()

    if not login or not email or not password:
        raise MissingData('not enough data in register data')

    if User.query.filter_by(email=email).all:
        raise NotUniqError('your email is not uniq')

    user.login = login
    user.email = email
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201

@bp.route('/login', methods=['POST'])
@create_response
def login_user():
    data: dict = request.json
    email = data.get('email')
    password = data.get('password')

    if not email and not password:
        raise MissingData('not enough data')

    user: User = User.query.filter_by(email=email).first()
    print(user)
    if not user:
        raise NotFound
    print('a')
    if not user.check_password(password):
        raise ValidationError('wrong password')

    token = jwt.encode({'user_id': user.id, 'created_at': int(time.time())}, current_app.config['SECRET_KEY'],
                       algorithm='HS256')

    return jsonify({'token': token})

@bp.route('', methods=['GET'])
@requires_user
@create_response
def get_user(user: User):
    return jsonify(user.to_dict())
