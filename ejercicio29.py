#Registro de notas con tuplas y arrays:
# Consigna: Escribe una función que reciba una lista de tuplas donde cada tupla contiene el nombre de un estudiante y 
# sus calificaciones en un array. La función debe devolver un diccionario con el nombre del estudiante como clave y su 
# promedio de calificaciones como valor.

notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

def promedios(notas):
    promedios = {}
    for nombre, calificaciones in notas:
        
        promedio = sum(calificaciones) / len(calificaciones)
        promedios[nombre] = promedio
    return promedios
        
    
resultadosPromedios = promedios(notas_estudiantes)

print ("los promedios de los estudiantes son:", resultadosPromedios )





































