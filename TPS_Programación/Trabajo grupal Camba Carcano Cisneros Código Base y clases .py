
class Archivo:
    def __init__(self, nombre: str, tamano_bytes: int):
        self.nombre = nombre
        self.tamano_bytes = tamano_bytes

class Directorio:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.archivos = []
        self.subdirectorios = []  
#
def calcular_tamano_total(directorio: Directorio) -> int:
    tamaño_local = sum(archivo.tamano_bytes for archivo in directorio.archivos)
    tamaño_subdirectorios = sum(calcular_tamano_total(sub) for sub in directorio.subdirectorios)
    return tamaño_local + tamaño_subdirectorios
def buscar_por_extension(directorio: Directorio, extension: str, ruta_padre: str = "") -> list[str]:
    if ruta_padre == "":
        ruta_actual = directorio.nombre
    else:
        ruta_actual = f"{ruta_padre}/{directorio.nombre}"
    coincidencias = []
    for archivo in directorio.archivos:
        if archivo.nombre.endswith(extension):
            coincidencias.append(f"{ruta_actual}/{archivo.nombre}")
    for sub in directorio.subdirectorios:
        coincidencias.extend(buscar_por_extension(sub, extension, ruta_actual))
    return coincidencias
def limpiar_archivos_vacios(directorio: Directorio) -> int:
    archivos_iniciales = len(directorio.archivos)
    directorio.archivos = [a for a in directorio.archivos if a.tamano_bytes > 0]
    eliminados_locales = archivos_iniciales - len(directorio.archivos)
    eliminados_subdirectorios = 0
    for sub in directorio.subdirectorios:
        eliminados_subdirectorios += limpiar_archivos_vacios(sub)
        
    return eliminados_locales + eliminados_subdirectorios
root = Directorio("root")
root.archivos.append(Archivo("documento.pdf", 1500))
root.archivos.append(Archivo("config.txt", 0))
imagenes = Directorio("imagenes")
imagenes.archivos.append(Archivo("foto1.png", 2000))
imagenes.archivos.append(Archivo("foto2.png", 3500))
root.subdirectorios.append(imagenes)
proyectos = Directorio("proyectos")
proyectos.archivos.append(Archivo("avance.pdf", 800))
temp = Directorio("temp")
temp.archivos.append(Archivo("log.txt", 0))
proyectos.subdirectorios.append(temp)

root.subdirectorios.append(proyectos)


tamaño_total = calcular_tamano_total(root)
print(f"1. Tamaño Total: {tamaño_total} bytes")

archivos_pdf = buscar_por_extension(root, ".pdf")
print(f"2. Archivos PDF encontrados: {archivos_pdf}")
archivos_eliminados = limpiar_archivos_vacios(root)
print(f"3. Total de archivos eliminados: {archivos_eliminados}")
