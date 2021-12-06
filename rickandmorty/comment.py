import functools
import json

from flask import (
    Blueprint, request, render_template, flash
)
from rickandmorty.db import get_db

bp = Blueprint('comment', __name__, url_prefix='/comment')

@bp.route('/comments', methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':
        comment = request.form['comment']
        episode = request.form['episode']
        character = request.form['character']
        db = get_db()
        error = None

        if not comment:
            error = 'Comment is required.'
        elif not episode and not character:
            error = 'Comment must at least concern an episode or a character.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO comments (comment, episode, character) VALUES (?, ?, ?)",
                    (comment, episode, character)
                )
                db.commit()
            except db.IntegrityError:
                error = f"Unexpected error."
        flash(error)

    return render_template('templates/comment.html')
