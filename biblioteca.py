from exceptions import LibroNoDisponibleError, UsuarioNoEncontradoError


class Biblioteca:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.libros = []
        self.usuarios = []

    def buscar_usuario(self, cedula):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        raise UsuarioNoEncontradoError(
            f"El usuario con la cedula: {cedula} no fue encontrado"
        )

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                return libro # Se usa libro en minúscula para evitar confusiones con la clase Libro.
                # return significa que se encontró el libro y se devuelve la instancia del libro encontrado, es decir, el objeto que representa ese libro específico en la biblioteca.
        raise LibroNoDisponibleError(
            f"El libro: {titulo}, no está disponible o no existe."
        )

    @property
    def libros(self):
        return self._libros

    @libros.setter
    def libros(self, value):
        if not isinstance(value, list):
            raise TypeError("libros debe ser una lista de instancias de Libro.")
        # validación opcional por elemento (import dentro para evitar ciclos)
        try:
            from libros import Libro
            for item in value:
                if not isinstance(item, Libro):
                    raise TypeError("Todos los elementos de libros deben ser instancias de Libro.")
        except ImportError:
            # Si no existe el módulo libros, solo validar tipo de lista
            pass
        self._libros = value

    @property
    def libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]  

    @staticmethod # @staticmethod es un decorador que se utiliza para definir un método estático dentro de una clase. Un método estático es un método que pertenece a la clase en sí, en lugar de a una instancia específica de la clase. Esto significa que el método puede ser llamado sin necesidad de crear una instancia de la clase. En el caso de validar_isbn, al ser un método estático, se puede llamar directamente desde la clase Biblioteca sin necesidad de instanciarla, lo que es útil para realizar validaciones relacionadas con los libros sin depender del estado de una instancia específica de la biblioteca. 
    def validar_isbn(isbn: str) -> bool:
        return len(isbn) >= 10
