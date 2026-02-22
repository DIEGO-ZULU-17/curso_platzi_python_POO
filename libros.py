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

    @property
    def es_popular(self) -> bool:
        return self.__veces_prestado > 5

    @property # @property se utiliza para definir un método como una propiedad, lo que permite acceder a su valor como si fuera un atributo, sin necesidad de llamarlo como una función. Esto es útil para proporcionar una interfaz más limpia y fácil de usar, especialmente cuando el valor se calcula dinámicamente o se basa en otros atributos.
    def veces_prestado(self) -> int:
        return self.__veces_prestado

    @veces_prestado.setter # @veces_prestado.setter se utiliza para definir un método como un setter para una propiedad previamente definida con @property. Esto permite asignar un valor a la propiedad, lo que a su vez llama al método setter para realizar cualquier lógica adicional necesaria al establecer el valor.
    def veces_prestado(self, veces_prestado):
        if veces_prestado > 0:
            self.__veces_prestado = veces_prestado
        else:
            raise ValueError("El número de veces prestado debe ser mayor que cero")

    @property
    def descripcion_completa(self) -> str:
        return f"{self.titulo} por {self.autor}, ISBN: {self.isbn}"

    def calcular_duracion(self) -> str:
        return "7 días"

    @classmethod # @classmethod es un decorador que se utiliza para definir un método de clase dentro de una clase. Un método de clase es un método que pertenece a la clase en sí, en lugar de a una instancia específica de la clase. Esto significa que el método puede ser llamado sin necesidad de crear una instancia de la clase. En el caso de crear_no_disponible, al ser un método de clase, se puede llamar directamente desde la clase Libro sin necesidad de instanciarla, lo que es útil para crear libros que no estén disponibles sin depender del estado de una instancia específica del libro. Utiliza cls porque hace referencia a la clase en sí, lo que permite crear una nueva instancia de la clase con los atributos proporcionados, marcándola como no disponible. cls es igual que Libro(), pero es más flexible porque si se hereda de la clase Libro, el método de clase seguirá funcionando correctamente al crear instancias de la subclase.
    def crear_no_disponible(cls, titulo, autor, isbn):
        return cls(titulo, autor, isbn, disponible=False)


class LibroFisico(Libro):
    def calcular_duracion(self) -> str:
        return "7 días"


class LibroDigital(Libro):
    def calcular_duracion(self) -> str:
        return "14 días"