#!/usr/bin/env python3

import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['DEBUG'] = True
app.config['USE_RELOADER'] = True

# helper functions to get connection to database
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row    # ensures rows are returned as python dict
    return connection

# helper function to get a post from the posts table
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    connection.close()
    if post is None:
        abort(404)
    return post


# application routes
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM POSTS').fetchall()
    connection.close()
    return render_template('index.html', posts=posts) 

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                                (title, content))
            connection.commit()
            connection.close()
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:id>/edit/',methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required')
        
        elif not content:
            flash('Content is required')

        else:
            connection = get_db_connection()
            connection.execute('UPDATE posts SET title = ?, content = ?'
                               'WHERE id = ?',
                               (title, content, id))
            connection.commit()
            connection.close()
            return redirect(url_for('index'))
    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = get_post(id)
    connection = get_db_connection()
    connection.execute('DELETE FROM posts WHERE id = ?', (id,))
    connection.commit()
    connection.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))