"""_Partimos del archivo usuarios.py y definimos la clase base con los 
atributos comunes. Las clases hijas heredan colocando el nombre de la 
clase padre entre paréntesis. 
El uso de super en el constructor (init) llama al init de la clase padre 
sin nombrarla directamente, evitando confusiones y acoplamientos innecesarios.
"""


from typing import Protocol

from exceptions import TituloInvalidoError


class SolicitanteProtocol(Protocol):
    def solicitar_libro(self, titulo: str) -> str:
        """Metodo que debe implementar cualquier solicitante"""
        ...


class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def solicitar_libro(self, titulo):
        return f"Solicitud de libro '{titulo}' realizada"


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