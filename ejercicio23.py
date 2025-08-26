#Gestión de inventario con arrays:
# Consigna: Una tienda maneja su inventario de productos en un array donde cada índice representa un producto específico y 
# su valor es la cantidad disponible. Escribe una función que reciba el array de inventario y un número de productos vendidos 
# (otro array) y devuelva el inventario actualizado.

def actualizar_inventario(inventario, ventas):
 
    inventario_actualizado = []

    for i in range(len(inventario)):
        stock_actual = inventario[i]
        vendidos = ventas[i]
        nuevo_stock = stock_actual - vendidos
        inventario_actualizado.append(nuevo_stock)

    return inventario_actualizado



inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]
print(actualizar_inventario(inventario, ventas))  
