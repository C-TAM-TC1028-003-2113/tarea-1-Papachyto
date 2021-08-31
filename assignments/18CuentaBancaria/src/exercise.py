def main():
    # escribe tu código abajo de esta línea
    #Le pedimos al usuario las variables a tomar en cuenta
    saldo = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingreso: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    #Calculamos el saldo final de la cuenta
    saldof = (saldo + ingresos - egresos- (cheques*13)) * 0.925
    #Le decimos el saldo final al usuario
    print("El saldo final de la cuenta es:", saldof )


if __name__ == '__main__':
    main()
