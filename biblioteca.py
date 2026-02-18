from exceptions import LibroNoDisponibleError, UsuarioNoEncontradoError


class Biblioteca:
    def __init__(self, name) -> None:
        self.name = name
        self.libros = []
        self.usuarios = []

    def libros_disponibles(self):
        return [libro.titulo for libro in self.libros if libro.disponible]

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