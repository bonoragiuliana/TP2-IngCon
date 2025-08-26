#Análisis de resultados deportivos con diccionarios:
# Consigna: Un club deportivo registra los resultados de sus partidos en un diccionario donde la clave es el nombre del equipo 
# rival y el valor es una tupla con los goles anotados y recibidos. Escribe una función que calcule el total de goles anotados y 
# recibidos en la temporada.
#resultados = {
#    "Equipo A": (3, 2),
#    "Equipo B": (1, 1),
#    "Equipo C": (4, 0)
#}

def resultadosPartidos(result):
    anotados =0
    recibidos = 0
    for equipo, goles in result.items():
        anotados += goles[0]
        recibidos += goles[1]
    return (anotados, recibidos)    


resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

print("Cantidad de goles anotados:", resultadosPartidos(resultados)[0], ". Y cantidad de goles recibidos:", resultadosPartidos(resultados)[1])
