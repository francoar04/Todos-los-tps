class Componente:
    def __init__(self, nombre: str, marca: str, cantidad: int, precioUnitario: float):
        self.nombre = nombre
        self.marca = marca
        self.cantidad = cantidad
        self.precioUnitario = precioUnitario
    def calcularSubtotal(self):
        return self.cantidad * self.precioUnitario