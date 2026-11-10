import os

ARCHIVO = "alumnos.txt"
APROBADOS = "aprobados.txt"


def es_nota_valida(texto):
    if texto.count(".") > 1 or texto.replace(".", "").isdigit() == False:
        return False
    return 1 <= float(texto) <= 10


def leer_alumnos():
    if not os.path.exists(ARCHIVO):
        open(ARCHIVO, "w", encoding="utf-8").close()
    alumnos = []
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")
            if len(datos) == 4 and es_nota_valida(datos[3]):
                alumnos.append({
                    "nombre": datos[0],
                    "apellido": datos[1],
                    "legajo": datos[2],
                    "nota": float(datos[3]),
                })
    return alumnos


def crear_diccionario(alumnos):
    diccionario = {}
    for alumno in alumnos:
        diccionario[alumno["legajo"]] = alumno
    return diccionario


def formato_nota(nota):
    if nota == int(nota):
        return str(int(nota))
    return str(nota)


def ver_alumnos(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos cargados.")
        return
    for alumno in alumnos:
        print(alumno["nombre"], alumno["apellido"], "- Legajo:", alumno["legajo"], "- Nota promedio:", formato_nota(alumno["nota"]))


def pedir_texto(mensaje):
    texto = input(mensaje).strip()
    while texto.replace(" ", "").isalpha() == False:
        print("Error: solo se permiten letras.")
        texto = input(mensaje).strip()
    return texto


def pedir_legajo():
    legajo = input("Legajo (5 dígitos): ").strip()
    while len(legajo) != 5 or legajo.isdigit() == False:
        print("Error: el legajo debe tener 5 dígitos.")
        legajo = input("Legajo (5 dígitos): ").strip()
    return legajo


def pedir_nota():
    nota = input("Nota promedio (1 a 10): ").strip().replace(",", ".")
    while es_nota_valida(nota) == False:
        print("Error: la nota debe ser un número entre 1 y 10.")
        nota = input("Nota promedio (1 a 10): ").strip().replace(",", ".")
    return float(nota)


def validar_existe_alumno(legajo, diccionario):
    return legajo in diccionario


def agregar_alumno(alumnos, diccionario):
    nombre = pedir_texto("Nombre: ")
    apellido = pedir_texto("Apellido: ")
    legajo = pedir_legajo()
    nota = pedir_nota()
    if validar_existe_alumno(legajo, diccionario):
        print("El legajo", legajo, "ya existe en el archivo alumnos.txt, no se permite su escritura")
        return
    alumno = {"nombre": nombre, "apellido": apellido, "legajo": legajo, "nota": nota}
    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(nombre + ";" + apellido + ";" + legajo + ";" + formato_nota(nota) + "\n")
    alumnos.append(alumno)
    diccionario[legajo] = alumno
    print("Alumno agregado correctamente.")


def guardar_aprobados(alumnos):
    with open(APROBADOS, "w", encoding="utf-8") as archivo:
        for alumno in alumnos:
            if alumno["nota"] >= 6:
                archivo.write(alumno["nombre"] + ";" + alumno["apellido"] + ";" + alumno["legajo"] + ";" + formato_nota(alumno["nota"]) + "\n")
    print("Contenido de aprobados.txt:")
    with open(APROBADOS, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    if contenido == "":
        print("No hay alumnos aprobados.")
    else:
        print(contenido, end="")


def menu():
    alumnos = leer_alumnos()
    diccionario = crear_diccionario(alumnos)
    opcion = ""
    while opcion != "4":
        print()
        print("1. Ver alumnos")
        print("2. Agregar alumno")
        print("3. Generar y mostrar archivo de aprobados")
        print("4. Salir")
        opcion = input("Elegí una opción: ").strip()
        if opcion == "1":
            ver_alumnos(alumnos)
        elif opcion == "2":
            agregar_alumno(alumnos, diccionario)
        elif opcion == "3":
            guardar_aprobados(alumnos)
        elif opcion == "4":
            print("Saliendo...")
        else:
            print("Opción inválida.")


menu()
