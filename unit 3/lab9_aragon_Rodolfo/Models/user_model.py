from Controller.database_connection import Database_connection


class User:
    """Modelo de la tabla `users` (Lab 8)."""

    def __init__(self, nombre="", email="", passw=""):
        self.nombre = nombre
        self.email = email
        self.password = passw
        self.db = Database_connection()

    # ---------- Consultas ----------
    def auth(self):
        """Devuelve la lista de coincidencias (vacía si no existe) o None si hubo error."""
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        return self.db.ejecutar_consulta(query, (self.email, self.password))

    def exists(self):
        query = "SELECT id FROM users WHERE email = %s"
        result = self.db.ejecutar_consulta(query, (self.email,))
        if result is None:
            return None
        return len(result) > 0

    # ---------- Comandos ----------
    def create(self):
        """Devuelve 'ok', 'duplicado' o 'error'."""
        existe = self.exists()
        if existe is None:
            return "error"
        if existe:
            return "duplicado"

        query = "INSERT INTO users (nombre, email, password) VALUES (%s, %s, %s)"
        result = self.db.ejecutar_comando(query, (self.nombre, self.email, self.password))
        return "ok" if result is not None else "error"
