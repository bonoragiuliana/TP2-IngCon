#Sistema de reservas con tuplas y diccionarios:
# Consigna: Un hotel maneja sus reservas utilizando un diccionario donde la clave es la fecha y el valor es 
# una lista de tuplas, cada tupla contiene el nombre del huésped, la habitación asignada y el precio. Escribe 
# una función que permita hacer una nueva reserva verificando primero si la habitación está disponible en la fecha seleccionada.

def hacer_reserva(reservas, fecha, huesped, habitacion, precio):
   
    if fecha not in reservas:
        reservas[fecha] = []  

    for reserva_existente in reservas[fecha]:
        if reserva_existente[1] == habitacion:
            print(f"Lo siento, la habitación {habitacion} ya está ocupada para la fecha {fecha}.")
            return False  


    reservas[fecha].append((huesped, habitacion, precio))
    print(f"¡Reserva exitosa! {huesped} ha reservado la habitación {habitacion} para el {fecha}.")
    return True


reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}


print("Intentando nueva reserva")
hacer_reserva(reservas, "2024-08-15", "Pedro", 101, 150)  
print("\n Intentando otra reserva")
hacer_reserva(reservas, "2024-08-17", "Marta", 103, 200)  
print("\n Estado actual de las reservas")
print(reservas)






