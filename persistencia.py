import json
from datetime import datetime

from biblioteca import Biblioteca
from libros import LibroFisico
from usuarios import Estudiante, Profesor


class Persistencia:
    def __init__(self, archivo="biblioteca.json") -> None:
        self.archivo = archivo

    def guardar_datos(self, biblioteca):
        datos = {
            "nombre": biblioteca.nombre,
            "usuarios": [usuario.__dict__ for usuario in biblioteca.usuarios],
            "libros": [libro.__dict__ for libro in biblioteca.libros],
            "fecha_guardado": datetime.now().isoformat(),
        }
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        with open(self.archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)

        # datos: {'titulo': 'Cien Años de Soledad', 'autor': 'Gabriel García Márquez', 'isbn': '9780307474728', 'disponible': True, '_Libro__veces_prestado': 0}

        biblioteca = Biblioteca(datos["nombre"])
        for dato_libro in datos["libros"]:
            libro = LibroFisico(
                titulo=dato_libro["titulo"],
                autor=dato_libro["autor"],
                isbn=dato_libro["isbn"],
                disponible=dato_libro["disponible"],
            )
            biblioteca.libros.append(libro)

        # datos: {'nombre': 'Felipe', 'cedula': '123123123', 'libros_prestados': [], 'limite_libros': None}
        # datos: {'nombre': 'Ana María López', 'cedula': '1001234567', 'libros_prestados': [], 'carrera': 'Ingeniería de Sistemas', 'limite_libros': 3}
        for dato_usuario in datos["usuarios"]:
            if "carrera" in dato_usuario:
                usuario = Estudiante(
                    nombre=dato_usuario["nombre"],
                    cedula=dato_usuario["cedula"],
                    carrera=dato_usuario["carrera"],
                )
            else:
                usuario = Profesor(
                    nombre=dato_usuario["nombre"], cedula=dato_usuario["cedula"]
                )
            biblioteca.usuarios.append(usuario)
        return biblioteca