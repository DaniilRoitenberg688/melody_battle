from flask import Blueprint, jsonify, send_file

bp = Blueprint('main', __name__)

@bp.route('/ping')
def ping():
    return jsonify({'answer': 'pong'}), 200


@bp.route('/get_image/melody_battles_images/<path>')
def get_image(path):
    return send_file(f'static/melody_battles_images/{path}')