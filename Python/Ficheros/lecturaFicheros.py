# Para abrir el fichero
miFichero = open("textoFile.txt","rt")

# Guardamos la información para poder usarla
infoFichero = miFichero.read()

print(infoFichero)

miFichero.close()