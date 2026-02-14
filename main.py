"""
# Proyecto Biblioteca

Proyecto de catálogo de libros
Este proyecto define una clase Libro para representar libros en un catálogo.
Cada libro tiene un título, autor, ISBN y disponibilidad.
Se crean dos instancias de libros y se almacenan en una lista que representa el catálogo.
Finalmente, se imprime el catálogo de libros.    
"""

from biblioteca import Biblioteca
from libros import LibroFisico
from usuarios import Estudiante, Profesor, SolicitanteProtocol

biblioteca = Biblioteca("Platzi Biblioteca")

estudiante = Estudiante("Luis", "1123123123", "Sistemas")
estudiante_1 = Estudiante("Jose", "56789", "Salud")
profesor = Profesor("Felipe", "123123123")
usuarios: list[SolicitanteProtocol] = [estudiante, estudiante_1, profesor]


mi_libro = LibroFisico(
    "100 Años de Soledad",
    "Gabriel Garcia Marquez",
    "9781644734728",
    True,
)
mi_libro_no_disponible = LibroFisico(
    "No disponible",
    "Luis",
    "56789",
    True,
)
otro_libro = LibroFisico(
    "El Principito",
    "Saint-Exupéry",
    "9781644731234728",
    True,
)


biblioteca.libros = [mi_libro, mi_libro_no_disponible, otro_libro]


print(biblioteca.libros)
