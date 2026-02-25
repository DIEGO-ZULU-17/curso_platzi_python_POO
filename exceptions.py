class BibliotecaError(Exception):
    """Excepción base para errores de la biblioteca"""

    pass


class LimitePrestamosError(BibliotecaError):
    """Se excedió el límite de préstamos permitidos"""

    pass


class TituloInvalidoError(BibliotecaError):
    """El título del libro no es válido"""

    pass


class LibroNoDisponibleError(BibliotecaError):
    """El libro no está disponible para préstamo"""

    pass


class UsuarioNoEncontradoError(BibliotecaError):
    """El usuario no fue encontrado en el sistema"""

    pass


class PersistenciaError(BibliotecaError):
    """Errores relacionados con persistencia de datos (I/O, formato)"""

    pass


class ArchivoNoEncontradoError(PersistenciaError):
    """El archivo de persistencia no fue encontrado"""

    pass


class DatosInvalidosError(PersistenciaError):
    """Los datos leídos tienen un formato inválido"""

    pass