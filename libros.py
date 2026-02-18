from typing import Protocol

from exceptions import LibroNoDisponibleError


class LibroProtocol(Protocol):
    def prestar(self) -> str:
        """Método de prestar un libro"""
        ...

    def devolver(self) -> str:
        """Método de devolver un libro"""
        ...

    def calcular_duracion(self) -> str:
        """Calcula el tiempo de prestamo"""
        ...


class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.__veces_prestado = 0

    def __str__(self):
        return f"{self.titulo} por {self.autor} disponible: {self.disponible}"

    def prestar(self):
        if not self.disponible: # not self.disponible significa que si el libro no está disponible (es decir, si self.disponible es False), entonces se ejecutará el bloque de código dentro del if. En este caso, se lanzará una excepción LibroNoDisponibleError con un mensaje que indica que el libro no está disponible para préstamo.
            raise LibroNoDisponibleError(f"'{self.titulo}' no está disponible")

        if self.disponible:
            self.disponible = False
            self.__veces_prestado += 1
            return f"'{self.titulo}' prestado exitosamente. Total préstamos: {self.__veces_prestado}"

    def devolver(self):
        self.disponible = True
        return f"'{self.titulo}' devuelto y disponible nuevamente"

    def es_popular(self):
        return self.__veces_prestado > 5

    def get_veces_prestado(self):
        return self.__veces_prestado

    def set_veces_prestado(self, veces_prestado):
        self.__veces_prestado = veces_prestado


class LibroFisico(Libro):
    def calcular_duracion(self):
        return "7 días"


class LibroDigital(Libro):
    def calcular_duracion(self):
        return "14 días"