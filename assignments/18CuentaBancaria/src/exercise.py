def main():
    # escribe tu código abajo de esta línea
    saldo = float(input("Dame el saldo del mas anterior: "))
    ingresos = float(input("Dame los ingreso: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    saldof = (saldo + ingresos - egresos- (cheques*13)) * 0.925
    print("El saldo final de la cuenta es:", saldof )


if __name__ == '__main__':
    main()
