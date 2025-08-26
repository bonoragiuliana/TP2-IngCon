#Manejo de parámetros variables con *args:
# Consigna: Escribe una función que reciba un número variable de notas de estudiantes y devuelva la nota
#  promedio. Utiliza *args para recibir las notas.
# calcular_promedio(85, 90, 78, 92)


def nota(*args):
    
    promedio = sum(args) / len(args)
    return promedio

print("el promedio es de:", nota(85, 90, 78, 92))