class Libro:
    total_libros = 0

    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True
        Libro.total_libros += 1

    def prestar(self):
        if not self.disponible:
            raise ValueError("El libro ya está prestado")
        self.disponible = False

    def devolver(self):
        if self.disponible:
            raise ValueError("El libro ya está disponible")
        self.disponible = True