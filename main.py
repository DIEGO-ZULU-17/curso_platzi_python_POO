"""
# Proyecto Biblioteca

Proyecto de catálogo de libros
Este proyecto define una clase Libro para representar libros en un catálogo.
Cada libro tiene un título, autor, ISBN y disponibilidad.
Se crean dos instancias de libros y se almacenan en una lista que representa el catálogo.
Finalmente, se imprime el catálogo de libros.    
"""

class Libro:

    historial_prestamos = [] # Lista de clase para registrar los títulos de los libros prestados. Se utiliza para determinar la popularidad de un libro.
    
    def __init__(self, titulo, autor, isbn, disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} | ISBN: {self.isbn} | disponible: {self.disponible}" # Se debe usar return porque __str__ debe devolver una cadena de texto. Se usa f-string para formatear la salida.

    def prestar(self):
        if self.disponible:
            self.disponible = False
            Libro.historial_prestamos.append(self)
            return f"{self.titulo}: prestado exitosamente."

    def devolver(self):
        self.disponible = True
        return f"{self.titulo}: ha sido devuelto y está disponible nuevamente."
    
    def es_popular(self):
        """Retorna True si el libro ha sido prestado más de 5 veces."""
        if Libro.historial_prestamos.count(self) > 5:
            print(f"El libro {self.titulo} es popular, se prestó más de 5 veces")
            return True
        return False


mi_libro = Libro("100 años de soledad", "Gabriel García Márquez", "12345ASDF", True)
otro_libro = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0-15-601219-5", True)

print(mi_libro.prestar() + "\n")
print(mi_libro.devolver() + "\n")

print(otro_libro.prestar() + "\n")
print(otro_libro.devolver() + "\n")

print(mi_libro.es_popular())
print(otro_libro.es_popular())

catalogo = [
    mi_libro ,
    otro_libro
]

print("\n Catálogo de libros: \n")
for libro in catalogo:
    print("\n" + str(libro) + "\n")

# Prestar el mismo libro 6 veces para que sea popular
for i in range(6):
    resultado = mi_libro.prestar()
    if resultado:
        print(resultado)
    mi_libro.devolver()  # Devolverlo para poder prestarlo de nuevo

# Ahora verificar si es popular
print("\nVerificando popularidad:")
print(mi_libro.es_popular())