from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/ping')
def ping():
    return jsonify({'answer': 'pong'}), 200
