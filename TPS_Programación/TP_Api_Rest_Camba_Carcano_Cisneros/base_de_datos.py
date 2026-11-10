import os
import sqlite3
from contextlib import closing

RUTA_BD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "biblioteca.db")


def conectar():
    conexion = sqlite3.connect(RUTA_BD)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def inicializar_db():
    with closing(conectar()) as conexion, conexion:
        conexion.executescript(
            """
            CREATE TABLE IF NOT EXISTS autores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                nacionalidad TEXT NOT NULL
            );

            -- "titulo" y "anio" se mantienen sin tilde porque son los
            -- nombres de campo que exige el trabajo práctico.
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                anio INTEGER NOT NULL,
                autor_id INTEGER NOT NULL,
                FOREIGN KEY (autor_id) REFERENCES autores (id) ON DELETE CASCADE
            );
            """
        )


def _libro_desde_fila(fila):
    return {
        "id": fila["id"],
        "titulo": fila["titulo"],
        "anio": fila["anio"],
        "autor_id": fila["autor_id"],
        "autor": {
            "id": fila["autor_id"],
            "nombre": fila["autor_nombre"],
            "nacionalidad": fila["autor_nacionalidad"],
        },
    }


def obtener_autores_db(conexion=None):
    if conexion:
        filas = conexion.execute("SELECT id, nombre, nacionalidad FROM autores ORDER BY id").fetchall()
        return [dict(fila) for fila in filas]
    
    with closing(conectar()) as conexion_db:
        return obtener_autores_db(conexion=conexion_db)


def obtener_autor_db(id, conexion=None):
    if conexion:
        fila = conexion.execute(
            "SELECT id, nombre, nacionalidad FROM autores WHERE id = ?", (id,)
        ).fetchone()
        return dict(fila) if fila else None

    with closing(conectar()) as conexion_db:
        return obtener_autor_db(id, conexion=conexion_db)


def insertar_autor_db(nombre, nacionalidad):
    with closing(conectar()) as conexion, conexion:
        cursor = conexion.execute(
            "INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)",
            (nombre, nacionalidad),
        )
        return obtener_autor_db(cursor.lastrowid, conexion=conexion)


def obtener_libros_db():
    with closing(conectar()) as conexion:
        filas = conexion.execute(
            """
            SELECT
                l.id, l.titulo, l.anio, l.autor_id,
                a.nombre AS autor_nombre,
                a.nacionalidad AS autor_nacionalidad
            FROM libros l
            JOIN autores a ON a.id = l.autor_id
            ORDER BY l.id
            """
        ).fetchall()
    return [_libro_desde_fila(fila) for fila in filas]


def obtener_libro_db(id, conexion=None):
    if conexion:
        fila = conexion.execute(
            """
            SELECT
                l.id, l.titulo, l.anio, l.autor_id,
                a.nombre AS autor_nombre,
                a.nacionalidad AS autor_nacionalidad
            FROM libros l
            JOIN autores a ON a.id = l.autor_id
            WHERE l.id = ?
            """,
            (id,),
        ).fetchone()
        return _libro_desde_fila(fila) if fila else None

    with closing(conectar()) as conexion_db:
        return obtener_libro_db(id, conexion=conexion_db)


def insertar_libro_db(titulo, año, autor_id):
    with closing(conectar()) as conexion, conexion:
        cursor = conexion.execute(
            "INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)",
            (titulo, año, autor_id),
        )
        return obtener_libro_db(cursor.lastrowid, conexion=conexion)


def actualizar_libro_db(id, titulo, año, autor_id):
    with closing(conectar()) as conexion, conexion:
        conexion.execute(
            "UPDATE libros SET titulo = ?, anio = ?, autor_id = ? WHERE id = ?",
            (titulo, año, autor_id, id),
        )
        return obtener_libro_db(id, conexion=conexion)


def eliminar_libro_db(id):
    with closing(conectar()) as conexion, conexion:
        cursor = conexion.execute("DELETE FROM libros WHERE id = ?", (id,))
        return cursor.rowcount > 0