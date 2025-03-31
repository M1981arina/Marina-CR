# 1. Crear un Diccionario con información ficticia
informacion_personal = {
    "nombre": "Johanna Castillo",  # Nombre ficticio
    "edad": 43,  # Edad ficticia
    "ciudad": "Arenillas",  # Ciudad original
    "profesion": "Tecnóloga en Informática"  # Profesión original
}

# 2. Acceder y Modificar Valores
# Cambiar la ciudad a otra diferente
informacion_personal["ciudad"] = "Arenillas"

# Agregar/modificar la clave 'profesion' con un nuevo valor
informacion_personal["profesion"] = "Tecnóloga Informática"

# 3. Verificar Existencia de Claves
# Si la clave "telefono" no existe, se agrega con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "++593969280318"

# 4. Eliminar una Clave
# Se elimina la clave "edad" ya que no es necesaria
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# 5. Imprimir el Diccionario Final
# Mostramos el diccionario después de todas las modificaciones
print("Diccionario Final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

    Diccionario
    Final:

    nombre: Johanna Castillo

    ciudad: Arenillas
    edad: 43

    profesión: Tecnóloga en Informática

    teléfono: +593969280318