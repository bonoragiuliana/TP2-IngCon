#Administración de empleados con tuplas y diccionarios:
# Consigna: Una empresa quiere administrar la información de sus empleados, donde cada empleado se representa como 
# una tupla (nombre, edad, salario). Escribe una función que reciba un diccionario donde la clave es el ID del empleado y el valor 
# es la tupla con su información. La función debe devolver un diccionario con los empleados que ganan más de un salario dado.

#empleados = {
#    1: ("Ana", 30, 3000),
#    2: ("Luis", 25, 2500),
#    3: ("María", 35, 4000)
#}

def filtrar_empleados(empleados, salario_minimo):
    
    empleados_filtrados = {}

    
    for id_empleado, datos in empleados.items():
        nombre, edad, salario = datos  

        if salario > salario_minimo:
            empleados_filtrados[id_empleado] = datos  

    return empleados_filtrados

empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

resultado = filtrar_empleados(empleados, 3000)
print(resultado)
