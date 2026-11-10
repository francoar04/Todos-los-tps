import requests

URL_BASE = "http://127.0.0.1:5000"


def probar_api():
    print("1. GET /api/libros")
    respuesta = requests.get(f"{URL_BASE}/api/libros")
    print("Estado:", respuesta.status_code)
    print("Respuesta:", respuesta.json())
    respuesta.raise_for_status()

    print("\n2. POST /api/autores")
    respuesta = requests.post(
        f"{URL_BASE}/api/autores",
        json={"nombre": "Autor de Prueba", "nacionalidad": "Argentina"},
    )
    print("Estado:", respuesta.status_code)
    print("Respuesta:", respuesta.json())
    respuesta.raise_for_status()
    autor_id = respuesta.json()["id"]

    print("\n2. POST /api/libros")
    respuesta = requests.post(
        f"{URL_BASE}/api/libros",
        json={"titulo": "Libro de Prueba", "anio": 2024, "autor_id": autor_id},
    )
    print("Estado:", respuesta.status_code)
    print("Respuesta:", respuesta.json())
    respuesta.raise_for_status()
    libro_id = respuesta.json()["id"]

    print(f"\n3. PUT /api/libros/{libro_id}")
    respuesta = requests.put(
        f"{URL_BASE}/api/libros/{libro_id}",
        json={"titulo": "Título Actualizado"},
    )
    print("Estado:", respuesta.status_code)
    print("Respuesta:", respuesta.json())
    respuesta.raise_for_status()
    assert respuesta.json()["titulo"] == "Título Actualizado"

    print(f"\n4. DELETE /api/libros/{libro_id}")
    respuesta = requests.delete(f"{URL_BASE}/api/libros/{libro_id}")
    print("Estado:", respuesta.status_code)
    print("Respuesta:", respuesta.json())
    respuesta.raise_for_status()
    assert respuesta.json()["mensaje"] == "Libro eliminado correctamente"

    respuesta = requests.get(f"{URL_BASE}/api/libros/{libro_id}")
    assert respuesta.status_code == 404
    print("\nEl libro fue eliminado correctamente.")


if __name__ == "__main__":
    probar_api()
