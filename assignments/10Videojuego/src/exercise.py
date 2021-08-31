def main():
    # escribe tu código abajo de esta línea
    #Preguntamos el tipo de juegos que compro
    nuevos = int(input("Dame la cantidad de juegos nuevos: "))
    usados = int(input("Dame la cantidad de juegos usados: "))
    #Calculamos cuanto es el total de su compra
    costo = (1000*nuevos) + (350*usados)
    #Le decimos al usuario su compra
    print("El total de la compra es", costo)


if __name__ == '__main__':
    main()
