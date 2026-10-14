CREATE DATABASE IF NOT EXISTS login_system_db;
USE login_system_db;

CREATE TABLE IF NOT EXISTS users(
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    passw varchar (256) NOT NULL,
    email VARCHAR (100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products (
    id_product INT BIGINT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
)
INSERT INTO users (username, passw, nombre) VALUES ('admin','admin123','superadmin');