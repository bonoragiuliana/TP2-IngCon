#Ordenamiento de datos con tuplas:
# Consigna: Escribe una función que reciba una lista de tuplas donde cada tupla contiene un nombre y una puntuación.
#  La función debe devolver la lista ordenada por puntuación de mayor a menor.
# puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]


puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

def ordenarPuntuaciones(lista):
    return sorted(lista, key=lambda x: x[1], reverse=True)

ordenada = ordenarPuntuaciones(puntuaciones)
print(ordenada)  

