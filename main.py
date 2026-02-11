"""
# Proyecto Biblioteca

Proyecto de catálogo de libros
Este proyecto define una clase Libro para representar libros en un catálogo.
Cada libro tiene un título, autor, ISBN y disponibilidad.
Se crean dos instancias de libros y se almacenan en una lista que representa el catálogo.
Finalmente, se imprime el catálogo de libros.    
"""

from encodings.punycode import T


class Libro:

    historial_prestamos = [] # Lista de clase para registrar los títulos de los libros prestados. Se utiliza para determinar la popularidad de un libro.
    
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.__veces_prestado = 0 # Contador de veces que el libro ha sido prestado, se incrementa cada vez que se presta el libro.
        # El _ indica que es un atributo privado, pero en Python no es estrictamente privado.
        # El __ indica que es un atributo con name mangling, lo que hace que sea más difícil acceder a él desde fuera de la clase, pero aún así es posible.
        # La pregunta para definir variables privadas es ¿Esta variable interna debería ser modificada directamente por un usuario exterior? Si la respuesta es no, entonces se puede usar un atributo privado con name mangling para indicar que no debería ser modificado directamente desde fuera de la clase.  

    def __str__(self):
        return f"{self.titulo} - {self.autor} | ISBN: {self.isbn} | disponible: {self.disponible}" # Se debe usar return porque __str__ debe devolver una cadena de texto. Se usa f-string para formatear la salida.

    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.__veces_prestado += 1
            return f"{self.titulo} prestado exitosamente. Total de veces prestado: {self.__veces_prestado}"
        return f"{self.titulo} no está disponible para préstamo."

    def devolver(self):
        self.disponible = True
        return f"{self.titulo}: ha sido devuelto y está disponible nuevamente."
    
    def es_popular(self):
        """Retorna True si el libro ha sido prestado más de 5 veces."""
        return self.__veces_prestado > 5
    
    def get_veces_prestado(self):
        return self.__veces_prestado # Método getter para acceder al contador de veces prestado desde fuera de la clase, ya que el atributo es privado con name mangling.
    
    def set_veces_prestado(self, veces_prestado):
        self.__veces_prestado = veces_prestado # Método setter para modificar el contador de veces prestado desde fuera de la clase, ya que el atributo es privado con name mangling. En este método se podría agregar validación para asegurarse de que el valor sea un número entero no negativo.


mi_libro = Libro("100 años de soledad", "Gabriel García Márquez", "12345ASDF", True)
otro_libro = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0-15-601219-5", True)

#print(mi_libro.__veces_prestado) # Esto generará un error porque __veces_prestado es un atributo con name mangling, lo que hace que sea más difícil acceder a él desde fuera de la clase. Sin embargo, aún es posible acceder a él usando el nombre mangled: mi_libro._Libro__veces_prestado

mi_libro.set_veces_prestado(10) # Esto establecerá el contador de veces prestado a 10, lo que hará que el libro sea considerado popular según el método es_popular.
print(mi_libro.get_veces_prestado()) # Esto imprimirá 0, ya que el libro no ha sido prestado aún. Tiene que usar el método getter para acceder al contador de veces prestado desde fuera de la clase, ya que el atributo es privado con name mangling.
print(f"¿El libro '{mi_libro.titulo}' es popular? {mi_libro.es_popular()} \n") # Esto imprimirá True, ya que el contador de veces prestado se ha establecido en 10, lo que hace que el libro sea considerado popular según el método es_popular.

print(mi_libro.prestar() + "\n")
print(mi_libro.prestar() + "\n")
print(mi_libro.devolver() + "\n")

print(otro_libro.prestar() + "\n")
print(otro_libro.devolver() + "\n")



catalogo = [
    mi_libro ,
    otro_libro
]

print("\n Catálogo de libros: \n")
for libro in catalogo:
    print("\n" + str(libro) + "\n")

