import time
from functools import wraps

import jwt
from werkzeug.exceptions import BadRequest, NotFound
from errors import MissingData, ValidationError, TokenError

from flask import request, current_app

from app.models import User

def create_response(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BadRequest as e:
            return {'error': 'bad request', 'reason': str(e)}, 400
        except NotFound as e:
            return {'error': 'not found', 'reason': str(e)}, 404
        except MissingData as e:
            return {'error': 'missing data', 'reason': str(e)}, 400
        except ValidationError as e:
            return {'error': 'invalid data', 'reason': str(e)}, 400

        except TokenError as e:
            return {'error': 'token error', 'reason': str(e)}, 401
        except Exception as e:
            return {'error': 'something went wrong on server', 'reason': str(e)}, 400


    wrapper.__name__ = func.__name__
    return wrapper

def requires_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # получаем токен из заголовков запроса
        token = request.headers.get('Authorization', '').replace('Bearer ', '')

        # если токена нет - возвращаем ошибку
        if not token:
            raise TokenError('Missing token')

        # расшифровываем токен и получаем его содержимое
        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        except Exception as e:
            raise TokenError('Invalid token')

        # получаем id пользователя и время генерации из токена
        user_id = payload.get('user_id')
        created_at = payload.get('created_at')

        # если чего-то нет - возвращаем ошибку
        if not user_id or not created_at:
            raise TokenError('Invalid token')

        # находим пользователя, если его нет - возвращаем ошибку
        user = User.query.filter_by(id=user_id).first()
        if not user:
            raise TokenError('user not found')

        # если с момента генерации прошло больше суток, просим войти заного
        if created_at + 60 * 60 * 24 < int(time.time()):
            raise TokenError('token expired')

        # передаем в целевой эндпоинт пользователя и параметры пути
        return func(user, *args, **kwargs)

    return wrapper
