#Script de limpieza de archivos (POSIBLEMENTE SOLO PARA EL MULTIFACTOR)
import pandas as pd

def limpieza_archivos(file1A,file1B,file2A,file2B):

  files = [file1A,file1B,file2A,file2B]

  table = []

  for i in files:
    table.append(read_table(i))

  diccionario = dict(zip(range(len(table)), table))

  genes = pd.DataFrame(diccionario, index=diccionario[0].index,
                      columns=diccionario.keys())

  genes_transpuesto = genes.transpose()

  genes_transpuesto.rename(index={key: f"sample_{key + 1}" for key in range(len(table))}, inplace=True)

  # Segunda tabla (metadatos)
  df_meta = pd.DataFrame({'condicion': ["A", "B", "A", "B"],
                          'grupo': ["X", "X", "Y", "Y"]},
                        index=genes_transpuesto.index)

  #Limpieza de genes con menos de 10 lecturas
  genes_to_keep = genes_transpuesto.columns[genes_transpuesto.sum(axis=0) >= 10]
  genes_clean = genes_transpuesto[genes_to_keep]

  return genes_clean, df_meta

def read_table(archivo):
  df = pd.read_csv(archivo, sep = '\t')
  sample = pd.Series(data=df["Unique gene reads"], copy=False)
  return sample