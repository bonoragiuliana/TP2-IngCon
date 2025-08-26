#Análisis de datos meteorológicos con arrays:
# Consigna: Un meteorólogo registra las temperaturas diarias durante un mes y las almacena en un array. Escribe una función
#  que reciba este array y devuelva la temperatura media del mes, la máxima y la mínima.
# temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def datos_meteorologicos(temp):
    promedio = sum(temp) / len(temp)
    maxima = max(temp)
    minima = min(temp)

    return promedio, maxima, minima

prom, temp_max, temp_min = datos_meteorologicos(temperaturas)


print("Temperatura media:", prom)
print("Temperatura máxima:", temp_max)
print("Temperatura mínima:", temp_min)