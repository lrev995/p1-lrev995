from libro import Libro

def main():
    libros = [
        Libro("La colmena", "Camilo José Cela", 1951),
        Libro("Cien años de soledad", "Gabriel García Márquez", 1967),
        Libro("La casa de Bernarda Alba", "Federico García Lorca", 1936),
        Libro("Nada", "Carmen Laforet", 1945),
        Libro("La familia de Pascual Duarte", "Camilo José Cela", 1942)
    ]
    for libro in libros:
        print(libro.titulo, libro.autor, libro.anio)

if __name__ == "__main__":
    main()