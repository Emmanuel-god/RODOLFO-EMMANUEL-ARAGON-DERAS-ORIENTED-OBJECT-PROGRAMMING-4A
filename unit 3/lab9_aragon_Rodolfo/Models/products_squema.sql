-- Tabla de productos (no destructiva: se puede ejecutar varias veces).
CREATE TABLE IF NOT EXISTS products(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    precio NUMERIC(10, 2) NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0
);

-- Datos de ejemplo solo si la tabla está vacía.
INSERT INTO products (nombre, categoria, precio, stock)
SELECT * FROM (VALUES
    ('The Legend of Zelda: Tears of the Kingdom', 'Aventura', 1399.00, 12),
    ('Super Mario Bros. Wonder', 'Plataformas', 1199.00, 20),
    ('EA Sports FC 25', 'Deportes', 1099.00, 15),
    ('Elden Ring', 'RPG', 999.00, 8),
    ('Mortal Kombat 1', 'Pelea', 899.00, 10),
    ('Control DualSense', 'Accesorios', 1599.00, 6),
    ('Tarjeta PSN $500', 'Tarjetas', 500.00, 50),
    ('Minecraft', 'Sandbox', 599.00, 25)
) AS v(nombre, categoria, precio, stock)
WHERE NOT EXISTS (SELECT 1 FROM products);
