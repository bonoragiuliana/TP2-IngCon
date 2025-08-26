#Configuración de perfiles de usuario con **kwargs y arrays: 
# Consigna: Escribe una función que reciba una lista de usuarios y sus preferencias de configuración como **kwargs.
#  La función debe devolver un diccionario donde la clave es el nombre del usuario y el valor es un array con las configuraciones 
# aplicadas.


usuarios = ["Ana", "Luis", "María"]

def configurar_perfiles(usuarios, **kwargs):
    perfiles = {}
    for usuario in usuarios:
        perfiles[usuario] = list(kwargs.values())
    return perfiles

resultados = configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)

print("Perfiles configurados:", resultados)
