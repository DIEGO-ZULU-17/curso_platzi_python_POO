"""En este archivo se definen las excepciones personalizadas para la biblioteca."""

class BibliotecaError(Exception):
    pass

class TituloInvalidoError(BibliotecaError):
    pass

class LibroNoDisponibleError(BibliotecaError):
    def __init__(self, titulo: str | None = None):
        if titulo:
            mensaje = f"El libro '{titulo}' no está disponible para préstamo."
        else:
            mensaje = "El libro no está disponible para préstamo."
        super().__init__(mensaje)

class UsuarioNoEncontrado(Exception):
    """El usuario no fue encontrado en el sistema"""
    pass