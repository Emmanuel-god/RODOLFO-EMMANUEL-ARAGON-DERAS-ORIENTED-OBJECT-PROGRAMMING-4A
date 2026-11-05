from Controller.database_connection import Database_connection


class Product:
    """Modelo de la tabla `products` (inventario de la tienda de videojuegos)."""

    def __init__(self):
        self.db = Database_connection()

    def listar(self):
        """Devuelve todos los productos como lista de diccionarios, o None si hubo error."""
        query = (
            "SELECT id, nombre, categoria, precio, stock "
            "FROM products ORDER BY id"
        )
        return self.db.ejecutar_consulta(query)
