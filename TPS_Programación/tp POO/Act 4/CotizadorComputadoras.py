from componente import Componente
from computadora import Computadora

class CotizadorComputadoras:
    @staticmethod
    def main():
        salirPrograma = ""
        while salirPrograma != "SI":
            print("====COTIZADOR DE COMPUTADORAS====")
            marca_valida = False
            while not marca_valida:
                marcaPC = input("Ingrese la marca de la computadora: ").strip()
                if marcaPC == "":
                    print("Error: La marca no puede estar vacía.")
                elif any(c.isdigit() for c in marcaPC):
                    print("Error: La marca no puede contener números.")
                else:
                    marca_valida = True
            modeloPC = input("Ingrese el modelo de la computadora: ").strip()
            while modeloPC == "":
                print("Error: El modelo no puede estar vacío.")
                modeloPC = input("Ingrese el modelo de la computadora: ").strip()
            computadora = Computadora(marcaPC, modeloPC)
            salirComponentes = ""
            while salirComponentes != "SI":
                print("\n  --- Carga de Componente ---")
                nombreComp = input("  Nombre del componente: ").strip()
                while nombreComp == "":
                    print("  Error: El nombre no puede estar vacío.")
                    nombreComp = input("  Nombre del componente: ").strip()
                marcaComp = input("  Marca del componente: ").strip()
                while marcaComp == "":
                    print("  Error: La marca no puede estar vacía.")
                    marcaComp = input("  Marca del componente: ").strip()
                cantidad_valida = False
                while not cantidad_valida:
                    cant_str = input("  Cantidad: ").strip()
                    if cant_str.isdigit() and int(cant_str) > 0:
                        cantidad = int(cant_str)
                        cantidad_valida = True
                    else:
                        print("  Error: Ingrese un número entero válido mayor a 0.")
                precio_valido = False
                while not precio_valido:
                    precio_str = input("  Precio por unidad: ").strip().replace(',', '.')
                    if precio_str.replace('.', '', 1).isdigit() and precio_str.count('.') <= 1:
                        precioUnitario = float(precio_str)
                        if precioUnitario >= 0:
                            precio_valido = True
                        else:
                            print("  Error: El precio no puede ser negativo.")
                    else:
                        print("  Error: Ingrese un valor numérico válido.")
                un_componente = Componente(nombreComp, marcaComp, cantidad, precioUnitario)
                computadora.componentes.append(un_componente)
                salirComponentes = input("  ¿Desea salir de la carga de componentes? (SI/NO): ").strip().upper()
                while salirComponentes not in ["SI", "NO"]:
                    print("  Por favor responda 'SI' o 'NO'.")
                    salirComponentes = input("  ¿Desea salir de la carga de componentes? (SI/NO): ").strip().upper()
            costoTotal, ganancia, precioVenta = computadora.calcularPrecioVenta()
            print("\n====Computadora====")
            print(f"Marca: {computadora.marca}")
            print(f"Modelo: {computadora.modelo}")
            print("Componentes:")
            print(f"{'Componente':<18} {'Marca':<12} {'Cantidad':<10} {'Precio X Unidad':<16} {'SubTotal'}")
            for comp in computadora.componentes:
                subtotal = comp.calcularSubtotal()
                print(f"{comp.nombre:<18} {comp.marca:<12} {comp.cantidad:<10} {comp.precioUnitario:<16} {subtotal}")
            print("-" * 55)
            print(f"{'Costo Total':<44} {costoTotal}")
            print("-" * 55)
            print(f"El precio sugerido de venta es {costoTotal} + {ganancia:.0f} = {precioVenta:.0f}")
            print("-------------------------------------------------------")
            salirPrograma = input("\n¿Desea cotizar una nueva computadora? (SI/NO): ").strip().upper()
            while salirPrograma not in ["SI", "NO"]:
                print("Por favor responda 'SI' o 'NO'.")
                salirPrograma = input("\n¿Desea cotizar una nueva computadora? (SI/NO): ").strip().upper()
if __name__ == "__main__":
    CotizadorComputadoras.main()