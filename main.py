from libro import Libro

def intentar_prestar(libro):
    try:
        libro.prestar()
        print(f"Préstamo realizado: {libro.titulo}")
    except ValueError as error:
        print(f"Préstamo rechazado: {error}")

def intentar_devolver(libro):
    try:
        libro.devolver()
        print(f"Devolución realizada: {libro.titulo}")
    except ValueError as error:
        print(f"Devolución rechazada: {error}")

def main():
    libros = [
        Libro("La colmena", "Camilo José Cela", 1951),
        Libro("Cien años de soledad", "Gabriel García Márquez", 1967),
        Libro("La casa de Bernarda Alba", "Federico García Lorca", 1936),
        Libro("Nada", "Carmen Laforet", 1945),
        Libro("La familia de Pascual Duarte", "Camilo José Cela", 1942)
    ]
    
    libro = libros[1]
    intentar_prestar(libro)
    intentar_prestar(libro)
    intentar_devolver(libro)
    intentar_devolver(libro)

    print("Total de libros creados:", Libro.total_libros)

    try:
        nuevo_libro = Libro("", "Miguel de Unamuno", 1914)
        libros.append(nuevo_libro)
    except ValueError as error:
        print(f"Error al crear el libro: {error}")

    reciente = Libro("Ejemplo reciente", "Autor de ejemplo", 2022)
    print("¿Es antiguo el libro reciente?:", reciente.es_antiguo)
    
    otro_libro = Libro("Nada", "Carmen Laforet", 1945)
    print("Comparación ==:", libros[3] == otro_libro)
    print("Comparación is:", libros[3] is otro_libro)
    
    print("\n--- Ordenados por año ---")
    libros_ordenados = sorted(libros, key=lambda libro: libro.anio)
    for libro in libros_ordenados:
        print(libro)

    print("\n--- Títulos disponibles ---")
    titulos_disponibles = map(
        lambda libro: libro.titulo,
        filter(lambda libro: libro.disponible, libros)
    )
    for titulo in titulos_disponibles:
        print(titulo)

if __name__ == "__main__":
    main()