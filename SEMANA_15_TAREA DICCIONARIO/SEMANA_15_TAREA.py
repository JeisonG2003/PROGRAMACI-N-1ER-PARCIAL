# Garcia Arreaga Jeison Teobaldo
# Crear un diccionario llamado informacion_personal con la información solicitada
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Guayaquil"

# Verificar si la clave "telefono" existe en el diccionario. Si no existe, agregarla con el número respectivo
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminar la clave "edad" del diccionario, ya que esa información no es necesaria
del informacion_personal["edad"]

# Imprimir el diccionario resultante después de realizar todas las operaciones, mostrando cada par clave-valor en líneas separadas
print("Diccionario Final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")
