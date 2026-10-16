from Controller.database_connection import Database_connection


class Product:

    def __init__(self, name="", description="", category="", price=0.0, stock=0, product_id=None):
        self.id = product_id
        self.name = name
        self.description = description
        self.category = category
        self.price = price
        self.stock = stock
        self.db = Database_connection()

    # ---------- Consultas ----------
    def get_all(self):
        query = "SELECT * FROM products ORDER BY id"
        return self.db.ejecutar_consulta(query) or []

    def get_by_id(self, product_id):
        query = "SELECT * FROM products WHERE id = %s"
        result = self.db.ejecutar_consulta(query, (product_id,))
        return result[0] if result else None

    def search(self, text):
        query = "SELECT * FROM products WHERE name LIKE %s OR category LIKE %s ORDER BY id"
        like = f"%{text}%"
        return self.db.ejecutar_consulta(query, (like, like)) or []

    # ---------- Comandos ----------
    def create(self):
        query = (
            "INSERT INTO products (name, description, category, price, stock) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        result = self.db.ejecutar_comando(
            query, (self.name, self.description, self.category, self.price, self.stock)
        )
        if result:
            self.id = result[1]
        return result is not None

    def update(self):
        query = (
            "UPDATE products SET name = %s, description = %s, category = %s, "
            "price = %s, stock = %s WHERE id = %s"
        )
        result = self.db.ejecutar_comando(
            query,
            (self.name, self.description, self.category, self.price, self.stock, self.id),
        )
        return result is not None and result[0] > 0

    def delete(self):
        query = "DELETE FROM products WHERE id = %s"
        result = self.db.ejecutar_comando(query, (self.id,))
        return result is not None and result[0] > 0
