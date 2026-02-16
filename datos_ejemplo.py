"""
Módulo para generar datos de ejemplo de libros de la biblioteca.
Este módulo contiene una colección de libros preconfigurados para
facilitar las pruebas y demostraciones del sistema.
"""

from libros import LibroFisico, LibroDigital


def obtener_libros_ejemplo():
    """
    Retorna una lista de libros de ejemplo para la biblioteca.
    
    Returns:
        list: Lista de instancias de Libro (físicos y digitales)
    """
    libros = [
        # Libros Físicos
        LibroFisico(
            "100 Años de Soledad",
            "Gabriel García Márquez",
            "9781644734728",
            disponible=True
        ),
        LibroFisico(
            "El Principito",
            "Antoine de Saint-Exupéry",
            "9781644731234728",
            disponible=True
        ),
        LibroFisico(
            "Don Quijote de la Mancha",
            "Miguel de Cervantes",
            "9788424127749",
            disponible=False
        ),
        LibroFisico(
            "La Metamorfosis",
            "Franz Kafka",
            "9788497935074",
            disponible=True
        ),
        
        # Libros Digitales
        LibroDigital(
            "Python para Principiantes",
            "Mark Lutz",
            "9781449355739",
            disponible=True
        ),
        LibroDigital(
            "Clean Code",
            "Robert C. Martin",
            "9780132350884",
            disponible=True
        ),
        LibroDigital(
            "Design Patterns",
            "Gang of Four",
            "9780201633610",
            disponible=False
        ),
        LibroFisico(
            "El Quijote",
            "Miguel de Cervantes",
            "9788420462165",
            disponible=True
        ),
        LibroFisico(
            "Orgullo y Prejuicio",
            "Jane Austen",
            "9788498383980",
            disponible=True
        ),
    ]
    
    return libros


def obtener_usuarios_ejemplo():
    """
    Retorna una lista de usuarios de ejemplo para la biblioteca.
    
    Returns:
        list: Lista de instancias de Usuario (Estudiantes y Profesores)
    """
    from usuarios import Estudiante, Profesor
    
    usuarios = [
        Estudiante("Luis", "1123123123", "Sistemas"),
        Estudiante("Jose", "56789", "Salud"),
        Estudiante("María", "9876543210", "Ingeniería"),
        Estudiante("Carlos", "1111111111", "Administración"),
        Profesor("Felipe", "123123123"),
        Profesor("Ana", "987654321"),
    ]
    
    return usuarios