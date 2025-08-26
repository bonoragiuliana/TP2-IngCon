#Gestión de inventarios en múltiples tiendas con diccionarios y **kwargs:
# Consigna: Escribe una función que gestione el inventario de una cadena de tiendas. La función debe recibir el nombre de 
# la tienda, el producto y la cantidad a actualizar usando **kwargs. Debe manejar un diccionario donde la clave es el nombre 
# de la tienda y el valor es otro diccionario con los productos y sus cantidades. La función debe actualizar el inventario y 
# devolver el estado actual.


inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}


def actualizar_inventario(tienda, **kwargs):
    if tienda not in inventario:
        print(f"La tienda '{tienda}' no existe en el inventario.")
        return inventario
    
    
    for producto, cambio in kwargs.items():
        if producto in inventario[tienda]:
            inventario[tienda][producto] += cambio
        else:
            
            inventario[tienda][producto] = cambio
    
    return inventario


resultado = actualizar_inventario(tienda="Tienda A", producto_1=10, producto_2=-5)
print(resultado)

