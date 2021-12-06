import functools
import json

from flask import (
    Blueprint, app, g, request, session, render_template
)
from rickandmorty.db import get_db

bp = Blueprint('list', __name__, url_prefix='/list')

@bp.route('/episodes', methods=['GET'])
def episodes():
    db = get_db()
    episodes = db.execute('SELECT * from episodes').fetchall()
    characters_name = db.execute('SELECT episode_id, name from joinEpisodesCharacters LEFT JOIN characters ON joinEpisodesCharacters.character_id = characters.id').fetchall()
    character_dict=dict()
    for appearing_name in characters_name:
        if appearing_name['episode_id'] not in character_dict:
            character_dict[appearing_name['episode_id']] = [appearing_name['name']]
        else:
            character_dict[appearing_name['episode_id']] += [appearing_name['name']]
    db.close()
    return render_template('list/episodes.html', episodes=episodes, character_dict=character_dict)

@bp.route('/characters', methods=['GET'])
def characters():
    db = get_db()
    characters = db.execute('SELECT * from characters').fetchall()
    episodes_name = db.execute('SELECT character_id, name from joinEpisodesCharacters LEFT JOIN episodes ON joinEpisodesCharacters.episode_id = episodes.id').fetchall()
    episode_dict=dict()
    for episode in episodes_name:
        if episode['character_id'] not in episode_dict:
            episode_dict[episode['character_id']] = [episode['name']]
        else:
            episode_dict[episode['character_id']] += [episode['name']]
    db.close()
    return render_template('list/characters.html', characters=characters, episode_dict=episode_dict)