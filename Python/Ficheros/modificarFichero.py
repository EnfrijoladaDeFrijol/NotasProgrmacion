# Creamos el archivo, usamos open para crearlo
miFichero = open("mificheroCreado.txt","wt") # write text

textoFichero = "Prueba del fichero, texto alternativo"

# Escribimos sobre el fichero
miFichero.write(textoFichero)

# Cerramos el fichero de la linea donde guardamso el open
miFichero.close()

# Para borrar un fichero
import os
#os.remove("miFicheroCreado.txt")