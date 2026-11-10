from Archivo import Archivo
from Directorio import Directorio


def calcular_tamano_total(directorio: Directorio) -> int:
    total = sum(archivo.tamano_bytes for archivo in directorio.archivos)

    for subdirectorio in directorio.subdirectorios:
        total += calcular_tamano_total(subdirectorio)

    return total


def buscar_por_extension(directorio: Directorio, extension: str) -> list[str]:
    def _buscar(directorio_actual: Directorio, ruta_actual: str) -> list[str]:
        resultados = [
            f"{ruta_actual}/{archivo.nombre}"
            for archivo in directorio_actual.archivos
            if archivo.nombre.endswith(extension)
        ]

        for subdirectorio in directorio_actual.subdirectorios:
            resultados.extend(
                _buscar(subdirectorio, f"{ruta_actual}/{subdirectorio.nombre}")
            )

        return resultados

    return _buscar(directorio, directorio.nombre)


def limpiar_archivos_vacios(directorio: Directorio) -> int:
    eliminados = 0
    archivos_conservados = []

    for archivo in directorio.archivos:
        if archivo.tamano_bytes == 0:
            eliminados += 1
        else:
            archivos_conservados.append(archivo)

    directorio.archivos = archivos_conservados

    for subdirectorio in directorio.subdirectorios:
        eliminados += limpiar_archivos_vacios(subdirectorio)

    return eliminados


if __name__ == "__main__":
    root = Directorio("root")

    root.archivos.append(Archivo("documento.pdf", 1566))
    root.archivos.append(Archivo("config.txt", 0))

    imagenes = Directorio("imagenes")
    imagenes.archivos.append(Archivo("foto1.png", 200))
    imagenes.archivos.append(Archivo("foto2.png", 350))
    root.subdirectorios.append(imagenes)

    proyectos = Directorio("proyectos")
    proyectos.archivos.append(Archivo("avance.pdf", 5684))

    temp = Directorio("temp")
    temp.archivos.append(Archivo("log.txt", 0))
    proyectos.subdirectorios.append(temp)

    root.subdirectorios.append(proyectos)

    print("Tamaño total:", calcular_tamano_total(root), "bytes")
    print("Archivos .pdf:", buscar_por_extension(root, ".pdf"))
    print("Archivos vacíos eliminados:", limpiar_archivos_vacios(root))
