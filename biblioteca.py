from exceptions import LibroNoDisponibleError, UsuarioNoEncontradoError


class Biblioteca:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.libros = []
        self.usuarios = []

    def libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]

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
                return libro
        raise LibroNoDisponibleError(
            f"El libro: {titulo}, no está disponible o no existe."
        )

    @staticmethod
    def validar_isbn(isbn):
        return len(isbn) >= 10