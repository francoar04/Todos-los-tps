#Ejercicio 1
import sqlite3

class Autor:
    def __init__(self, id_autor: int, nombre: str, nacionalidad: str):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self) -> str:
        return f"Autor[{self.id_autor}]: {self.nombre} ({self.nacionalidad})"

class Libro:
    def __init__(self, id_libro: int, titulo: str, anio_publicacion: int, autor: Autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor

    def __str__(self) -> str:
        return (f"Libro[{self.id_libro}]: '{self.titulo}' "
                f"({self.anio_publicacion}) - Autor: {self.autor.nombre}")


DB = 'biblioteca.db'


def conectar() -> sqlite3.Connection:
    conexion = sqlite3.connect(DB)
    conexion.execute('PRAGMA foreign_keys = ON')  # SQLite no controla las FK si no se activa
    return conexion


def inicializar_db() -> None:
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            nacionalidad TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            anio INTEGER,
            autor_id INTEGER,
            FOREIGN KEY (autor_id) REFERENCES autores(id)
        )
    ''')

    conexion.commit()
    conexion.close()


#Ejercicio 3
def registrar_autor(nombre: str, nacionalidad: str) -> int:
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)',
                   (nombre, nacionalidad))
    conexion.commit()
    id_generado = cursor.lastrowid  # ID que SQLite le asignó al autor
    conexion.close()
    return id_generado


def registrar_libro(titulo: str, anio: int, autor_id: int) -> int:
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)',
                   (titulo, anio, autor_id))
    conexion.commit()
    id_generado = cursor.lastrowid
    conexion.close()
    return id_generado


def listar_libros() -> list[Libro]:
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT libros.id, libros.titulo, libros.anio,
               autores.id, autores.nombre, autores.nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
    ''')
    filas = cursor.fetchall()
    conexion.close()

    libros = []
    for id_libro, titulo, anio, id_autor, nombre, nacionalidad in filas:
        autor = Autor(id_autor, nombre, nacionalidad)
        libro = Libro(id_libro, titulo, anio, autor)
        libros.append(libro)
        print(libro)
    return libros


def actualizar_titulo_libro(id_libro: int, nuevo_titulo: str) -> bool:
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('UPDATE libros SET titulo = ? WHERE id = ?', (nuevo_titulo, id_libro))
    conexion.commit()
    actualizado = cursor.rowcount > 0  # False si no existía un libro con ese id
    conexion.close()
    return actualizado


def eliminar_libro(id_libro: int) -> bool:
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM libros WHERE id = ?', (id_libro,))
    conexion.commit()
    eliminado = cursor.rowcount > 0
    conexion.close()
    return eliminado


#Ejercicio 4
if __name__ == '__main__':
    inicializar_db()

    # 2. Registrar 2 autores y 3 libros
    id_borges = registrar_autor('Jorge Luis Borges', 'Argentina')
    id_garcia = registrar_autor('Gabriel García Márquez', 'Colombia')

    id_ficciones = registrar_libro('Ficciones', 1944, id_borges)
    id_aleph = registrar_libro('El Aleph', 1949, id_borges)
    id_cien = registrar_libro('Cien años de soledad', 1967, id_garcia)

    print('--- Libros registrados ---')
    listar_libros()

    nuevo_titulo = 'Ficciones (edición revisada)'
    actualizar_titulo_libro(id_ficciones, nuevo_titulo)

    print('\n--- Después de actualizar ---')
    libros = listar_libros()
    for libro in libros:
        if libro.id_libro == id_ficciones:
            if libro.titulo == nuevo_titulo:
                print(f"Verificado: el libro {id_ficciones} ahora se llama '{libro.titulo}'")
            else:
                print(f"Error: el título no se actualizó")

    eliminar_libro(id_aleph)
    print(f'\n--- Después de eliminar el libro {id_aleph} ---')
    listar_libros()
