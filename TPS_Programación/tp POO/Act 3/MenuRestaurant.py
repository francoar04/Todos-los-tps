from ingredientes import Ingrediente
from plato import Plato

class MenuRestaurant:
    @staticmethod
    def main():
        platosMenu = []
        salirPlato = ""
        while salirPlato != "SI":
            print("===CARGA DE PLATOS===")
            nombrePlato = input("Ingrese el nombre completo del plato: ").strip()
            while nombrePlato == "":
                print("Error: El nombre del plato no puede estar vacío.")
                nombrePlato = input("Ingrese el nombre completo del plato: ").strip()
            precio_valido = False
            while not precio_valido:
                precio_str = input("Ingrese el precio: ").strip().replace(',', '.')
                if precio_str.replace('.', '', 1).isdigit() and precio_str.count('.') <= 1:
                    precio = float(precio_str)
                    precio_valido = True
                else:
                    print("Error: Ingrese un valor numérico válido para el precio.")
            bebida_str = input("¿Es una bebida? (SI/NO): ").strip().upper()
            while bebida_str not in ["SI", "NO"]:
                print("Por favor responda 'SI' o 'NO'.")
                bebida_str = input("¿Es una bebida? (SI/NO): ").strip().upper()
            bebida = (bebida_str == "SI")
            un_plato = Plato(nombrePlato, precio, bebida)
            if not bebida:
                salirIngredientes = ""
                while salirIngredientes != "SI":
                    print("\n  --- Carga de Ingrediente ---")
                    nombreIngrediente = input("  Nombre del ingrediente: ").strip()
                    while nombreIngrediente == "":
                        print("  Error: El nombre del ingrediente no puede estar vacío.")
                        nombreIngrediente = input("  Nombre del ingrediente: ").strip()
                    cantidad_valida = False
                    while not cantidad_valida:
                        cant_str = input("  Cantidad: ").strip().replace(',', '.')
                        if cant_str.replace('.', '', 1).isdigit() and cant_str.count('.') <= 1:
                            cantidad = float(cant_str)
                            cantidad_valida = True
                        else:
                            print("  Error: Ingrese un valor numérico válido para la cantidad.")
                    unidadMedida = input("  Unidad de medida (ej. gramos, unidad): ").strip()
                    while unidadMedida == "":
                        print("  Error: La unidad de medida no puede estar vacía.")
                        unidadMedida = input("  Unidad de medida (ej. gramos, unidad): ").strip()
                    un_ingrediente = Ingrediente(nombreIngrediente, cantidad, unidadMedida)
                    un_plato.ingredientes.append(un_ingrediente)
                    salirIngredientes = input("  ¿Desea salir de la carga de ingredientes? (SI/NO): ").strip().upper()
                    while salirIngredientes not in ["SI", "NO"]:
                        print("  Por favor responda 'SI' o 'NO'.")
                        salirIngredientes = input("  ¿Desea salir de la carga de ingredientes? (SI/NO): ").strip().upper()
            platosMenu.append(un_plato)
            salirPlato = input("\n¿Desea salir de la carga de platos? (SI/NO): ").strip().upper()
            while salirPlato not in ["SI", "NO"]:
                print("Por favor responda 'SI' o 'NO'.")
                salirPlato = input("\n¿Desea salir de la carga de platos? (SI/NO): ").strip().upper()
        print("\n" + "-----------MENÚ----------------")
        for plato in platosMenu:
            print(f"{plato.nombreCompleto}")
            print(f"Precio: $ {plato.precio}")
            if not plato.bebida and len(plato.ingredientes) > 0:
                print("Ingredientes:")
                print(f"Nombre\t\tCantidad\tUnidad de Medida")
                for ing in plato.ingredientes:
                    print(f"{ing.nombre}\t\t{ing.cantidad}\t\t{ing.unidadMedida}")
            print("-" * 34)
if __name__ == "__main__":
    MenuRestaurant.main()