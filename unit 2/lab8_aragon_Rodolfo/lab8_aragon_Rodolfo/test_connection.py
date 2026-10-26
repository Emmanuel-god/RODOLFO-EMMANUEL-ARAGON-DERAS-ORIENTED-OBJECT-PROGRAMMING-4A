"""Prueba de conexión a PostgreSQL (Lab 8). Ejecutar: python test_connection.py

Diagnostica paso a paso y, si solo falta la base o la tabla, las crea.
"""
import os
import socket

import psycopg2

from Controller.config import DB_config
from Controller.database_connection import Database_connection

RUTA_SQL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Models", "database_squema.sql")


def _conectar(dbname):
    cfg = dict(DB_config)
    cfg["dbname"] = dbname
    return psycopg2.connect(**cfg)


def probar():
    host, port, base = DB_config["host"], DB_config["port"], DB_config["dbname"]

    # 1) ¿El servicio responde en el puerto?
    try:
        socket.create_connection((host, port), timeout=3).close()
        print(f"[OK] PostgreSQL responde en {host}:{port}.")
    except OSError:
        print(f"[X] Nada responde en {host}:{port}. Inicia el servicio de PostgreSQL "
              "(Servicios de Windows -> postgresql-x64-XX) o revisa el puerto en config.py.")
        return False

    # 2) ¿Usuario y contraseña correctos? (se prueba contra la base 'postgres')
    try:
        admin = _conectar("postgres")
    except (UnicodeDecodeError, psycopg2.Error):
        print(f"[X] No se pudo iniciar sesión como '{DB_config['user']}'. "
              "Casi seguro la contraseña de Controller/config.py es incorrecta (o está vacía). "
              "Usa la que definiste al instalar PostgreSQL.")
        return False
    print("[OK] Usuario y contraseña correctos.")

    # 3) ¿Existe la base? Si no, se crea.
    admin.autocommit = True
    cur = admin.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (base,))
    if cur.fetchone() is None:
        cur.execute(f'CREATE DATABASE "{base}"')
        print(f"[OK] La base '{base}' no existía y se creó.")
    else:
        print(f"[OK] La base '{base}' existe.")
    cur.close()
    admin.close()

    # 4) ¿Existe la tabla users? Si no, se crea desde el .sql
    db = Database_connection()
    tabla = db.ejecutar_consulta("SELECT to_regclass('public.users') AS tabla")
    if tabla is None:
        print("[X] No se pudo consultar la base. Revisa el mensaje de arriba.")
        return False
    if not tabla[0]["tabla"]:
        with open(RUTA_SQL, encoding="utf-8") as f:
            sql = f.read()
        conexion = db.get_connection()
        cursor = conexion.cursor()
        cursor.execute(sql)
        conexion.commit()
        cursor.close()
        conexion.close()
        print("[OK] La tabla 'users' no existía y se creó con Models/database_squema.sql.")

    total = db.ejecutar_consulta("SELECT COUNT(*) AS total FROM users")
    print(f"[OK] Tabla 'users' lista ({total[0]['total']} usuarios). Ya puedes correr main.py.")
    return True


if __name__ == "__main__":
    probar()