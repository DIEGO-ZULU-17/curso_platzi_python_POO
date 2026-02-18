"""
Módulo para generar datos de ejemplo de libros de la biblioteca.
Este módulo contiene una colección de libros preconfigurados para
facilitar las pruebas y demostraciones del sistema.
"""

from libros import LibroFisico
from usuarios import Estudiante

# Creación de 10 libros físicos con diferentes títulos y autores

libro1 = LibroFisico("Cien Años de Soledad", "Gabriel García Márquez", "9780307474728")
libro2 = LibroFisico("El Principito", "Antoine de Saint-Exupéry", "9780156012195")
libro3 = LibroFisico("Don Quijote de la Mancha", "Miguel de Cervantes", "9788491050049")
libro4 = LibroFisico("1984", "George Orwell", "9780451524935")
libro5 = LibroFisico("Orgullo y Prejuicio", "Jane Austen", "9780141439518")
libro6 = LibroFisico("El Gran Gatsby", "F. Scott Fitzgerald", "9780743273565")
libro7 = LibroFisico("Crimen y Castigo", "Fiódor Dostoyevski", "9788420674742")
libro8 = LibroFisico("Matar un Ruiseñor", "Harper Lee", "9780061120084")
libro9 = LibroFisico("El Señor de los Anillos", "J.R.R. Tolkien", "9780544003415")
libro10 = LibroFisico("La Metamorfosis", "Franz Kafka", "9788420674025")


# Creación de 10 estudiantes con diferentes nombres, cédulas y carreras
estudiante1 = Estudiante("Ana María López", "1001234567", "Ingeniería de Sistemas")
estudiante2 = Estudiante("Carlos Andrés Ruiz", "1001234568", "Medicina")
estudiante3 = Estudiante("María Fernanda Torres", "1001234569", "Derecho")
estudiante4 = Estudiante("Juan Pablo Gómez", "1001234570", "Arquitectura")
estudiante5 = Estudiante("Laura Sofía Martínez", "1001234571", "Psicología")
estudiante6 = Estudiante("Alejandro Castro", "1001234572", "Administración de Empresas")
estudiante7 = Estudiante("Valentina Pérez", "1001234573", "Diseño Gráfico")
estudiante8 = Estudiante("Santiago Ramírez", "1001234574", "Ingeniería Civil")
estudiante9 = Estudiante("Camila Andrea Vargas", "1001234575", "Comunicación Social")
estudiante10 = Estudiante("Sebastián Morales", "1001234576", "Contaduría Pública")

data_libros = [
    libro1,
    libro2,
    libro3,
    libro4,
    libro5,
    libro6,
    libro7,
    libro8,
    libro9,
    libro10,
]

data_estudiantes = [
    estudiante1,
    estudiante2,
    estudiante3,
    estudiante4,
    estudiante5,
    estudiante6,
    estudiante7,
    estudiante8,
    estudiante9,
    estudiante10,
]