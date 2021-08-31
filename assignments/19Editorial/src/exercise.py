def main():
    # escribe tu código abajo de esta línea
    # importamos la librería math ya que la necesitaremos
    import math
    # Pedimos las variables de entrada
    palabras = int( input( "Dame el número de palabras: "))
    # Redondeamos el número de páginas al número mayor más cercano
    paginas = math.ceil(palabras / 475)
    # Calculamos el costo
    costo = paginas * 60 * 0.9
    # Le decimos el costo de publicación al usuario
    print( "El costo de la publicación es:", costo)


if __name__ == '__main__':
    main()
