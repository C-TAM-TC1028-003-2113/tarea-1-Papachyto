def main():
    # escribe tu código abajo de esta línea
    #Pedimos las variables
    x1 = float(input("Dame x1: "))
    y1 = float(input("Dame y1: "))
    x2 = float(input("Dame x2: "))
    y2 = float(input("Dame y2: "))
    #Calculamos la pendiente
    m = (y2 - y1) / (x2 - x1)
    #Le decimos la pendiente al usuario
    print("Pendiente:", m)

if __name__ == '__main__':
    main()
