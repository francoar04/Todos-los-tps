from Notas import Nota
class Alumno:
    def __init__(self, nombreCompleto: str, legajo: int):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []
    def calcularPromedio(self):
        if len(self.notas) == 0:
            return 0.0
        suma = sum(nota.notaExamen for nota in self.notas)
        return suma / len(self.notas)