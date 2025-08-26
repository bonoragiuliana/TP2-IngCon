#Planificación de viajes con tuplas y diccionarios:
# Consigna: Una agencia de viajes tiene diferentes paquetes turísticos, cada uno representado como una tupla 
# (destino, precio, duración en días). Escribe una función que reciba una lista de estos paquetes y devuelva un 
# diccionario con los destinos como claves y el precio total (precio por día * duración) como valor.

def calcularCostos(paquete):
    costos = {}
    for destino, precio, dias in paquetes:
        total = precio * dias
        costos[destino] = total

    return costos 
    
paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

print(calcularCostos(paquetes))




