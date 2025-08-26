#Estadísticas de ventas con arrays:
# Consigna: Escribe una función que reciba un array con las ventas de cada mes y devuelva un diccionario con el total de ventas, 
# el promedio mensual, y el mes con mayores ventas.

ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

def esatdisticasDeVentas (ventas):
    total = sum(ventas)
    promedio = total / len(ventas)
    mes_maximo = ventas.index(max(ventas)) + 1  
    estadisticas  = {"total": total, "promedio": promedio, "mes_maximo": mes_maximo}
    return estadisticas

print (esatdisticasDeVentas(ventas_mensuales))