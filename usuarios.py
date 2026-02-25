from abc import ABC, abstractmethod
from typing import Protocol

from exceptions import TituloInvalidoError


class SolicitanteProtocol(Protocol):
    def solicitar_libro(self, titulo: str) -> str:
        """Metodo que debe implementar cualquier solicitante"""
        ...


class UsuarioBase(ABC):
    @abstractmethod
    def solicitar_libro(self):
        pass

    @abstractmethod
    def metodo_prueba(self):
        pass


class Usuario(UsuarioBase):
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def solicitar_libro(self, titulo):
        return f"Solicitud de libro '{titulo}' realizada"

    def metodo_prueba(self):
        return "Metodo de prueba para saber como funciona ABC"


class Estudiante(Usuario):
    def __init__(self, nombre, cedula, carrera):
        super().__init__(nombre, cedula)
        self.carrera = carrera
        self.limite_libros = 3

    def solicitar_libro(self, titulo):
        if not titulo:
            raise TituloInvalidoError(f"El libro con el titulo: {titulo}, no es válido")

        if len(self.libros_prestados) < self.limite_libros:
            self.libros_prestados.append(titulo)
            return f"Prestamo del libro: {titulo} autorizado"
        else:
            return (
                f"No puedes prestar más libros, Limite alcanzado: {self.limite_libros}"
            )


class Profesor(Usuario):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_libros = None

    def solicitar_libro(self, titulo):
        self.libros_prestados.append(titulo)
        return f"Prestamo del libro: {titulo} autorizado"