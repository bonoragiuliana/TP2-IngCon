#Simulación de mercado bursátil con arrays y tuplas:
# Consigna: Escribe una función que simule el comportamiento de acciones en un mercado bursátil. La función 
# debe recibir un array con los precios diarios de una acción y una lista de tuplas donde cada tupla contiene un día y 
# un precio de compra o venta. La función debe devolver el beneficio o pérdida total si las acciones se hubieran comprado 
# y vendido en los días especificados.

precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

def simular_mercado(precios_diarios, operaciones):
    beneficio_total = 0
    acciones = 0
    precio_compra = 0

    for operacion, dia in operaciones:
        precio_dia = precios_diarios[dia]  
        
        if operacion == "compra":
            acciones += 1
            precio_compra = precio_dia
            print(f"Compré 1 acción a {precio_compra} el día {dia}")
        
        elif operacion == "venta":
            if acciones > 0:
                beneficio = precio_dia - precio_compra
                beneficio_total += beneficio
                acciones -= 1
                print(f"Vendí 1 acción a {precio_dia} el día {dia}, beneficio: {beneficio}")
            else:
                print(f"No hay acciones para vender el día {dia}")
    
    return beneficio_total


resultado = simular_mercado(precios_diarios, operaciones)
print(f"\nBeneficio total: {resultado}")

