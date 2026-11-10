from flask import Flask, jsonify, request

from base_de_datos import (
    actualizar_libro_db,
    eliminar_libro_db,
    inicializar_db,
    insertar_autor_db,
    insertar_libro_db,
    obtener_autor_db,
    obtener_autores_db,
    obtener_libro_db,
    obtener_libros_db,
)

aplicacion = Flask(__name__)
inicializar_db()


def faltan_campos(datos, campos):
    if not isinstance(datos, dict):
        return True
    for campo in campos:
        if campo not in datos or datos[campo] is None:
            return True
        if isinstance(datos[campo], str) and not datos[campo].strip():
            return True
    return False


@aplicacion.route("/api/autores", methods=["GET"])
def listar_autores():
    return jsonify(obtener_autores_db()), 200


@aplicacion.route("/api/autores", methods=["POST"])
def crear_autor():
    datos = request.get_json(silent=True)
    if faltan_campos(datos, ["nombre", "nacionalidad"]):
        return jsonify({"error": "Faltan campos obligatorios: nombre, nacionalidad"}), 400

    autor = insertar_autor_db(datos["nombre"], datos["nacionalidad"])
    return jsonify(autor), 201


@aplicacion.route("/api/libros", methods=["GET"])
def listar_libros():
    return jsonify(obtener_libros_db()), 200


@aplicacion.route("/api/libros/<int:libro_id>", methods=["GET"])
def obtener_libro(libro_id):
    libro = obtener_libro_db(libro_id)
    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404
    return jsonify(libro), 200


@aplicacion.route("/api/libros", methods=["POST"])
def crear_libro():
    datos = request.get_json(silent=True)
    if faltan_campos(datos, ["titulo", "anio", "autor_id"]):
        return jsonify({"error": "Faltan campos obligatorios: titulo, anio, autor_id"}), 400

    if obtener_autor_db(datos["autor_id"]) is None:
        return jsonify({"error": "Autor no encontrado"}), 404

    título = datos["titulo"]
    año = datos["anio"]
    libro = insertar_libro_db(título, año, datos["autor_id"])
    return jsonify(libro), 201


@aplicacion.route("/api/libros/<int:libro_id>", methods=["PUT"])
def actualizar_libro(libro_id):
    libro = obtener_libro_db(libro_id)
    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404

    datos = request.get_json(silent=True)
    if not isinstance(datos, dict):
        return jsonify({"error": "El cuerpo de la petición debe ser un JSON válido"}), 400

    título = datos.get("titulo", libro["titulo"])
    año = datos.get("anio", libro["anio"])
    autor_id = datos.get("autor_id", libro["autor_id"])

    if título is None or año is None or autor_id is None:
        return jsonify({"error": "Los campos no pueden ser nulos"}), 400

    if obtener_autor_db(autor_id) is None:
        return jsonify({"error": "Autor no encontrado"}), 404

    libro_actualizado = actualizar_libro_db(libro_id, título, año, autor_id)
    return jsonify(libro_actualizado), 200


@aplicacion.route("/api/libros/<int:libro_id>", methods=["DELETE"])
def borrar_libro(libro_id):
    if obtener_libro_db(libro_id) is None:
        return jsonify({"error": "Libro no encontrado"}), 404

    eliminar_libro_db(libro_id)
    return jsonify({"mensaje": "Libro eliminado correctamente"}), 200


if __name__ == "__main__":
    aplicacion.run(debug=True, port=5000)
