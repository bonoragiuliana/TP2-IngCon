#Análisis de rendimiento académico con diccionarios y arrays:
# Consigna: Una universidad lleva un registro de las calificaciones de los estudiantes en diferentes materias. 
# Cada estudiante tiene un ID único y su información se almacena en un diccionario donde la clave es el ID y el valor 
# es otro diccionario con las materias y sus respectivas calificaciones (arrays). Escribe una función que reciba este diccionario 
# y devuelva un ranking de estudiantes basado en su promedio general.


estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

def ranking_estudiantes(estudiantes):
    
    promedios = {}

    for id_estudiante, materias in estudiantes.items():
        total = 0
        cantidad = 0
        
        for calificaciones in materias.values():
            total += sum(calificaciones)      
            cantidad += len(calificaciones)   
        promedio = total / cantidad
        promedios[id_estudiante] = promedio

    
    ranking = dict(sorted(promedios.items(), key=lambda item: item[1], reverse=True))
    
    return ranking


resultado = ranking_estudiantes(estudiantes)
print("Ranking de estudiantes por promedio general:")
print(resultado)
