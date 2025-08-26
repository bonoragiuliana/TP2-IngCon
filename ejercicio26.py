#Registro de empleados con tuplas y **kwargs:
# Consigna: Escribe una función que reciba el nombre, edad, y salario de un empleado como parámetros obligatorios, 
# y otros datos como dirección, número de teléfono, etc., como **kwargs. La función debe devolver un diccionario con toda la 
# información del empleado.
# registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789")


def registro_empleado(nombre, edad, salario, **kwargs):
    return {
        "nombre": nombre,
        "edad": edad,
        "salario": salario,
        **kwargs
    }

print(registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789", id=1111))