from exceptions import (
    LibroNoDisponibleError,
    UsuarioNoEncontradoError,
    PersistenciaError,
    DatosInvalidosError,
)
from persistencia import Persistencia
from biblioteca import Biblioteca
import sys

persistencia = Persistencia()
try:
    biblioteca = persistencia.cargar_datos()
except (PersistenciaError, DatosInvalidosError) as e:
    print(f"Error al cargar datos: {e}")
    print("Se iniciará una biblioteca vacía.")
    biblioteca = Biblioteca("Biblioteca Vacía")


print("\n Bienvenido a Platzi Biblioteca \n")

print("Libros disponibles:\n")
for libro in biblioteca.libros_disponibles():
    print(libro.descripcion_completa)
print()

cedula = input("\nDigite el numero cedula: \n")
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(f"\nUsuario encontrado: {usuario.cedula}, {usuario.nombre}")
except UsuarioNoEncontradoError as e:
    print(e)
    sys.exit(1)

titulo = input("\nDigite el titulo del libro: \n")
try:
    libro = biblioteca.buscar_libro(titulo)
    print(f"El libro que selecionaste es: {libro}")
except LibroNoDisponibleError as e:
    print(e)
    sys.exit(1)

resultado = usuario.solicitar_libro(libro.titulo)
print(f"\n{resultado}")

try:
    resultado_prestar = libro.prestar()
    print(f"\n{resultado_prestar}")
except LibroNoDisponibleError as e:
    print(e)

try:
    persistencia.guardar_datos(biblioteca)
except PersistenciaError as e:
    print(f"No se pudo guardar la información: {e}")