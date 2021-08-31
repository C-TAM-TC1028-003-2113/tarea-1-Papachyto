def main():
    # escribe tu código abajo de esta línea
    #Pedimos las variables de entrada
    mensajes = int(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    minutos = int(input("Dame el número de minutos: "))
    #Calculamos el costo
    costo = (mensajes+megas+minutos)*0.8
    #Le decimos el costo al usuario
    print("El costo mensual es:", costo)


if __name__ == '__main__':
    main()
