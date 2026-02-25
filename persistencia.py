import json
from datetime import datetime

from biblioteca import Biblioteca
from libros import LibroFisico
from usuarios import Estudiante, Profesor
from exceptions import (
    PersistenciaError,
    ArchivoNoEncontradoError,
    DatosInvalidosError,
)
from config import ENCODING


class Persistencia:
    def __init__(self, archivo="biblioteca.json") -> None:
        self.archivo = archivo

    def guardar_datos(self, biblioteca):
        datos = {
            "nombre": biblioteca.nombre,
            "usuarios": [],
            "libros": [libro.__dict__ for libro in biblioteca.libros],
            "fecha_guardado": datetime.now().isoformat(),
        }
        # Serializar usuarios incluyendo el tipo de usuario para restauración
        for usuario in biblioteca.usuarios:
            udata = usuario.__dict__.copy()
            udata["tipo"] = usuario.__class__.__name__
            datos["usuarios"].append(udata)

        try:
            with open(self.archivo, "w", encoding=ENCODING) as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
        except Exception as e:
            raise PersistenciaError(f"Error guardando datos en {self.archivo}: {e}")

    def cargar_datos(self):
        try:
            with open(self.archivo, "r", encoding=ENCODING) as f:
                datos = json.load(f)
        except FileNotFoundError:
            # Archivo ausente: devolver una biblioteca vacía sin imprimir mensajes de depuración
            return Biblioteca("Biblioteca Vacía")
        except json.JSONDecodeError as e:
            raise DatosInvalidosError(f"El archivo {self.archivo} contiene JSON inválido: {e}")
        except Exception as e:
            raise PersistenciaError(f"Error leyendo {self.archivo}: {e}")

        # validar estructura mínima
        if not isinstance(datos, dict) or "nombre" not in datos:
            raise DatosInvalidosError("Estructura de datos inválida en el archivo de persistencia")

        biblioteca = Biblioteca(datos.get("nombre", "Biblioteca"))

        for dato_libro in datos.get("libros", []):
            try:
                libro = LibroFisico(
                    titulo=dato_libro.get("titulo", ""),
                    autor=dato_libro.get("autor", ""),
                    isbn=dato_libro.get("isbn", ""),
                    disponible=dato_libro.get("disponible", True),
                )
                biblioteca.libros.append(libro)
            except Exception:
                # Omitir entradas inválidas silenciosamente
                continue

        for dato_usuario in datos.get("usuarios", []):
            try:
                tipo = dato_usuario.get("tipo", "Profesor")
                if tipo == "Estudiante":
                    usuario = Estudiante(
                        nombre=dato_usuario.get("nombre", ""),
                        cedula=dato_usuario.get("cedula", ""),
                        carrera=dato_usuario.get("carrera", ""),
                    )
                else:
                    usuario = Profesor(
                        nombre=dato_usuario.get("nombre", ""), cedula=dato_usuario.get("cedula", "")
                    )
                biblioteca.usuarios.append(usuario)
            except Exception:
                # Omitir usuarios inválidos silenciosamente
                continue

        return biblioteca