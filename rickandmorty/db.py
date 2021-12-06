import sqlite3
import json

import click
from flask import current_app, g, jsonify
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    
    cur = db.cursor()

    episodes_json = json.loads(open('./data/episodes.json').read())
    for row in episodes_json:
        cur.execute("INSERT INTO episodes (name, air_date, episode) VALUES (?, ?, ?)",
                    (row['name'], row['air_date'], row['episode'])
                    )

    characters_json = json.loads(open('./data/characters.json').read())
    for row in characters_json:
        cur.execute("INSERT INTO characters (name, status, species, type, gender) VALUES (?, ?, ?, ?, ?)",
                    (row['name'], row['status'], row['species'], row['type'] ,row['gender'])
                    )
        for episode_id in row['episode']:
            cur.execute("INSERT INTO joinEpisodesCharacters (character_id, episode_id) VALUES (?, ?)",
                    (row['id'], episode_id)
                    )
    db.commit()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)