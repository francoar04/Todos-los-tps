class Computadora:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.componentes = []
    def calcularCostoTotal(self):
        total = 0
        for comp in self.componentes:
            total += comp.calcularSubtotal()
        return total
    def calcularPrecioVenta(self):
        costo = self.calcularCostoTotal()
        if costo < 50000:
            porcentaje = 0.40
        else:
            porcentaje = 0.3
        ganancia = costo * porcentaje
        precioVenta = costo + ganancia
        return costo, ganancia, precioVenta