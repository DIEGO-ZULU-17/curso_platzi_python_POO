"""
# Proyecto Biblioteca

Proyecto de catálogo de libros
Este proyecto define una clase Libro para representar libros en un catálogo.
Cada libro tiene un título, autor, ISBN y disponibilidad.
Se crean dos instancias de libros y se almacenan en una lista que representa el catálogo.
Finalmente, se imprime el catálogo de libros.    
"""

from typing import Protocol # Protocol ayuda en que el código sea más flexible y menos acoplado
from datetime import datetime

# Definición del Protocolo
class LibroProtocol(Protocol):
    def prestar(self) -> str: 
        """Método para prestar el libro. Devuelve un mensaje indicando si el préstamo fue exitoso o si el libro no está disponible."""
        ... # "-> str" significa que el método prestar devuelve una cadena de texto (str). El uso de "..." indica que el cuerpo del método no está implementado en esta definición de protocolo, lo que es común en los protocolos para indicar que las clases que implementen este protocolo deben proporcionar su propia implementación de este método. 
    
    def devolver(self) -> str: ...
    
    def calcular_duracion(self) -> str: ...

# Implementación de la clase Libro que cumple con el protocolo LibroProtocol
class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.veces_prestado = 0

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.titulo} — {self.autor} (ISBN: {self.isbn}) — {estado}"

    def prestar(self):
        if not self.disponible:
            return f"El libro '{self.titulo}' no está disponible."
        self.disponible = False
        self.veces_prestado += 1
        return f"Prestado: {self.titulo}"

    def devolver(self):
        if self.disponible:
            return f"El libro '{self.titulo}' ya está en la biblioteca."
        self.disponible = True
        return f"Devuelto: {self.titulo}"

    def es_popular(self):
        return self.veces_prestado > 5

    def get_veces_prestado(self):
        return self.veces_prestado

    def set_veces_prestado(self, veces_prestado):
        self.veces_prestado = int(veces_prestado)


# Nueva composición: Usuarios y Préstamos
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.prestamos = []

    def __str__(self):
        return f"{self.nombre} ({self.id_usuario})"

    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def eliminar_prestamo(self, prestamo):
        if prestamo in self.prestamos:
            self.prestamos.remove(prestamo)

    def lista_prestamos(self):
        return [p for p in self.prestamos]


class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo=None):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo or datetime.now()
        self.devuelto = False

    def devolver(self):
        if self.devuelto:
            return f"El préstamo de '{self.libro.titulo}' ya fue devuelto."
        self.devuelto = True
        return f"Préstamo devuelto: {self.libro.titulo}"

    def is_active(self):
        return not self.devuelto

    def __str__(self):
        estado = "activo" if not self.devuelto else "devuelto"
        fecha = self.fecha_prestamo.strftime('%Y-%m-%d %H:%M')
        return f"{self.libro.titulo} -> {self.usuario.nombre} ({estado}, {fecha})"

# Implementación de las clases LibroFisico y LibroDigital que heredan de Libro y cumplen con el protocolo LibroProtocol
class LibroFisico(Libro):
    def calcular_duracion(self):
        return "7 días"

class LibroDigital(Libro):
    def calcular_duracion(self):
        return "14 días"
    
# Implementación de la clase Biblioteca que contiene una lista de libros y usuarios, y métodos para gestionar los libros disponibles en la biblioteca.
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def libros_disponibles(self):
        return [
            libro.titulo 
            for libro in self.libros 
            if libro.disponible]

    # Métodos para gestionar usuarios y préstamos
    def registrar_usuario(self, usuario: Usuario):
        if usuario not in self.usuarios:
            self.usuarios.append(usuario)
            return f"Usuario registrado: {usuario.nombre}"
        return f"Usuario {usuario.nombre} ya registrado"

    def prestar_a_usuario(self, libro: Libro, usuario: Usuario):
        if libro not in self.libros:
            return f"El libro '{libro.titulo}' no pertenece a esta biblioteca."
        if not libro.disponible:
            return f"El libro '{libro.titulo}' no está disponible."
        # Realizar préstamo
        msg = libro.prestar()
        prestamo = Prestamo(libro, usuario)
        self.prestamos.append(prestamo)
        usuario.agregar_prestamo(prestamo)
        return msg

    def devolver_libro(self, libro: Libro, usuario: Usuario = None):
        # Buscar préstamo activo
        for p in self.prestamos:
            if p.libro == libro and not p.devuelto:
                p.devolver()
                libro.devolver()
                if p in p.usuario.prestamos:
                    p.usuario.eliminar_prestamo(p)
                return f"Libro '{libro.titulo}' devuelto correctamente."
        return f"No se encontró un préstamo activo para '{libro.titulo}'."

    def prestamos_por_usuario(self, usuario: Usuario):
        return [p for p in self.prestamos if p.usuario == usuario]

    def prestamos_activos(self):
        return [p for p in self.prestamos if not p.devuelto]



mi_libro = LibroFisico(
    "100 Años de Soledad",
    "Gabriel Garcia Marquez",
    "9781644734728",
    True,
)

mi_libro_no_disponible = LibroFisico(
    "No disponible",
    "Diego",
    "12345678901234",
    True,
)

otro_libro = LibroFisico(
    "El Principito",
    "Saint-Exupéry",
    "9781644731234728",
    True,
)

biblioteca = Biblioteca("Biblioteca Central")

biblioteca.libros = [
    mi_libro, 
    mi_libro_no_disponible, 
    otro_libro
    ]

print(biblioteca.libros_disponibles())

# Ejemplo: registrar un usuario, prestar y devolver un libro
usuario1 = Usuario("Ana Pérez", "u1")
print(biblioteca.registrar_usuario(usuario1))

# Prestar `mi_libro` a `usuario1`
print(biblioteca.prestar_a_usuario(mi_libro, usuario1))
print("Préstamos activos:", [str(p) for p in biblioteca.prestamos_activos()])
print("Préstamos de usuario:", [str(p) for p in usuario1.lista_prestamos()])
print("Disponibles:", biblioteca.libros_disponibles())

# Devolver el libro
print(biblioteca.devolver_libro(mi_libro, usuario1))
print("Préstamos activos después de devolución:", [str(p) for p in biblioteca.prestamos_activos()])
print("Disponibles después de devolución:", biblioteca.libros_disponibles())