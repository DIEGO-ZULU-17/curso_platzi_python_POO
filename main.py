"""
# Proyecto Biblioteca

Proyecto de catálogo de libros
Este proyecto define una clase Libro para representar libros en un catálogo.
Cada libro tiene un título, autor, ISBN y disponibilidad.
Se crean dos instancias de libros y se almacenan en una lista que representa el catálogo.
Finalmente, se imprime el catálogo de libros.    
"""

class Libro:
    def __init__(self, titulo, autor, isbn, disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

mi_libro = Libro("100 años de soledad", "Gabriel García Márquez", "12345ASDF", True)
otro_libro = Libro("1984", "George Orwell", "098765ÑLKJH12345", True)

catalogo = [
    mi_libro ,
    otro_libro
]

print("Catálogo de libros: \n")
for libro in catalogo:
    print(libro.titulo, libro.autor, libro.isbn, libro.disponible)
