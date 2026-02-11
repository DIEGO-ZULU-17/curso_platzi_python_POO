"""_Partimos del archivo usuarios.py y definimos la clase base con los 
atributos comunes. Las clases hijas heredan colocando el nombre de la 
clase padre entre paréntesis. 
El uso de super en el constructor (init) llama al init de la clase padre 
sin nombrarla directamente, evitando confusiones y acoplamientos innecesarios.
"""

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

# Pruebas de préstamo
print("=== PRUEBAS DE PRÉSTAMO ===")
print("\n")

print(estudiante.solicitar_libro("Python básico"))
print(estudiante.solicitar_libro("Python intermedio"))
print(estudiante.solicitar_libro("Python avanzado"))
print(estudiante.solicitar_libro("Python Django"))  # Debe indicar límite alcanzado: 3

print("\n") # Salto de línea para separar las pruebas de estudiante y profesor

print(profesor.solicitar_libro("Python básico"))
print(profesor.solicitar_libro("Python intermedio"))
print(profesor.solicitar_libro("Python avanzado"))
print(profesor.solicitar_libro("Python Django"))    # Todos autorizados

# Pruebas de devolución de libros
print("\n=== PRUEBAS DE DEVOLUCIÓN ===")
print(f"Libros prestados del estudiante antes: {estudiante.libros_prestados}")
print(estudiante.devolver_libro("Python básico"))  # Debe devolver exitosamente
print(f"Libros prestados del estudiante después: {estudiante.libros_prestados}")

print("\nIntentando devolver un libro que no tiene...")
print(estudiante.devolver_libro("Python Django"))  # Debe indicar que no tiene este libro

print("\n")
print(f"Libros prestados del profesor antes: {profesor.libros_prestados}")
print(profesor.devolver_libro("Python intermedio"))  # Debe devolver exitosamente
print(f"Libros prestados del profesor después: {profesor.libros_prestados}")

print("\nIntentando devolver un libro que no tiene...")
print(profesor.devolver_libro("Harry Potter"))  # Debe indicar que no tiene este libro