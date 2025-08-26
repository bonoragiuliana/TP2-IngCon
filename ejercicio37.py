#Análisis de tendencias en redes sociales con arrays y tuplas:
# Consigna: Una empresa de marketing digital desea analizar las tendencias de hashtags en las redes sociales. 
# Escribe una función que reciba un array de hashtags y una lista de tuplas donde cada tupla contiene un hashtag 
# y su frecuencia de uso. La función debe devolver los hashtags que han sido mencionados más de una cierta cantidad de veces.


def analizar_tendencias(hashtags, tendencias, umbral):

    populares = []


    for hashtag, frecuencia in tendencias:
        if frecuencia > umbral:  
            populares.append(hashtag)

    return populares


hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

resultado = analizar_tendencias(hashtags, tendencias, umbral=100)
print("Hashtags populares:", resultado)

