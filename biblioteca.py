from exceptions import LibroNoDisponibleError, UsuarioNoEncontradoError


class Biblioteca:
    def __init__(self, name) -> None:
        self.name = name
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