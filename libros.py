from typing import Protocol, Optional
from abc import ABC, abstractmethod

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


class LibroBase(ABC):
    def __init__(self, titulo: str, autor: str, paginas: Optional[int] = None, es_nuevo: bool = False):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.es_nuevo = es_nuevo

    @abstractmethod
    def calcular_duracion(self) -> str:
        raise NotImplementedError


class Libro(LibroBase):
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True,
                 paginas: Optional[int] = None, es_nuevo: bool = False):
        super().__init__(titulo, autor, paginas, es_nuevo)
        self.isbn = isbn
        self.disponible = disponible
        self.__veces_prestado = 0

    def __str__(self):
        return f"{self.titulo} por {self.autor} disponible: {self.disponible}"

    def prestar(self) -> str:
        if not self.disponible:
            raise LibroNoDisponibleError(f"'{self.titulo}' no está disponible")

        self.disponible = False
        self.__veces_prestado += 1
        return f"'{self.titulo}' prestado exitosamente. Total préstamos: {self.__veces_prestado}"

    def devolver(self) -> str:
        self.disponible = True
        return f"'{self.titulo}' devuelto y disponible nuevamente"

    def es_popular(self) -> bool:
        return self.__veces_prestado > 5

    def get_veces_prestado(self) -> int:
        return self.__veces_prestado

    def set_veces_prestado(self, veces_prestado: int) -> None:
        self.__veces_prestado = veces_prestado


class LibroFisico(Libro):
    def calcular_duracion(self) -> str:
        return "7 días"


class LibroDigital(Libro):
    def calcular_duracion(self) -> str:
        return "14 días"