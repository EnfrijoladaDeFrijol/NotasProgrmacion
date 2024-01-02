from modulo1 import despedirse

print("\nUso de solo una función dentro de un solo modulo")
despedirse("Miriam")


# También podemos renombrar a la función que estemos ocupando
from modulo1 import despedirse as decirAdios

decirAdios("Arturo")