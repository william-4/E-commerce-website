#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as schema:
    # execute multiple SQL statements at once
    connection.executescript(schema.read())

# process rows in the database
cursor = connection.cursor()


# add items to products table
for i in range(20):
    product_id = i
    product_name = "shoe {}".format(i)
    product_category = "category_{}".format(i)
    product_price = i + 1000
    product_quantity = i + 10
    product_image_01 = "image 01-{}".format(i)
    product_image_02 = "image 02-{}".format(i)
    product_image_03 = "image 03-{}".format(i)
    product_image_04 = "image 04-{}".format(i)
    product_image_05 = "image 05-{}".format(i)
    product_description = "description 0{}".format(i)

    cursor.execute("INSERT INTO products (product_id, product_name, product_category,\
            product_price, product_quantity, product_image_01, product_image_02, product_image_03,\
            product_image_04, product_image_05, product_description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                   (product_id, product_name, product_category, product_price, 
                    product_quantity, product_image_01, product_image_02, product_image_03,
                     product_image_04, product_image_05, product_description)
                    );

connection.commit()
cursor.close()
connection.close()