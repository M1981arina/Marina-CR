# Autor: Johanna Castillo
# Descripción: Escritura, lectura y cierre de un archivo de texto
# Fecha: 05 de Abril 2025

with open("my_notes.txt", "w") as archivo:
    # Escribimos múltiples líneas de notas personales usando el método write().
    archivo.write("Hoy he comenzado a practicar el manejo de archivos en Python.\n")
    archivo.write("Aprender a trabajar con archivos es fundamental para el desarrollo de software.\n")
    archivo.write("Me siento motivado a seguir practicando todos los días.\n")
    archivo.write("Entendí que usar 'with open()' también cierra el archivo automáticamente.\n")
    archivo.write("En el futuro quiero aplicar esto para leer archivos de configuración o logs.\n")

# No es necesario cerrar el archivo manualmente si se usa 'with open()',
print("📖 Leyendo el contenido del archivo 'my_notes.txt':\n")

with open("my_notes.txt", "r") as archivo:
    # Usamos un bucle para leer línea por línea usando readline() implícito en el bucle for.
    for linea in archivo:
        # strip() elimina el salto de línea al final de cada línea para una impresión más limpia.
        print(linea.strip())
