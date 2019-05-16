import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
	)

from NoteBook.db import get_db

bp = Blueprint('notes', __name__)

@bp.route('/<path_name>')
def save_path(path_name):
    db = get_db()
    if path_name is '':
	    return redirect(url_for('home'))
    elif path_name is 'myNotebook':
    	return redirect(url_for('example'))
    elif db.execute(
    		'SELECT * FROM note WHERE id = ?', (path_name,)
    	).fetchone() is None:
    	    db.execute(
    	        'INSERT INTO note (id, fileName) VALUES (?,?)', (path_name,path_name)
    	    	)
    	    db.commit()
    return render_template('notes.html', id=path_name)
