from vivienda import Vivienda

class Barrio:
    def __init__(self, nombre: str, empresaConstructora: str):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = []
    def getSuperficieTotalTerreno(self):
        totalTerreno = 0
        for vivienda in self.viviendas:
            totalTerreno += vivienda.superficieTerreno
        return totalTerreno
    def getSuperficieTotalTerrenoXManzana(self, manzana: str):
        totalTerrenoManzana = 0
        for vivienda in self.viviendas:
            if vivienda.manzana.strip().upper() == manzana.strip().upper():
                totalTerrenoManzana += vivienda.superficieTerreno
        return totalTerrenoManzana
    def getSuperficieTotalCubierta(self):
        totalCubiertaBarrio = 0
        for vivienda in self.viviendas:
            totalCubiertaBarrio += vivienda.getMetrosCuadradosCubiertos()
        return totalCubiertaBarrio
    