#!/usr/bin/env python3

import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

random_id = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]


# helper functions to get connection to database
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row    # ensures rows are returned as python dict
    return connection

# helper function to get a post from the posts table
def get_shoe(shoe_id):
    connection = get_db_connection()
    shoe = connection.execute('SELECT * FROM products WHERE product_id = ?', (shoe_id,)).fetchone()
    connection.close()
    if shoe is None:
        abort(404)
    return shoe

# helper function to check if the file is valid
def allowed_file(filename):
    if '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
        return True
    return False

# application routes
@app.route('/')
def index():
    """
    View function that returns all the shoes in the products table
    """
    connection = get_db_connection()
    shoes = connection.execute('SELECT * FROM products').fetchall()
    connection.close()
    return render_template('index.html', shoes=shoes)


@app.route('/add/', methods=('GET', 'POST'))
def add():
    """
    View function that adds a new product to our product table
    """
    if request.method == "POST":
        id = random_id.pop()
        name = request.form['name']
        category = request.form['category']
        price = request.form['price']
        quantity = request.form['quantity']
        image_01 = request.files['image_01']
        image_02 = request.files['image_02']
        image_03 = request.files['image_03']
        image_04 = request.files['image_04']
        image_05 = request.files['image_05']
        description = request.form['description']

        if not name:
            flash('Shoe name is required!')
            return render_template('add.html')
        elif not category:
            flash('Shoe category is required')
        elif not price:
            flash('Price is required')
        elif not quantity:
            flash('Quantity is required')
        elif not image_01 or image_01.filename == '':
            flash('Image 01 is required')
        elif not image_02 or image_02.filename == '':
            flash('Image 02 is required')
        elif not image_03 or image_03.filename == '':
            flash('Image 03 is required')
        elif not image_04 or image_04.filename == '':
            flash('Image 04 is required')
        elif not image_05 or image_05.filename == '':
            flash('Image 05 is required')
        elif not description:
            flash('A brief descriptin of the shoe is required')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO products (\
                               product_id,\
                               product_name, product_category,\
                               product_price, product_quantity,\
                               product_image_01, product_image_02, product_image_03,\
                               product_image_04, product_image_05, product_description)\
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (id, name, category, price, quantity, image_01.read(),
                                 image_02.read(), image_03.read(), image_04.read(), image_05.read(), description))
            connection.commit()
            connection.close()
            return redirect(url_for('index'))
        
    return render_template('add.html')


@app.route('/<int:id>/update/',methods=('GET', 'POST'))
def update(id):
    """
    View function that updates product information based on the product id
    """
    shoe = get_shoe(id)

    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        price = request.form['price']
        quantity = request.form['quantity']
        image_01 = request.files['image_01']
        image_02 = request.files['image_02']
        image_03 = request.files['image_03']
        image_04 = request.files['image_04']
        image_05 = request.files['image_05']
        description = request.form['description']

        if not name:
            flash('Shoe name is required!')
            return render_template('add.html')
        elif not category:
            flash('Shoe category is required')
        elif not price:
            flash('Price is required')
        elif not quantity:
            flash('Quantity is required')
        elif not image_01 or image_01.filename == '':
            flash('Image 01 is required')
        elif not image_02 or image_02.filename == '':
            flash('Image 02 is required')
        elif not image_03 or image_03.filename == '':
            flash('Image 03 is required')
        elif not image_04 or image_04.filename == '':
            flash('Image 04 is required')
        elif not image_05 or image_05.filename == '':
            flash('Image 05 is required')
        elif not description:
            flash('A brief descriptin of the shoe is required')
        else:
            connection = get_db_connection()
            connection.execute('UPDATE products SET product_name = ?, product_category = ?,\
                               product_price = ?, product_quantity = ?, product_image_01 = ?,\
                               product_image_02 = ?, product_image_03 = ?, product_image_04=?,\
                               product_image_05 = ?, description = ?'
                               'WHERE id = ?',
                               (name, category, price, quantity, image_01.read(),
                                image_02.read(), image_03.read(), image_04.read(), image_05.read(),
                                description, id))
            connection.commit()
            connection.close()
            return redirect(url_for('index'))
    return render_template('update.html', shoe=shoe)


@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    """
    view function that deletes a product based on the id
    """
    shoe = get_shoe(id)

    connection = get_db_connection()
    connection.execute('DELETE FROM products WHERE product_id = ?', (id,))
    connection.commit()
    connection.close()

    flash('"{}" was successfully deleted!'.format(shoe['product_name']))
    return redirect(url_for('index'))