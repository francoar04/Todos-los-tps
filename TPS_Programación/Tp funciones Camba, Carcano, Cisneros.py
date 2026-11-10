#Actividad N1
def calcular_factura_final(monto_base: float, impuesto: float = 21.0, descuento: float = 0.0, envio_prioritario: float | None = None) -> float:
    subtotal= monto_base*(1-descuento/100)
    total= subtotal*(1+impuesto/100)
    if envio_prioritario is not None:
        total+=envio_prioritario
    return round(total, 2)
prueba_1=calcular_factura_final(1000.0)
prueba_2=calcular_factura_final(1000.0, descuento=10.0)
prueba_3 = calcular_factura_final(1000.0, impuesto=10.0, descuento=5.0, envio_prioritario=150.0)
print(f"Prueba 1: {prueba_1}")
print(f"Prueba 2: {prueba_2} ")
print(f"Prueba 3: {prueba_3}")

#Actividad N2
print("="*100)
class validadorfinanciero:
    @staticmethod
    def es_cuit_valido(cuit: str) -> bool:
        return len(cuit) == 11 and cuit.isdigit()
    @staticmethod
    def convertir_moneda(monto: float, tasa_cambio: float, comision: float = 0.02) -> float:
        numero_convertido= monto*tasa_cambio
        montofinal= numero_convertido*(1-comision)
        return montofinal
print(validadorfinanciero.es_cuit_valido("20384920194")) 
print(validadorfinanciero.es_cuit_valido("20-38492019-4"))
print(validadorfinanciero.convertir_moneda(100.0, 1000.0, comision=0.05))

#Avtividad N3
print("="*100)
class notificador:
    def enviar_recibo(self, cliente:str,total:float)->None:
        print("====================")
        print("COMPROBANTE DE PAGO")
        print("====================")
        print(f"Cliente: {cliente}")
        print(f"Total: ${total:.2f}")
        print("====================")
class procesador_pagos:
    def __init__(self):
        self.notificador = notificador()
    def procesar_transaccion(self, cliente: str, items: list[dict], descuento_cupon: float = 0.0) -> float:
        total= 0.0
        for item in items:
            total += item["precio"]
        total -= descuento_cupon
        self.notificador.enviar_recibo(cliente, total)
        return total
carrito = [{"nombre": "Teclado", "precio": 50.0}, {"nombre": "Mouse", "precio": 30.0}]
procesador = procesador_pagos()
total_final = procesador.procesar_transaccion("Ana Gómez", carrito, descuento_cupon=10.0)
print(f"El método retornó el valor numérico: {total_final}")

#Actividad N4
print("="*100)
def generar_auditoria_sistema(modulo: str, *mensajes: str, **metadatos) -> str:
    reporte = f"--- AUDITORÍA MÓDULO: {modulo.upper()} ---\n"
    reporte += "Eventos Registrados:\n"
    for i, mensaje in enumerate(mensajes, 1):
        reporte += f"  [{i}] {mensaje}\n"
    if metadatos:
        reporte += "Contexto Adicional:\n"
        for clave, valor in metadatos.items():
            reporte += f"  {clave.upper()}: {valor}\n"
    return reporte.strip()
log = generar_auditoria_sistema("AUTH", "Intento fallido", "Bloqueo de IP", usuario="admin", ip="192.168.1.10")
print(log)

#Actividad N5
print("="*100)
class CalculadoraFitness:
    @staticmethod
    def calcular_imc(peso_kg: float, altura_m: float) -> float:
        imc = peso_kg / (altura_m ** 2)
        return round(imc, 2)
    @staticmethod
    def clasificar_nivel(imc: float) -> str:
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25.0:
            return "Normal"
        else:
            return "Sobrepeso"
class Atleta:
    def __init__(self, nombre: str, peso: float, altura: float):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
    def obtener_reporte(self, incluir_recomendacion: bool = False, **metricas_extra) -> str:
        imc_actual = CalculadoraFitness.calcular_imc(self.peso, self.altura)
        estado = CalculadoraFitness.clasificar_nivel(imc_actual)

        reporte = f"=== REPORTE FÍSICO: {self.nombre.upper()} ===\n"
        reporte += f"IMC: {imc_actual} -> Clasificación: {estado}\n"

        if metricas_extra:
            reporte += "\nMétricas Adicionales:\n"
            for clave, valor in metricas_extra.items():
                clave_limpia = clave.replace("_", " ").capitalize()
                reporte += f" - {clave_limpia}: {valor}\n"
        if incluir_recomendacion:
            reporte += "\nRecomendación:\n"
            if estado == "Bajo peso":
                reporte += " Priorizar superávit calórico y entrenamiento de fuerza."
            elif estado == "Normal":
                reporte += " Mantener hábitos de mantenimiento. ¡Buen trabajo!"
            else:
                reporte += " Evaluar déficit calórico ligero y aumentar actividad cardiovascular."
        return reporte.strip()

atleta_1 = Atleta("Marcos Silva", peso=82.5, altura=1.78)
reporte_final = atleta_1.obtener_reporte(incluir_recomendacion=True,grasa_corporal="15%",frecuencia_cardiaca_reposo="55 bpm",horas_sueno_promedio=7.5)
print(reporte_final)