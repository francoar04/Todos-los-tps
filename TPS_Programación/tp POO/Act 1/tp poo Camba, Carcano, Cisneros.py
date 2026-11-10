#Act N1 Codificar Clases
class celda:
    def __init__(self, fila:int,columna:int,valor:str):
        self.fila=fila
        self.columna=columna
        self.valor=valor
class Matriz:
    def __init__(self):
        self.celdasMatriz=[]
    def obtenerValor(self, fila, columna):
        for c in self.celdasMatriz:
            if c.fila == fila and c.columna == columna:
                return c.valor
        return "La fila y la columna indicada no ha sido asignada en ninguna celda"
matriz = Matriz()
valor= input("Ingrese el valor (o escriba FIN para terminar): ").upper()
while valor.strip()=="":
    print("Error, el valor no puede estar vacío.")
    valor=input("ingrese solamente números (O escriba FIN para terminar): ").upper()

while valor != "FIN":
    fila = int(input("Ingrese la fila: "))
    columna= int(input("Ingrese la columna: "))
    existe= False
    for c in matriz.celdasMatriz:
        if c.fila==fila and c.columna==columna:
            existe= True
            break
    if existe:
        print("Error, Esa fila y columna ya fueron cargadas.")
    else:
        nueva = celda(fila, columna, valor)
        matriz.celdasMatriz.append(nueva)
        print(f"Celda guardada con éxito, El valor ingresado es: {valor}.  ")
    valor= input("\nIngrese el valor (o escriba FIN para terminar): ").upper()
    while valor.strip()=="":
         print("Error, el valor no puede estar vacío.")
         valor=input("ingrese solamente números (O escriba FIN para terminar): ").upper()
print("\n===Valores cargados en la lista===")
for c in matriz.celdasMatriz:
    print(f"Fila: {c.fila} | Columna: {c.columna} | Valor: {c.valor}")
