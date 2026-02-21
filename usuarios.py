"""_Partimos del archivo usuarios.py y definimos la clase base con los 
atributos comunes. Las clases hijas heredan colocando el nombre de la 
clase padre entre paréntesis. 
El uso de super en el constructor (init) llama al init de la clase padre 
sin nombrarla directamente, evitando confusiones y acoplamientos innecesarios.
"""


from typing import Protocol
from abc import ABC, abstractmethod
from exceptions import TituloInvalidoError


class SolicitanteProtocol(Protocol): # Protocol es una clase de la biblioteca typing que se utiliza para definir interfaces o contratos que las clases pueden implementar. En este caso, SolicitanteProtocol define un método solicitar_libro que cualquier clase que implemente este protocolo debe proporcionar. Esto permite una mayor flexibilidad y desacoplamiento en el diseño del código, ya que cualquier clase que implemente el método solicitar_libro puede ser utilizada como un solicitante de libros sin necesidad de heredar de una clase base específica.

    def solicitar_libro(self, titulo: str) -> str:
        """Metodo que debe implementar cualquier solicitante"""
        ...

class UsuarioBase(ABC): # ABC sirve para marcar esta clase como abstracta, lo que significa que no se puede instanciar directamente. Esto es útil para definir una estructura común para las clases hijas (Estudiante y Profesor) sin permitir la creación de objetos de la clase UsuarioBase.

    @abstractmethod # El decorador @abstractmethod se utiliza para marcar el método solicitar_libro como un método abstracto, lo que significa que las clases hijas (Estudiante y Profesor) deben proporcionar una implementación concreta de este método. Esto garantiza que cualquier clase que herede de UsuarioBase implementará el método solicitar_libro, lo que es esencial para el funcionamiento del sistema de préstamos de libros en la biblioteca.

    def solicitar_libro(self):
        pass

    @abstractmethod
    def metodo_prueba(self): # Sale el error "TypeError: Can't instantiate abstract class Estudiante without an implementation for abstract method 'metodo_prueba'" porque la clase Estudiante hereda de UsuarioBase, que tiene un método abstracto llamado metodo_prueba. Al no proporcionar una implementación concreta para este método en la clase Estudiante, se considera que Estudiante es una clase abstracta y no se puede instanciar directamente. Para solucionar este error, se debe implementar el método metodo_prueba en la clase Estudiante, proporcionando una funcionalidad específica para ese método. Se corrige agregando (self) como parámetro y una implementación concreta dentro del método.
        pass

class Usuario(UsuarioBase):
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def solicitar_libro(self, titulo):
        return f"Solicitud de libro '{titulo}' realizada"

    def metodo_prueba(self):
        return "Implementación del método de prueba en Usuario" # Aquí se soluciona el TypeError porque se proporciona una implementación concreta para el método metodo_prueba, lo que permite que la clase Usuario ya no sea abstracta y pueda ser instanciada sin problemas.
    
    # Validación de nombre y cédula utilizando propiedades y setters para garantizar que los datos sean correctos y evitar errores en el sistema. Esto mejora la robustez del código al asegurarse de que los atributos nombre y cedula siempre tengan valores válidos, lo que es crucial para la gestión de usuarios en la biblioteca.
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self._nombre = value.strip()

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        if not isinstance(value, str) or not value.isdigit():
            raise ValueError("La cédula debe ser una cadena de dígitos.")
        self._cedula = value

    @property
    def nombre_completo(self):
        return f"{self.nombre} ({self.cedula})"


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