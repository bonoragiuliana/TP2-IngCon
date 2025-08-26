#Organización de eventos con *args:
# Consigna: Escribe una función que reciba un número variable de nombres de eventos y los imprima en un formato 
# de lista numerada. Utiliza *args para recibir los nombres de los eventos.


def organizar_eventos(*args):
    contador = 1
    for evento in args:
        print(f"{contador}. {evento}")
        contador += 1

organizar_eventos("Concierto", "Exposición de arte", "Conferencia")
