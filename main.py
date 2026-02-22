"""
# Proyecto Biblioteca

Proyecto de catálogo de libros
Este proyecto define una clase Libro para representar libros en un catálogo.
Cada libro tiene un título, autor, ISBN y disponibilidad.
Se crean instancias de libros y se almacenan en una lista que representa el catálogo.

# Funciones:
- Buscar libros disponibles
- Prestar libros
- Devolver libros
- Verificar popularidad de libros
- Manejo de excepciones para libros no disponibles
- Clases para usuarios (estudiantes y profesores) con límites de préstamos
- Clase Biblioteca para gestionar libros y usuarios
- Excepciones personalizadas para errores comunes en la biblioteca
"""

from biblioteca import Biblioteca
from data import data_estudiantes, data_libros
from exceptions import LibroNoDisponibleError, UsuarioNoEncontradoError
from usuarios import Profesor
from libros import Libro
from usuarios import Estudiante

biblioteca = Biblioteca("Biblioteca Perfecta")
profesor = Profesor("Felipe", "123123123")

biblioteca.usuarios = [profesor] + data_estudiantes
biblioteca.libros = data_libros


""" # EJEMPLO DE SETTER CON VALIDACIÓN
libro_de_prueba = data_libros[0]
libro_de_prueba.veces_prestado = -1 # Si es negativo, se lanzará una excepción ValueError indicando que el número de veces prestado debe ser mayor que cero. Esto se debe a la lógica implementada en el setter de la propiedad veces_prestado, que verifica si el valor asignado es mayor que cero antes de actualizar el contador de veces prestado. Si se intenta asignar un valor negativo, se lanza la excepción para evitar que el contador tenga un valor no válido. """

libro_no_disp = Libro.crear_no_disponible(
    titulo="Libro de prueba",
    autor="Autor de prueba",
    isbn="1234567890",
)
print("Libro disponible:", libro_no_disp.disponible)  # False
# Esto funciona porque crear_no_disponible es un método de clase, lo que significa que se puede llamar directamente desde la clase Libro sin necesidad de crear una instancia de la clase. En este caso, se está llamando al método crear_no_disponible pasando el título, autor e ISBN del libro como argumentos para crear una nueva instancia de Libro que no esté disponible. El resultado de esta operación se almacena en la variable libro_no_disp. Luego, se imprime el estado de disponibilidad del libro utilizando el atributo disponible, que en este caso será False, indicando que el libro no está disponible para préstamo.


# EJEMPLO DE USO DE MÉTODOS DE CLASE Y ESTÁTICOS EN LA CLASE Estudiante
# Usando el método de clase crear_estudiante
estudiante1 = Estudiante.crear_estudiante("Juan Pérez", "12345678", "Ingeniería")
print(f"Estudiante creado: {estudiante1.nombre_completo}, Carrera: {estudiante1.carrera}")

# Usando el factory method específico
estudiante2 = Estudiante.estudiante_ingeneria("María García", "87654321")
print(f"Estudiante creado: {estudiante2.nombre_completo}, Carrera: {estudiante2.carrera}")

# Usando el método estático directamente
es_valida = Estudiante.validar_carrera("Medicina")
print(f"¿Medicina es válida? {es_valida}")  # True

# Intentando crear con carrera inválida (lanza ValueError)
try:
    estudiante3 = Estudiante.crear_estudiante("Pedro", "11111111", "Filosofía")
except ValueError as e:
    print(f"Error: {e}")



print("\n Bienvenido a Platzi Biblioteca")

print("Libros disponibles:")
for libro in biblioteca.libros_disponibles:
    print(f"  - {libro.descripcion_completa}, Veces prestado: {libro.veces_prestado}") # veces_prestado funciona como un atributo de solo lectura aunque es un método, lo que significa que se puede acceder a su valor pero no se puede modificar directamente. Esto es útil para mantener la integridad de los datos y evitar cambios no deseados en el número de veces que un libro ha sido prestado.
    # No es necesario agregar los parentesis al acceder a veces_prestado porque se ha definido como una propiedad utilizando el decorador @property en la clase Libro. Esto permite acceder a veces_prestado como si fuera un atributo, sin necesidad de llamarlo como una función. Por lo tanto, se puede usar libro.veces_prestado en lugar de libro.veces_prestado() para obtener el valor del número de veces que el libro ha sido prestado.
print()

# Solicitar un libro

cedula = input("Digite el numero cedula: ")
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(usuario.nombre_completo)
except UsuarioNoEncontradoError as e:
    print(e)

# Solicitar un libro por título

titulo = input("Digite el titulo del libro: ")
try:
    libro = biblioteca.buscar_libro(titulo) # biblioteca.buscar_libro(titulo) significa que se está llamando al método buscar_libro de la clase Biblioteca, pasando el título del libro como argumento. Este método busca en la lista de libros disponibles en la biblioteca y devuelve el libro que coincide con el título proporcionado. Si el libro no está disponible o no existe, se lanza una excepción LibroNoDisponibleError. 
    print(f"El libro que selecionaste es: {libro}")
except LibroNoDisponibleError as e:
    print(e)

resultado = usuario.solicitar_libro(libro.titulo) # usuario.solicitar_libro(libro.titulo) significa que se está llamando al método solicitar_libro del objeto usuario, pasando el título del libro como argumento. Este método verifica si el usuario puede solicitar el libro (por ejemplo, si no ha alcanzado su límite de préstamos) y devuelve un mensaje indicando si el préstamo fue autorizado o no. El resultado de esta operación se almacena en la variable resultado.
print(f"\n{resultado}")

# Intentar prestar el mismo libro nuevamente para ver la excepción personalizada

try:
    resultado_prestar = libro.prestar() # libro.prestar() significa que se está llamando al método prestar del objeto libro, del archivo libros.py. Este método verifica si el libro está disponible para préstamo. Si el libro no está disponible, se lanza una excepción LibroNoDisponibleError. Si el libro está disponible, se marca como no disponible y se incrementa el contador de veces prestado, devolviendo un mensaje de éxito.
    print(f"\n{resultado_prestar}")
except LibroNoDisponibleError as e:
    print(e) # e significa que se está capturando la excepción LibroNoDisponibleError y se imprime el mensaje de error asociado a esa excepción. Esto permite manejar el caso en el que el libro no está disponible para préstamo de manera controlada, mostrando un mensaje informativo al usuario en lugar de que el programa falle abruptamente.

""" resultado = Biblioteca.validar_isbn("12345") 
print("El ISBN es válido:", resultado)  # False
# Esto funciona porque validar_isbn es un método estático, lo que significa que se puede llamar directamente desde la clase Biblioteca sin necesidad de crear una instancia de la clase. En este caso, se está llamando al método validar_isbn pasando el string "12345" como argumento para verificar si es un ISBN válido. El resultado de esta validación se almacena en la variable resultado. Luego, se imprime el resultado indicando si el ISBN es válido o no. En este caso, dado que "12345" tiene menos de 10 caracteres, el resultado será False, indicando que el ISBN no es válido.

resultado = Biblioteca.validar_isbn("1234567890")
print("El ISBN es válido:", resultado)  # True """

