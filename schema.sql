DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number INT NOT NULL,
    hashed_password VARCHAR NOT NULL
);

DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    product_category TEXT NOT NULL,
    product_price INTEGER NOT NULL,
    product_quantity INTEGER NOT NULL,
    product_image_01 BLOB NOT NULL,
    product_image_02 BLOB NOT NULL,
    product_image_03 BLOB,
    product_image_04 BLOB,
    product_image_05 BLOB,
    product_description VARCHAR NOT NULL
);
