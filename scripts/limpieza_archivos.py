#Script de limpieza de archivos (POSIBLEMENTE SOLO PARA EL MULTIFACTOR)
import pandas as pd

def limpieza_archivos(file1A, file1B, file2A, file2B):
    """
    Función para realizar la limpieza de archivos de expresión génica y metadatos. 
    Esta función carga, limpia y organiza los datos de expresión de los genes, 
    eliminando aquellos genes con bajas lecturas y organizando los metadatos 
    correspondientes a las muestras.

    Parámetros:
    file1A (str): Ruta del primer archivo de expresión génica (grupo A, condición A).
    file1B (str): Ruta del segundo archivo de expresión génica (grupo A, condición B).
    file2A (str): Ruta del tercer archivo de expresión génica (grupo B, condición A).
    file2B (str): Ruta del cuarto archivo de expresión génica (grupo B, condición B).

    Retorna:
    tuple: Un tuple que contiene dos elementos:
        - genes_clean (DataFrame): DataFrame con los datos de expresión génica 
          limpios (solo genes con lecturas suficientes).
        - df_meta (DataFrame): DataFrame con los metadatos (condición y grupo).
    """

    # Lista con los archivos de entrada
    files = [file1A, file1B, file2A, file2B]

    # Lista para almacenar las tablas de expresión génica de cada archivo
    table = []

    # Cargar cada archivo utilizando la función 'read_table' y almacenarlos en la lista 'table'
    for i in files:
        table.append(read_table(i))

    # Crear un diccionario con el índice como clave y las tablas de expresión como valor
    diccionario = dict(zip(range(len(table)), table))

    # Crear un DataFrame con los datos de expresión de genes, utilizando el índice de la primera tabla
    # y los nombres de las tablas como las columnas
    genes = pd.DataFrame(diccionario, index=diccionario[0].index, columns=diccionario.keys())

    # Transponer el DataFrame para que las muestras estén en las filas y los genes en las columnas
    genes_transpuesto = genes.transpose()

    # Renombrar los índices de las muestras con un formato 'sample_1', 'sample_2', ..., 'sample_n'
    genes_transpuesto.rename(index={key: f"sample_{key + 1}" for key in range(len(table))}, inplace=True)

    # Crear un DataFrame de metadatos, asignando condiciones y grupos a cada muestra
    df_meta = pd.DataFrame({'condicion': ["A", "B", "A", "B"],
                            'grupo': ["X", "X", "Y", "Y"]},
                           index=genes_transpuesto.index)

    # Limpiar los genes que tienen menos de 10 lecturas totales en todas las muestras
    genes_to_keep = genes_transpuesto.columns[genes_transpuesto.sum(axis=0) >= 10]
    genes_clean = genes_transpuesto[genes_to_keep]

    return genes_clean, df_meta

def read_table(archivo):
    """
    Función para leer un archivo de expresión génica y extraer la columna de lecturas de genes.
    
    Parámetros:
    archivo (str): Ruta del archivo que se va a leer.

    Retorna:
    Series: Una serie de pandas con los valores de la columna "Unique gene reads" del archivo.
    """
    df = pd.read_csv(archivo, sep='\t')
    sample = pd.Series(data=df["Unique gene reads"], copy=False)
    return sample
