#Administración de suscripciones con diccionarios, arrays, y **kwargs:
# Consigna: Escribe una función que gestione las suscripciones a un servicio en línea. La función debe recibir el 
# nombre del usuario, el tipo de suscripción (mensual, anual), y cualquier o	tra opción adicional usando **kwargs. La función 
# debe actualizar un diccionario que almacene el historial de suscripciones de los usuarios y devolver el estado actualizado.


suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

def actualizar_suscripcion(usuario, suscripcion, **kwargs):

    if usuario not in suscripciones:
        suscripciones[usuario] = []
    

    suscripciones[usuario].append(suscripcion)
    

    if kwargs:
        print(f"Opciones adicionales para {usuario}: {kwargs}")
    
    return suscripciones


resultado = actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True)
print("\nEstado actualizado de suscripciones:")
print(resultado)

