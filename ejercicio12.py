#Gestión de inventario con tuplas:
# Consigna: Una tienda tiene un inventario de productos, cada producto tiene un nombre, precio y cantidad disponible. 
# Representa cada producto como una tupla (nombre, precio, cantidad). Escribe una función que reciba una lista de productos (tuplas) y 
# devuelva el producto más caro.
# productos = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]

lista_productos = [("funda", 7000, 10), ("templado", 3000, 5), ("cargador", 14000, 20)]

def productoMasCaro(inventario):
    producto_caro = max(inventario, key=lambda x: x[1])
    return producto_caro

resultado = productoMasCaro(lista_productos)

print("El producto más caro es:", resultado[0], "con un precio de:", resultado[1], "y una cantidad disponible de:", resultado[2])