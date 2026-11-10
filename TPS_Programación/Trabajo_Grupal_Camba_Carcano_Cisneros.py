#Parte_A
# 1. Estructuras de Datos Iniciales
golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

claves_tecnico = ("admin", "CCCDDD", "2020")
golosinas_pedidas = []

# Bucle principal del menú
while True:
    print("\n--- MÁQUINA DE GOLOSINAS ---")
    print("a. Pedir golosina")
    print("b. Mostrar golosinas")
    print("c. Rellenar golosinas")
    print("d. Apagar maquina")
    opcion = input("Seleccione una opción: ").strip().lower()

    if opcion == 'a':
        try:
            legajo = int(input("Ingrese su legajo de empleado: "))
        except ValueError:
            print("Usted no es un empleado de la empresa")
            continue

        if legajo not in empleados:
            print("Usted no es un empleado de la empresa")
            continue

        print(f"Bienvenido/a {empleados[legajo]}")
        
        while True:
            entrada_codigo = input("Ingrese el código de la golosina (o 'salir' para cancelar): ").strip()
            if entrada_codigo.lower() == 'salir':
                break
            
            if not entrada_codigo.isdigit():
                print("Código inválido. Ingrese un número.")
                continue

            codigo = int(entrada_codigo)
            golosina_encontrada = None

            for g in golosinas:
                if g[0] == codigo:
                    golosina_encontrada = g
                    break

            if golosina_encontrada is None:
                print("Código de golosina no existe.")
                continue

            # Verificación de stock
            if golosina_encontrada[2] <= 0:
                print(f"Lo sentimos la golosina {golosina_encontrada[1]} no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina")
            else:
                # Descontar stock
                golosina_encontrada[2] -= 1
                
                # Registrar en golosinas_pedidas
                existe_en_pedidas = False
                for item in golosinas_pedidas:
                    if item[0] == golosina_encontrada[0]:
                        item[2] += 1
                        existe_en_pedidas = True
                        break
                
                if not existe_en_pedidas:
                    golosinas_pedidas.append([golosina_encontrada[0], golosina_encontrada[1], 1])
                
                print(f"¡Disfrute su {golosina_encontrada[1]}!")
                break

    elif opcion == 'b':
        print("\n--- INVENTARIO DE GOLOSINAS ---")
        for g in golosinas:
            print(f"Código: {g[0]:2d} | Golosina: {g[1]:20s} | Stock: {g[2]}")

    elif opcion == 'c':
        print("\n--- ACCESO TÉCNICO ---")
        p1 = input("Ingrese clave 1: ")
        p2 = input("Ingrese clave 2: ")
        p3 = input("Ingrese clave 3: ")

        if (p1, p2, p3) == claves_tecnico:
            try:
                codigo = int(input("Ingrese código de golosina a recargar: "))
                golosina_encontrada = None
                for g in golosinas:
                    if g[0] == codigo:
                        golosina_encontrada = g
                        break
                
                if golosina_encontrada:
                    cantidad = int(input("Ingrese la cantidad a recargar (> 0): "))
                    if cantidad > 0:
                        golosina_encontrada[2] += cantidad
                        print(f"Stock actualizado. Nuevo stock de {golosina_encontrada[1]}: {golosina_encontrada[2]}")
                    else:
                        print("La cantidad debe ser mayor a cero.")
                else:
                    print("Código de golosina no encontrado.")
            except ValueError:
                print("Entrada numérica inválida.")
        else:
            print("No tiene permiso para ejecutar la función de recarga")

    elif opcion == 'd':
        print("\n==========================================")
        print("          RESUMEN DE GOLOSINAS PEDIDAS    ")
        print("==========================================")
        total_acumulado = 0
        for item in golosinas_pedidas:
            print(f"Código: {item[0]:2d} | Golosina: {item[1]:20s} | Pedidas: {item[2]}")
            total_acumulado += item[2]
        print("------------------------------------------")
        print(f"Total general de golosinas pedidas: {total_acumulado}")
        print("Apagando máquina...")
        break
#Parte_B
# 1. Diccionario de Alumnos (Legajo: Nombre)
alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

# 2. Lista base de materias
materias_nombres = ["Ciencias", "Historia", "Geografia", "Matematicas", "Fisica"]

# 3. Lista final acumuladora de promedios generales
notas_finales = []

# Proceso de carga por alumno
for legajo, nombre_alumno in alumnos.items():
    print(f"\n==========================================")
    print(f"Alumno: {nombre_alumno} (Legajo: {legajo})")
    print(f"==========================================")
    
    materias_alumno = []
    
    # Carga de materias y calificaciones
    for mat_nombre in materias_nombres:
        print(f"\nIngrese las notas para la materia: {mat_nombre}")
        
        # Validar Nota 1
        while True:
            try:
                nota1 = float(input("  Nota 1 (0 a 10): "))
                if 0 <= nota1 <= 10:
                    break
                print("  Error: La nota debe estar entre 0 y 10.")
            except ValueError:
                print("  Error: Ingrese un valor numérico válido.")
                
        # Validar Nota 2
        while True:
            try:
                nota2 = float(input("  Nota 2 (0 a 10): "))
                if 0 <= nota2 <= 10:
                    break
                print("  Error: La nota debe estar entre 0 y 10.")
            except ValueError:
                print("  Error: Ingrese un valor numérico válido.")
                
        # Cálculo de Nota Final de la materia
        nota_final = (nota1 + nota2) / 2.0
        print(f"  Nota Final {mat_nombre}: {nota_final:.2f}")
        
        # Guardar en la estructura bidimensional del alumno
        materias_alumno.append([mat_nombre, nota1, nota2, nota_final])

    # Mostrar lista de materias completa del alumno
    print(f"\n--- RESUMEN DE MATERIAS DE {nombre_alumno.upper()} ---")
    materia_mas_alta = materias_alumno[0]
    suma_notas_finales = 0.0

    for m in materias_alumno:
        print(f"Materia: {m[0]:12s} | Nota 1: {m[1]:4.1f} | Nota 2: {m[2]:4.1f} | Nota Final: {m[3]:4.2f}")
        suma_notas_finales += m[3]
        
        # Determinar la materia con la calificación más alta
        if m[3] > materia_mas_alta[3]:
            materia_mas_alta = m

    # Mostrar materia con nota más alta
    print(f"\nMateria con la calificación más alta: {materia_mas_alta[0]} con {materia_mas_alta[3]:.2f}")

    # Calcular promedio general del alumno
    promedio_general = suma_notas_finales / len(materias_alumno)
    notas_finales.append([nombre_alumno, promedio_general])

# Determinación del estudiante con el mejor promedio general
print("\n==========================================")
print("       RESUMEN DE NOTAS FINALES INSTITUTO ")
print("==========================================")
mejor_alumno = notas_finales[0]

for nf in notas_finales:
    print(f"Estudiante: {nf[0]:22s} | Promedio General: {nf[1]:4.2f}")
    if nf[1] > mejor_alumno[1]:
        mejor_alumno = nf

print("------------------------------------------")
print(f"MEJOR PROMEDIO GENERAL: {mejor_alumno[0]} con un promedio de {mejor_alumno[1]:.2f}")
print("==========================================")