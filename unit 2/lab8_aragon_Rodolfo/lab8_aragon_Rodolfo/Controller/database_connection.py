import psycopg2
import psycopg2.extras
from psycopg2 import Error
from Controller.config import DB_config


class Database_connection:
    def __init__(self):
        self.config = DB_config

    def get_connection(self):
        try:
            return psycopg2.connect(**self.config)
        except UnicodeDecodeError:
            # En Windows en español, PostgreSQL responde con mensajes de error
            # en Windows-1252 (por ejemplo «lab8_login») y psycopg2 no puede
            # decodificarlos. Reintentamos con LATIN1 solo para leer el error real.
            try:
                return psycopg2.connect(client_encoding="LATIN1", **self.config)
            except UnicodeDecodeError:
                print(
                    "Error al conectar con PostgreSQL (mensaje ilegible). Causas comunes:\n"
                    "  1) La base de datos no existe -> CREATE DATABASE lab8_login;\n"
                    "  2) Contraseña/usuario incorrectos en Controller/config.py\n"
                    "  3) El servicio de PostgreSQL no está iniciado o el puerto no es 5432"
                )
            except Error as e:
                print(f"Error al conectar con PostgreSQL: {str(e).strip()}")
            return None
        except Error as e:
            print(f"Error al conectar con PostgreSQL: {e}")
            return None

    def ejecutar_consulta(self, query, params=()):
        conexion = self.get_connection()
        if not conexion:
            return None

        cursor = conexion.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        try:
            cursor.execute(query, params)
            return [dict(fila) for fila in cursor.fetchall()]
        except Error as e:
            print(f"Error en la consulta SQL: {e}")
            return None
        finally:
            cursor.close()
            conexion.close()

    def ejecutar_comando(self, query, params=()):
        conexion = self.get_connection()
        if not conexion:
            return None

        cursor = conexion.cursor()
        try:
            cursor.execute(query, params)
            conexion.commit()
            return cursor.rowcount
        except Error as e:
            conexion.rollback()
            print(f"Error al ejecutar el comando SQL: {e}")
            return None
        finally:
            cursor.close()
            conexion.close()