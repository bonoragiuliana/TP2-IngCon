#Una tienda quiere procesar sus ventas diarias almacenadas en un array. Escribe una función que reciba el array de ventas 
# diarias y devuelva el total de ventas y el promedio de ventas por día.
# ventas_diarias = [200, 450, 300, 400, 350, 500, 600]


def procesamientoVentas(ventas):
    total= sum(ventas)
    promedio= total/len(ventas)
    return total, promedio

ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

print("El total de ventas es de:", procesamientoVentas(ventas_diarias)[0], "y el promedio de ventas por día es de:", procesamientoVentas(ventas_diarias)[1])