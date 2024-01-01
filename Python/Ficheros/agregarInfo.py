miFichero = open("agregarInfo.txt","at") # append

cadenaAgregada = "\nCadena agreagada"

# Aqquí escribimos pero ahora por el \n se pondrá abajo
miFichero.write(cadenaAgregada)

miFichero.close()