import sqlite3
import os
import click
from flask import current_app, g
from flask.cli import with_appcontext
from . import images


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


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
    

@click.command('image-to-db')
@click.option('--path', '-p')
@with_appcontext
def image_to_db_command(path):
    tmp_img_path = path
    if not path:
        tmp_img_path = os.path.join(current_app.config['TMP_IMG'])
    images.copy_images(tmp_img_path)
    names = images.get_names(tmp_img_path)
    print(f'Making data from path {tmp_img_path}')
    with get_db() as db:
        for name, date in names:
            checked_name = db.execute('SELECT name FROM image WHERE name=?',
                              (name,)).fetchone()
            # не создаем запись в БД если такое имя файла существует
            if checked_name: 
                print(f'File {name} is exist')
                continue                  
            db.execute(
                'INSERT INTO  image (name, date) VALUES (?, ?)',
                (name, date)
            )
    


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(image_to_db_command)
