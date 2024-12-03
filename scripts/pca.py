import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

def gene_expression(file_path):
    """
    Lee un archivo de expresión génica, rellena valores nulos con 0,
    y extrae la columna 'RPKM' como una Serie de pandas.

    Args:
        file_path (str): Ruta al archivo de datos de expresión génica.

    Returns:
        pd.Series: Serie con los valores de la columna 'RPKM'.
    """
    data_frame = pd.read_csv(file_path, sep='\t')
    data_frame = data_frame.fillna(0)
    RPKM_series = pd.Series(data_frame['RPKM'])
    return RPKM_series

# Leer datos de expresión génica de los archivos de entrada
RPKM_1_N2 = gene_expression('data/gene_expression_N2.txt')
RPKM_1_NH4 = gene_expression('data/gene_expression_NH4.txt')

# Crear un DataFrame combinado para las dos condiciones
df_1 = pd.DataFrame({'RPKM_1_N2': RPKM_1_N2, 'RPKM_1_NH4': RPKM_1_NH4})

# Leer datos de regiones génicas para ambas condiciones
region_df = pd.read_csv('data/gene_region_N2.txt', sep='\t')
region_NH4_df = pd.read_csv('data/gene_region_NH4.txt', sep='\t')

# Comprobación de mantenimiento: asegurar que los DataFrames de regiones son equivalentes
print("¿Las regiones génicas son iguales en ambos DataFrames?:", region_df.equals(region_NH4_df))  

# Verificación de que todas las columnas dentro de un DataFrame contienen los mismos valores
print("¿La columna 1 es igual a la columna 2?:", region_df.iloc[:, 0].equals(region_df.iloc[:, 1]))  
print("¿La columna 2 es igual a la columna 3?:", region_df.iloc[:, 1].equals(region_df.iloc[:, 2]))  
print("¿La columna 3 es igual a la columna 1?:", region_df.iloc[:, 2].equals(region_df.iloc[:, 0]))  

# Inicializar listas para las categorías del diagrama de Venn
intersection = []  # Genes presentes en ambas condiciones
N2 = []  # Genes presentes solo en N2
NH4 = []  # Genes presentes solo en NH4

# Clasificar genes en función de sus valores RPKM
for i in df_1.index:
    if df_1.iloc[i, 0] != 0:  # Si el valor en N2 es distinto de 0
        N2.append(df_1.iloc[i, 0])
        continue
    if df_1.iloc[i, 1] != 0:  # Si el valor en NH4 es distinto de 0
        NH4.append(df_1.iloc[i, 1])
        continue
    if df_1.iloc[i, 1] == df_1.iloc[i, 0]:  # Si los valores son iguales en ambas condiciones
        intersection.append(df_1.iloc[i, 0])

# Imprimir las listas clasificadas
print("Genes presentes en ambas condiciones (intersección):", intersection)
print("Genes presentes solo en N2:", N2)
print("Genes presentes solo en NH4:", NH4)

# Verificación de que la suma de las longitudes de las listas coincide con el número de genes totales
len = __builtins__.len  # Usar la función interna `len`

# Imprimir las longitudes para asegurar la consistencia
print("Cantidad de genes presentes solo en N2:", len(N2))
print("Cantidad de genes presentes en ambas condiciones (intersección):", len(intersection))
print("Cantidad de genes presentes solo en NH4:", len(NH4))

# Generar un diagrama de Venn basado en las longitudes calculadas
venn2((len(N2), len(NH4), len(intersection)), set_labels=('N2', 'NH4'))
plt.show()
