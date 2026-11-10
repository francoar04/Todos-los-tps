from habitacion import Habitacion

class Vivienda:
    def __init__(self, calle: str, numero: int, manzana: str, nroCasa: int, superficieTerreno: float):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = []
    def getMetrosCuadradosCubiertos(self):
        totalCubiertos = 0
        for hab in self.habitaciones:
            totalCubiertos += hab.metrosCuadrados
        if totalCubiertos > self.superficieTerreno:
            print(f"Alerta: La superficie cubierta ({totalCubiertos}) supera al terreno ({self.superficieTerreno}).")
        return totalCubiertos