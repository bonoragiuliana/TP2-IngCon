# Optimización de rutas con arrays y tuplas:
# Consigna: Una empresa de logística necesita optimizar sus rutas de entrega. Cada ruta se representa como una tupla 
# (origen, destino, distancia). Escribe una función que reciba una lista de rutas y un array con las distancias máximas 
# permitidas para cada ruta. La función debe devolver las rutas que cumplen con las restricciones.


rutas = [
    ("Madrid", "Barcelona", 620),
    ("Madrid", "Valencia", 350),
    ("Barcelona", "Valencia", 350)
]
distancias_max = [600, 400, 500]

def filtrar_rutas(rutas, distancias_max):
    
    rutas_validas = []
    
    
    for ruta, max_dist in zip(rutas, distancias_max):
        origen, destino, distancia = ruta
        
        
        if distancia <= max_dist:
            rutas_validas.append(ruta)
    
    return rutas_validas



resultado = filtrar_rutas(rutas, distancias_max)
print("Rutas que cumplen con las restricciones:")
print(resultado)

