CREATE DATABASE IF NOT EXISTS login_system_db;
USE login_system_db;
DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL UNIQUE,
    password VARCHAR(256) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, password, nombre, email)
VALUES ('admin', 'admin123', 'super admin');

DROP TABLE IF EXISTS products;

CREATE TABLE products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO products (name, description, category, price, stock) VALUES
('Laptop Lenovo IdeaPad 15', 'Laptop 15.6" Ryzen 5, 8GB RAM, 512GB SSD', 'Computo', 11499.00, 12),
('Mouse inalámbrico Logitech M170', 'Mouse óptico inalámbrico 2.4GHz', 'Accesorios', 249.90, 60),
('Teclado mecánico Redragon Kumara', 'Teclado mecánico retroiluminado TKL', 'Accesorios', 799.00, 25),
('Monitor Samsung 24"', 'Monitor Full HD IPS 75Hz', 'Monitores', 2899.00, 15),
('Memoria USB Kingston 64GB', 'USB 3.2 de alta velocidad', 'Almacenamiento', 149.00, 100),
('Disco SSD Kingston 480GB', 'SSD SATA 2.5" A400', 'Almacenamiento', 619.00, 40),
('Audífonos Sony WH-CH520', 'Audífonos Bluetooth on-ear', 'Audio', 1099.00, 18),
('Webcam Logitech C270 HD', 'Cámara web HD 720p con micrófono', 'Accesorios', 549.00, 30);
