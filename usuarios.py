"""_Partimos del archivo usuarios.py y definimos la clase base con los 
atributos comunes. Las clases hijas heredan colocando el nombre de la 
clase padre entre paréntesis. 
El uso de super en el constructor (init) llama al init de la clase padre 
sin nombrarla directamente, evitando confusiones y acoplamientos innecesarios.
"""

from typing import Protocol # Protocol ayuda en que el código sea más flexible y menos acoplado, ya que permite definir una interfaz que las clases pueden implementar sin necesidad de heredar de una clase base específica. Esto es especialmente útil en casos donde se desea que diferentes clases compartan un comportamiento común sin tener que estar relacionadas jerárquicamente a través de la herencia tradicional. Al usar Protocol, se puede definir un conjunto de métodos que una clase debe implementar para ser considerada compatible con esa interfaz, lo que facilita la reutilización de código y la integración de diferentes clases sin necesidad de una relación de herencia directa.

class SolicitanteProtocol(Protocol): # Definimos un protocolo para la interfaz de solicitante, lo que permite que cualquier clase que implemente este protocolo pueda ser utilizada como solicitante en el sistema de préstamos de libros, sin necesidad de heredar de una clase base específica.

    def solicitar_libro(self, titulo: str) -> str: # Typing indica que el método solicitar_libro debe recibir un argumento de tipo str (el título del libro) y retornar un valor de tipo str (el resultado de la solicitud de préstamo). Esto ayuda a mejorar la legibilidad del código y a detectar errores de tipo durante el desarrollo, ya que proporciona información clara sobre los tipos de datos esperados para los argumentos y el valor de retorno del método solicitar_libro.

        """Retorna el resultado de la solicitud de préstamo."""
        ...

class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = [] # Se inicializa la lista de libros prestados para cada estudiante, lo que permite llevar un registro de los libros que cada estudiante tiene prestados.
        # Se pone aquí la lista porque ambos usuarios están usando la lista de libros prestados, por lo que es un atributo común que se puede definir en la clase padre Usuario para evitar duplicación de código en las clases hijas Estudiante y Profesor.

    def solicitar_libro(self, titulo): # Permite agregar dentro de una lista de libros prestados el título del libro solicitado por el usuario, lo que permite llevar un registro de los libros que cada usuario tiene prestados.
        return f"Solicitud de libro '{titulo}' realizada."


class Estudiante(Usuario): # Se hereda en el paréntesis para que herede los atributos de la clase padre.
    def __init__(self, nombre, cedula, carrera):

        super().__init__(nombre, cedula) # Super permite llamar al constructor de la clase padre para inicializar los atributos heredados sin tener que nombrar directamente la clase padre, lo que hace que el código sea más flexible y menos acoplado.
        # __init__ es el constructor de la clase, es decir, el método que se ejecuta al crear una instancia de la clase. Por ejemplo, cuando se crea un objeto de la clase Estudiante, se llama automáticamente al método __init__ para inicializar los atributos del objeto.
        self.carrera = carrera # Atributo específico de la clase Estudiante, que no es heredado de la clase Usuario. Se debe agregar en el constructor de la clase Estudiante para que se inicialice correctamente al crear una instancia de Estudiante.
        self.limite_libros = 3 # Se establece un límite de libros para los estudiantes, lo que significa que un estudiante no puede tener más de 3 libros prestados al mismo tiempo. Este atributo es específico de la clase Estudiante y no se hereda de la clase Usuario, por lo que se debe agregar en el constructor de la clase Estudiante para que se inicialice correctamente al crear una instancia de Estudiante.


    def solicitar_libro(self, titulo): # Copiamos el método solicitar_libro para agregar la lógica de límite de libros prestados para los estudiantes, ya que el comportamiento de solicitar un libro es diferente para los estudiantes en comparación con los profesores, por lo que se debe sobreescribir el método solicitar_libro en la clase Estudiante para implementar esta lógica específica.
        if len(self.libros_prestados) < self.limite_libros: # len permite obtener la cantidad de libros prestados actualmente por el estudiante, y se compara con el límite establecido para determinar si se puede autorizar el préstamo del libro solicitado.
            self.libros_prestados.append(titulo)
            return f"Préstamo del libro '{titulo}' autorizado."
        else:
            return (
                f"No puedes prestar más libros. Límite alcanzado: {self.limite_libros}."
            )

    def devolver_libro(self, titulo): # Permite a un estudiante devolver un libro y actualiza la lista de libros prestados. Gestiona el caso en que el estudiante intente devolver un libro que no tiene.
        if titulo in self.libros_prestados: # Verifica si el libro solicitado está en la lista de libros prestados del estudiante.
            self.libros_prestados.remove(titulo) # Si el libro está en la lista, lo elimina usando el método remove().
            return f"Devolución del libro '{titulo}' registrada. Total de libros: {len(self.libros_prestados)}."
        else: # Si el libro no está en la lista de libros prestados, se retorna un mensaje de error.
            return f"No tienes el libro '{titulo}' prestado."

class Profesor(Usuario): # Al agregar la clase Profesor como hija de Usuario, se heredan los atributos y métodos de la clase padre como nombre y cedula.
    def __init__(self, nombre, cedula): # El método constructor se ejecuta automáticamente al crear una instancia de la clase Profesor.
        super().__init__(nombre, cedula)
        self.limite_libros = None # No hay límite de libros para los profesores, por lo que se establece como None. Este atributo es específico de la clase Profesor y no se hereda de la clase Usuario, por lo que se debe agregar en el constructor de la clase Profesor para que se inicialice correctamente al crear una instancia de Profesor.

# Esta es una herencia simple, ya que solo hay una clase padre (Usuario) y dos clases hijas (Estudiante y Profesor). No debemos sobreescribir el método solicitar_libro en las clases hijas, ya que el comportamiento de solicitar un libro es el mismo tanto para estudiantes como para profesores, por lo que se puede utilizar el método heredado de la clase Usuario sin necesidad de modificarlo.
# Tampoco debemos volver a escribir las líneas de nombre y cedula en las clases hijas, ya que estos atributos son heredados de la clase Usuario y se inicializan correctamente al llamar al constructor de la clase padre con super().__init__(nombre, cedula). Esto evita la duplicación de código y mantiene una estructura más limpia y mantenible.
    
    def solicitar_libro(self, titulo):
        self.libros_prestados.append(titulo)
        return f"Préstamo del libro '{titulo}' autorizado."

    def devolver_libro(self, titulo): # Permite a un profesor devolver un libro y actualiza la lista de libros prestados.
        if titulo in self.libros_prestados:
            self.libros_prestados.remove(titulo)
            return f"Devolución del libro '{titulo}' registrada. Total de libros: {len(self.libros_prestados)}."
        else:
            return f"No tienes el libro '{titulo}' prestado."

# Hacemos las pruebas creando instancias de Estudiante y Profesor, y solicitando libros para cada uno, lo que permite verificar que la lógica de límite de libros prestados para los estudiantes se implementa correctamente, mientras que los profesores pueden solicitar libros sin restricciones.

# Instanciar objetos: retorna una variable que representa un objeto de la clase, lo que permite crear múltiples objetos con diferentes atributos y comportamientos basados en la misma clase. Por ejemplo, al crear una instancia de Estudiante, se puede asignar un nombre, cédula y carrera específicos para ese estudiante, lo que permite tener múltiples estudiantes con diferentes características en el sistema. De manera similar, al crear una instancia de Profesor, se puede asignar un nombre y cédula específicos para ese profesor, lo que permite tener múltiples profesores con diferentes características en el sistema. Esto es fundamental para la programación orientada a objetos, ya que permite modelar entidades del mundo real de manera más flexible y organizada.

estudiante = Estudiante("Luis", "123456", "Ingeniería") # Las variables empiezan con minúscula por convención, y en mayúscula para las clases, así podemos crear instancias de las clases.
profesor = Profesor("Ana", "987654")

estudiante_1 = Estudiante("Jose", "654321", "Salud")

usuarios = [estudiante, profesor, estudiante_1] # Se crea una lista de usuarios para almacenar las instancias de Estudiante y Profesor, lo que permite gestionar y acceder a los usuarios de manera organizada en el sistema. Esta lista puede ser utilizada para realizar operaciones como solicitar libros, devolver libros, o mostrar información de los usuarios.

for usuario in usuarios: # Se itera sobre la lista de usuarios para realizar operaciones específicas según el tipo de usuario. Esto permite aplicar lógica diferente para estudiantes y profesores, como el límite de libros prestados para los estudiantes y la capacidad ilimitada para los profesores. La iteración sobre la lista de usuarios facilita la gestión y manipulación de los objetos en el sistema.
    print(usuario.solicitar_libro("Título de ejemplo")) # Se llama al método solicitar_libro para cada usuario en la lista, lo que permite verificar que el comportamiento de solicitud de libros se implementa correctamente tanto para estudiantes como para profesores, y que se respetan las restricciones de préstamo según el tipo de usuario.

# Lista tipada: solo admite elementos que cumplan SolicitanteProtocol
#usuarios: list[SolicitanteProtocol] = []

#usuarios.append(Libro("Título de prueba", "Autor de prueba", "ISBN"))  # error en el editor: no implementa solicitar_libro    

class Estudiante:
    def solicitar_libro(self, titulo: str) -> str: # 
        return f"\n Préstamo autorizado para estudiante: {titulo}" # El método solicitar_libro en la clase Estudiante implementa la lógica específica para autorizar el préstamo de un libro a un estudiante, lo que permite diferenciar el comportamiento de solicitud de libros entre estudiantes y profesores en el sistema de préstamos de libros. Al implementar este método, se puede gestionar adecuadamente las solicitudes de préstamo según el tipo de usuario, asegurando que se respeten las restricciones y políticas establecidas para cada categoría de usuario.

class Profesor:
    def solicitar_libro(self, titulo: str) -> str:
        return f"\n Préstamo autorizado para profesor: {titulo}"

usuarios: list[SolicitanteProtocol] = [Estudiante(), Profesor()] # Se crea una lista de usuarios que implementan el protocolo SolicitanteProtocol, lo que permite almacenar tanto estudiantes como profesores en la misma lista y gestionar sus solicitudes de préstamo de manera uniforme a través del método solicitar_libro definido en el protocolo. Esto facilita la integración de diferentes tipos de usuarios en el sistema sin necesidad de una relación de herencia directa, promoviendo un diseño más flexible y desacoplado.

for usuario in usuarios:
    print(usuario.solicitar_libro("Título de prueba")) # Al iterar sobre la lista de usuarios que implementan el protocolo SolicitanteProtocol, se llama al método solicitar_libro para cada usuario, lo que permite verificar que el comportamiento de solicitud de libros se implementa correctamente tanto para estudiantes como para profesores, y que se respetan las restricciones de préstamo según el tipo de usuario. Esto demuestra la flexibilidad del diseño basado en protocolos, ya que se puede gestionar diferentes tipos de usuarios sin necesidad de una relación de herencia directa.


# ============================================================================
# PROTOCOL PARA LIBROS - Polimorfismo basado en contratos claros
# ============================================================================
# Un Protocol define un contrato que cualquier clase puede implementar
# sin necesidad de herencia. De esta forma, LibroFisico y LibroElectronico
# son independientes pero cumplen el mismo contrato (LibroProtocol).

class LibroProtocol(Protocol):
    """Define el contrato que deben cumplir todos los tipos de libros."""
    
    def prestar(self) -> str:
        """Retorna un mensaje de autorización de préstamo específico del tipo."""
        ...
    
    def calcular_duracion(self) -> str:
        """Retorna la duración del préstamo según el tipo de libro."""
        ...


class LibroFisico:
    """Implementación de un libro físico con su propia lógica de préstamo.
    
    Los libros físicos tienen una duración estándar de 14 días y requieren devolución física. No hereda de ninguna clase base, pero implementa el contrato LibroProtocol.
    """
    
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
    
    def prestar(self) -> str:
        """Lógica de préstamo para libros físicos: se registra en el sistema."""
        return f"Libro físico '{self.titulo}' de {self.autor} prestado. Por favor, cuídalo bien."
    
    def calcular_duracion(self) -> str:
        """Los libros físicos se prestan por 14 días."""
        return f"Duración del préstamo: 14 días (debe ser devuelto en perfectas condiciones)."


class LibroElectronico:
    """Implementación de un libro electrónico con su propia lógica de préstamo.
    
    Los libros electrónicos operan diferente: no se pierden, pueden ser copiados, y tienen acceso digital. No hereda de ninguna clase base, pero implementa el contrato LibroProtocol.
    """
    
    def __init__(self, titulo: str, autor: str, formato: str):
        self.titulo = titulo
        self.autor = autor
        self.formato = formato  # PDF, EPUB, MOBI, etc.
    
    def prestar(self) -> str:
        """Lógica de préstamo para libros electrónicos: acceso digital inmediato."""
        return f"Libro electrónico '{self.titulo}' de {self.autor} ({self.formato}) - Acceso digital autorizado instantáneamente."
    
    def calcular_duracion(self) -> str:
        """Los libros electrónicos se prestan por 30 días."""
        return f"Duración del acceso: 30 días (acceso digital ilimitado durante este período)."


# ============================================================================
# DEMOSTRACIÓN DE POLIMORFISMO CON LISTA TIPADA
# ============================================================================
# A pesar de que LibroFisico y LibroElectronico son clases independientes,
# pueden convivir en la misma lista tipada gracias al Protocol.
# El método prestar() y calcular_duracion() se comportan distintamente
# según el tipo concreto, demostrando polimorfismo en acción.

print("\n" + "="*70)
print("SISTEMA DE GESTIÓN DE BIBLIOTECA CON PROTOCOLS")
print("="*70)

# Crear instancias de diferentes tipos de libros
libro_fisico_1 = LibroFisico("Cien años de soledad", "Gabriel García Márquez")
libro_fisico_2 = LibroFisico("Don Quijote", "Miguel de Cervantes")
libro_electronico_1 = LibroElectronico("Clean Code", "Robert C. Martin", "PDF")
libro_electronico_2 = LibroElectronico("Python Avanzado", "Guido van Rossum", "EPUB")

# Lista tipada que acepta cualquier objeto que implemente LibroProtocol
biblioteca: list[LibroProtocol] = [
    libro_fisico_1,
    libro_fisico_2,
    libro_electronico_1,
    libro_electronico_2
]

# Iterar sobre la biblioteca: mismo interface, comportamientos distintos
print("\n📖 Procesando solicitudes de préstamo en la biblioteca:\n")
for libro in biblioteca:
    print(f"{libro.prestar()}")
    print(f"  {libro.calcular_duracion()}\n")

print("="*70)
print("✅ Polimorfismo en acción: LibroFisico y LibroElectronico implementan")
print("   el mismo Protocol (LibroProtocol) pero con lógicas diferentes.")
print("="*70)