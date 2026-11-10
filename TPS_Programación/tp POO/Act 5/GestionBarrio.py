from barrio import Barrio
from vivienda import Vivienda
from habitacion import Habitacion

class GestionBarrio:
    @staticmethod
    def main():
        print("====SISTEMA DE GESTIÓN DE BARRIOS====")
        nombreBarrio = input("Ingrese el nombre del barrio: ").strip()
        while nombreBarrio == "":
            print("Error: El nombre no puede estar vacío.")
            nombreBarrio = input("Ingrese el nombre del barrio: ").strip()
        empresa = input("Ingrese la empresa constructora: ").strip()
        while empresa == "":
            print("Error: La empresa no puede estar vacía.")
            empresa = input("Ingrese la empresa constructora: ").strip()
        mi_barrio = Barrio(nombreBarrio, empresa)
        salirViviendas = ""
        while salirViviendas != "SI":
            print("\n--- Carga de Vivienda ---")
            calle = input("Calle: ").strip()
            while calle == "":
                print("Error: La calle no puede estar vacía.")
                calle = input("Calle: ").strip()
            num_valido = False
            while not num_valido:
                num_str = input("Número: ").strip()
                if num_str.isdigit():
                    numero = int(num_str)
                    num_valido = True
                else:
                    print("Error: Ingrese un número entero válido.")
            manzana = input("Manzana: ").strip()
            while manzana == "":
                print("Error: La manzana no puede estar vacía.")
                manzana = input("Manzana: ").strip()
            nroCasa_valido = False
            while not nroCasa_valido:
                nroCasa_str = input("Nro de Casa: ").strip()
                if nroCasa_str.isdigit():
                    nroCasa = int(nroCasa_str)
                    nroCasa_valido = True
                else:
                    print("Error: Ingrese un número de casa válido.")
            sup_valida = False
            while not sup_valida:
                sup_str = input("Superficie del Terreno (m2): ").strip().replace(',', '.')
                if sup_str.replace('.', '', 1).isdigit() and sup_str.count('.') <= 1:
                    superficieTerreno = float(sup_str)
                    if superficieTerreno > 0:
                        sup_valida = True
                    else:
                        print("Error: La superficie debe ser mayor a 0.")
                else:
                    print("Error: Ingrese un valor numérico válido.")
            una_vivienda = Vivienda(calle, numero, manzana, nroCasa, superficieTerreno)
            salirHabitaciones = ""
            while salirHabitaciones != "SI":
                print("\n    -- Carga de Habitación --")
                nombreHab = input("    Nombre de la habitación: ").strip()
                while nombreHab == "":
                    print("    Error: El nombre no puede estar vacío.")
                    nombreHab = input("    Nombre de la habitación: ").strip()
                mt_valido = False
                while not mt_valido:
                    mt_str = input("    Metros cuadrados: ").strip().replace(',', '.')
                    if mt_str.replace('.', '', 1).isdigit() and mt_str.count('.') <= 1:
                        metrosCuadrados = float(mt_str)
                        if metrosCuadrados > 0:
                            mt_valido = True
                        else:
                            print("    Error: Los metros deben ser mayores a 0.")
                    else:
                        print("    Error: Ingrese un valor numérico válido.")
                una_habitacion = Habitacion(nombreHab, metrosCuadrados)
                una_vivienda.habitaciones.append(una_habitacion)
                salirHabitaciones = input("    ¿Desea salir de la carga de habitaciones? (SI/NO): ").strip().upper()
                while salirHabitaciones not in ["SI", "NO"]:
                    print("    Por favor responda 'SI' o 'NO'.")
                    salirHabitaciones = input("    ¿Desea salir de la carga de habitaciones? (SI/NO): ").strip().upper()
            mi_barrio.viviendas.append(una_vivienda)
            salirViviendas = input("\n¿Desea salir de la carga de viviendas? (SI/NO): ").strip().upper()
            while salirViviendas not in ["SI", "NO"]:
                print("Por favor responda 'SI' o 'NO'.")
                salirViviendas = input("\n¿Desea salir de la carga de viviendas? (SI/NO): ").strip().upper()
        print(f"====INFORME DEL BARRIO: {mi_barrio.nombre}====")
        print(f"====Empresa: {mi_barrio.empresaConstructora}====")
        totalTerreno = mi_barrio.getSuperficieTotalTerreno()
        print(f"a) Superficie Total de Terreno del Barrio: {totalTerreno:.2f} m2")
        consultaManzana = input("\nIngrese una Manzana para consultar su superficie de terreno: ").strip()
        totalTerrenoMza = mi_barrio.getSuperficieTotalTerrenoXManzana(consultaManzana)
        print(f"b) Superficie Total de Terreno en Manzana '{consultaManzana}': {totalTerrenoMza:.2f} m2")
        print("\nc) Detalle de Metros Cuadrados Cubiertos por Vivienda:")
        for v in mi_barrio.viviendas:
            cubiertos = v.getMetrosCuadradosCubiertos()
            print(f"   - Casa Nro {v.nroCasa} (Calle {v.calle} {v.numero}, Mza {v.manzana}): {cubiertos:.2f} m2 cubiertos")
        totalCubiertaBarrio = mi_barrio.getSuperficieTotalCubierta()
        print(f"\nd) Superficie Total Cubierta del Barrio: {totalCubiertaBarrio:.2f} m2")
if __name__ == "__main__":
    GestionBarrio.main()