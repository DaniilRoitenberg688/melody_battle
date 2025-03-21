from werkzeug.exceptions import BadRequest, NotFound
from app.errors import MissingData, InvalidData

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
        except InvalidData as e:
            return {'error': 'invalid data', 'reason': str(e)}, 400
        except Exception as e:
            return {'error': 'something went wrong on server', 'reason': str(e)}, 400


    wrapper.__name__ = func.__name__
    return wrapper
