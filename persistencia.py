import json
from datetime import datetime
from biblioteca import Biblioteca # El módulo biblioteca contiene la clase Biblioteca, que es la clase principal que representa la biblioteca y sus operaciones.
from libros import LibroFisico # El módulo libros contiene la clase LibroFisico, que es una subclase de Libro que representa un libro físico. Son los datos que se están guardando en el archivo JSON.
from usuarios import Usuario, Profesor, Estudiante # El módulo usuarios contiene las clases Usuario, Profesor y Estudiante, que representan los diferentes tipos de usuarios de la biblioteca. Estas clases se utilizan para crear instancias de usuarios que pueden solicitar libros y realizar otras operaciones en la biblioteca.

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

    def cargar_datos(self): # No carga datos desde ninguna instancia, sino que lee directamente del archivo JSON para reconstruir la biblioteca.
        with open(self.archivo, "r", encoding="utf-8") as f: # Usa r de read para abrir el archivo en modo lectura, lo que permite leer los datos almacenados en el archivo JSON. Al igual que en el método guardar_datos, se especifica la codificación UTF-8 para manejar correctamente caracteres especiales.
            datos = json.load(f) # json.load se utiliza para leer el contenido del archivo JSON y convertirlo de nuevo a un diccionario de Python. Esto permite acceder a los datos almacenados en el archivo JSON como un diccionario, lo que facilita la reconstrucción de las instancias de la biblioteca a partir de los datos guardados.

        # A partir de aquí se reconstruyen las instancias
        # y se retorna la biblioteca

        #print("Datos cargados desde el archivo JSON:", datos) # Se imprime el contenido del diccionario datos para verificar que se han cargado correctamente los datos desde el archivo JSON. Esto es útil para depurar y asegurarse de que la información de la biblioteca se ha leído correctamente antes de intentar reconstruir las instancias de la biblioteca a partir de esos datos.

        #print("Primer libro:", datos["libros"][0]) # Se imprime el primer libro del diccionario datos para verificar que se han cargado correctamente los datos de los libros desde el archivo JSON.
        # Se imprime: 
            # "Primer libro: {'titulo': 'Cien Años de Soledad', 'autor': 'Gabriel García Márquez', 'paginas': None, 'es_nuevo': False, 'isbn': '9780307474728', 'disponible': True, '_Libro__veces_prestado': 0}"
        # Así entendemos el formato que está guardado en el archivo y recrear cada uno de estos elementos. 


        # REGENERA LOS LIBROS DE LA BIBLIOTECA A PARTIR DE LOS DATOS CARGADOS
        biblioteca = Biblioteca(nombre=datos["nombre"])  # ejemplo de uso de la llave "nombre"

        for dato_libro in datos["libros"]:

            libro = LibroFisico(
                titulo=dato_libro["titulo"],
                autor=dato_libro["autor"],
                paginas=dato_libro["paginas"],
                es_nuevo=dato_libro["es_nuevo"],
                isbn=dato_libro["isbn"],
                disponible=dato_libro["disponible"],
            )
            biblioteca.libros.append(libro) # .append se utiliza para agregar cada instancia de libro creada a la lista de libros de la biblioteca. Esto permite reconstruir la colección de libros de la biblioteca a partir de los datos cargados desde el archivo JSON.
        
        # REGENERA LOS USUARIOS DE LA BIBLIOTECA A PARTIR DE LOS DATOS CARGADOS

        #print("Primer usuario profeso:", datos["usuarios"][0]) # Se imprime el primer usuario del diccionario datos para verificar que se han cargado correctamente los datos de los usuarios desde el archivo JSON.

        #print("Primer usuario estudiante:", datos["usuarios"][1]) # En este caso, se puede observar que el primer usuario es un profesor y el segundo es un estudiante, lo que indica que se han guardado diferentes tipos de usuarios con sus respectivas características en el archivo JSON.

            # Primer usuario profesor: {'_nombre': 'Felipe', '_cedula': '123123123', 'libros_prestados': [], 'limite_libros': None}
            # Primer usuario estudiante: {'_nombre': 'Ana María López', '_cedula': '1001234567', 'libros_prestados': [], 'carrera': 'Ingeniería de Sistemas', 'limite_libros': 3}
        
        # En los estudiantes está la variable carrera, mientras que en los profesores no, lo que nos permite diferenciarlos al momento de reconstruir las instancias de usuario.

        for dato_usuario in datos["usuarios"]:
            if "carrera" in dato_usuario:
                usuario = Estudiante(
                    nombre=dato_usuario["_nombre"],
                    cedula=dato_usuario["_cedula"],
                    carrera=dato_usuario["carrera"],
                )
            else:
                usuario = Profesor(
                    nombre=dato_usuario["_nombre"],
                    cedula=dato_usuario["_cedula"],
                )
            biblioteca.usuarios.append(usuario) # Se agrega cada instancia de usuario creada a la lista de usuarios de la biblioteca utilizando .append, lo que permite reconstruir la colección de usuarios de la biblioteca a partir de los datos cargados desde el archivo JSON.
        
        return biblioteca # Finalmente, se retorna la instancia de biblioteca reconstruida con los datos cargados desde el archivo JSON, lo que permite utilizar esta instancia para realizar operaciones en la biblioteca con los datos previamente guardados.