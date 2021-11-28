import functools
import json

from flask import (
    Blueprint, g, request, session, jsonify
)
from rickandmorty.db import get_db

bp = Blueprint('list', __name__, url_prefix='/list')

@bp.route('/episodes', methods=['GET', 'POST'])
def episodes():
    episodes_json = json.loads(open('./data/episodes.json').read())
    return jsonify(episodes_json)

@bp.route('/characters', methods=['GET'])
def characters():
    characters_json = json.loads(open('./data/characters.json').read())
    return jsonify(characters_json)