# Para usar archivos de Excel
import pandas as pd

# Para acceder ala rchivo
archivoExcel = pd.ExcelFile("/Users/Arthur/Documents/NotasProgramacion/Python/Excel/archivoEjemplo.xlsx")
# Especificamos alhoja
misDatos = archivoExcel.parse('Hoja1')

print(misDatos)