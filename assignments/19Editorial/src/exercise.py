def main():
    # escribe tu código abajo de esta línea
    import math
    palabras = int( input( "Dame el número de palabras: "))
    paginas = math.ceil(palabras / 475)
    costo = paginas * 60 * 0.9
    print( "El costo de la publicación es:", costo)


if __name__ == '__main__':
    main()
