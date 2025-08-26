#Simulación de ventas con tuplas, arrays, y *args:
# Consigna: Una empresa quiere simular las ventas de diferentes productos. Escribe una función que reciba un número variable 
# de ventas (tuplas) donde cada tupla contiene el producto, la cantidad vendida, y el precio por unidad. La función debe devolver 
# el total de ingresos generados por las ventas.



def simular_ventas(*ventas):
    total=0
    for venta in ventas:
        producto, cantidad, precio = venta
        total += cantidad * precio
    return total
       

empresa = simular_ventas(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0))
print("Total de ingresos generados por las ventas", empresa)
