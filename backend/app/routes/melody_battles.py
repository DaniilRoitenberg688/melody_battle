from flask import Blueprint, jsonify, request, current_app
from app.models import User
from errors import MissingData, ValidationError
from werkzeug.exceptions import NotFound
from app.models import MelodyBattle
from app.helpers import create_response, requires_user
from app import db
import jwt
import time
from app.ym import create_melody_battle

bp = Blueprint('melody_battle', __name__)


@bp.route('', methods=['GET'])
@create_response
@requires_user
def get_melody_battles(user):
    melody_battles: list[MelodyBattle]= user.melody_battles
    return jsonify([i.to_dict() for i in melody_battles]), 200


@bp.route('', methods=['POST'])
@create_response
@requires_user
def create_melody_battle_route(user):
    data = request.json
    url = data.get('url')
    melody_battle: MelodyBattle = create_melody_battle(url)
    print(melody_battle)
    melody_battle.user = user
    db.session.commit()
    return jsonify(melody_battle.to_dict()), 201

