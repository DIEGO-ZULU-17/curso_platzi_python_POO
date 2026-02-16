"""
# Proyecto Biblioteca

Proyecto de catálogo de libros
Este proyecto define una clase Libro para representar libros en un catálogo.
Cada libro tiene un título, autor, ISBN y disponibilidad.
Se crean instancias de libros y se almacenan en una lista que representa el catálogo.
"""

from biblioteca import Biblioteca
from usuarios import Estudiante
from exceptions import UsuarioNoEncontrado
from datos_ejemplo import obtener_libros_ejemplo, obtener_usuarios_ejemplo

biblioteca = Biblioteca("Biblioteca Perfecta")

# Cargar usuarios y libros de ejemplo
biblioteca.usuarios = obtener_usuarios_ejemplo()
biblioteca.libros = obtener_libros_ejemplo()

# Imprimir el catálogo de libros disponibles
print("\n")
print("Bienvenido a Biblioteca Perfecta.")
print("\n")
print("Libros disponibles:")
for titulo in biblioteca.libros_disponibles():
    print(f"  - {titulo}")
print()

# Buscar un usuario por cédula
cedula = input("Digite el número de cédula: ")

try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(f"\nCédula: {usuario.cedula}, Nombre: {usuario.nombre}")
    
    # Permitir que el usuario solicite un libro
    print("\nLibros disponibles para prestar:")
    for libro in biblioteca.libros:
        if libro.disponible:
            print(f"  - {libro.titulo}")
    
    titulo_libro = input("\n¿Qué libro deseas pedir prestado? ")
    
    # Buscar el libro y hacer el préstamo
    for libro in biblioteca.libros:
        if libro.titulo.lower() == titulo_libro.lower() and libro.disponible:
            resultado = usuario.solicitar_libro(libro.titulo)
            print("\n") 
            print(resultado)
            print("\n") 
            print(libro.prestar())
            break
    else:
        print("\n")
        print(f"El libro '{titulo_libro}' no está disponible.")
        
except UsuarioNoEncontrado:
    print(f"El usuario con cédula {cedula} que estás buscando no existe.")