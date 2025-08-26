#Registro de estudiantes con diccionarios:
# Consigna: Una escuela lleva un registro de estudiantes donde la clave es el número de matrícula y el valor es un diccionario 
# con nombre, edad y calificaciones en distintas materias. Escribe una función que reciba el registro de estudiantes y devuelva el 
# promedio de calificaciones de un estudiante dado su número de matrícula.
# estudiantes = {
    #101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    #102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
#}

estudiantes = {
    101: {"nombre": "Ana",  "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

def promedio_estudiante(registro, matricula):

    if matricula in registro:
        
        estudiante = registro[matricula]

        calificaciones_dict = estudiante["calificaciones"]
        notas = list(calificaciones_dict.values())  

        if len(notas) == 0:
            return None  
        promedio = sum(notas) / len(notas)

        return promedio
    else:
        return None  
    
p1 = promedio_estudiante(estudiantes, 101)
print("Promedio matrícula 101:", p1)  

p2 = promedio_estudiante(estudiantes, 102)
print("Promedio matrícula 102:", p2)  


