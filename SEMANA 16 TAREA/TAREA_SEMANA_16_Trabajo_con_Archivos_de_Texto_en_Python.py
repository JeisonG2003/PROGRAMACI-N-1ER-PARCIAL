# Trabajo con archivos de texto en Python
# Autor: Jeison Teobaldo García Arreaga
# Curso: 1er Programación (E)
# Tarea: Trabajo con Archivos de Texto en Python

# Apertura y escritura en un archivo de texto
# Se abre el archivo 'my_notes.txt' en modo escritura ('w') con codificación UTF-8
# Si el archivo no existe, Python lo crea automáticamente
with open("my_notes.txt", "w", encoding="utf-8") as file:
    # Se escriben varias líneas en el archivo, ahora con mayor extensión
    file.write("Autor: Jeison Teobaldo García Arreaga.\n")
    file.write("Curso: 1er Programación (E).\n")
    file.write("Tarea: Trabajo con Archivos de Texto en Python.\n")
    file.write("\nPython es un lenguaje poderoso y fácil de aprender, que permite a los programadores crear soluciones eficientes para una amplia variedad de problemas, desde simples scripts hasta aplicaciones complejas.\n")
    file.write("Manipular archivos de texto facilita el almacenamiento de información, permitiendo guardar y recuperar datos de manera estructurada y accesible para otros procesos o usuarios.\n")
    file.write("La constancia en la práctica fortalece las habilidades de programación, pues la repetición y la resolución de nuevos problemas ayuda a consolidar los conocimientos adquiridos.\n")

# Lectura del archivo con codificación UTF-8
# Se abre el archivo 'my_notes.txt' en modo lectura ('r') con la misma codificación
with open("my_notes.txt", "r", encoding="utf-8") as file:
    # Se lee el archivo línea por línea y se muestra en consola
    for line in file:
        print(line.strip())  # strip() elimina espacios y saltos de línea extra

