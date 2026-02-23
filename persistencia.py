import json
from datetime import datetime

class Persistencia:
    def __init__(self, archivo="biblioteca.json"): # Método constructor que inicializa la clase Persistencia con un archivo JSON específico.
        self.archivo = archivo
# Esta clase Persistencia se encarga de manejar la lectura y escritura de datos en un archivo JSON. El método __init__ inicializa la clase con el nombre del archivo que se utilizará para almacenar los datos de la biblioteca. Por defecto, el archivo se llama "biblioteca.json", pero se puede especificar otro nombre al crear una instancia de la clase.

    def guardar_datos(self, biblioteca):
        datos = {
            "nombre": biblioteca.nombre,
            "usuarios": [usuario.__dict__ for usuario in biblioteca.usuarios],
            "libros": [libro.__dict__ for libro in biblioteca.libros],
            "fecha_guardado": datetime.now().isoformat()
        }
    # Esta funcion guardar_datos toma un objeto biblioteca como argumento y crea un diccionario llamado datos para almacenar la información de la biblioteca. En este caso, se guarda el nombre de la biblioteca en el diccionario.
    # dict permite convertir cada usuario y libro en un diccionario, lo que facilita la serialización de los datos a formato JSON. Esto es necesario porque los objetos de las clases Usuario y Libro no pueden ser directamente convertidos a JSON, pero sus representaciones en forma de diccionario sí pueden serlo. Al convertir cada usuario y libro a un diccionario, se asegura que toda la información relevante de la biblioteca se pueda guardar correctamente en el archivo JSON.

        with open(self.archivo, "w", encoding="utf-8") as f: 
            json.dump(datos, f, indent=2, ensure_ascii=False)
        # El bloque with se utiliza para abrir el archivo en modo escritura ("w" de write) con codificación UTF-8 para las ñ y tildes. Esto asegura que el archivo se cierre automáticamente después de escribir los datos, incluso si ocurre un error durante la escritura. 
        # Dentro del bloque, se utiliza json.dump para escribir el diccionario datos en el archivo JSON, con una indentación de 2 espacios para mejorar la legibilidad y ensure_ascii=False para permitir caracteres no ASCII en el archivo JSON. Caracteres no ASCII significa que se pueden incluir caracteres especiales como letras acentuadas, eñes, y otros caracteres que no forman parte del conjunto ASCII estándar. Esto es importante para garantizar que los datos de la biblioteca se guarden correctamente sin perder información debido a problemas de codificación.