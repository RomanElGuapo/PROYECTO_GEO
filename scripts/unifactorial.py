import pydeseq2
from pydeseq2.dds import DeseqDataSet
from pydeseq2.default_inference import DefaultInference
from pydeseq2.ds import DeseqStats
import numpy as np
import pandas as pd

def analisis_unifactorial(genes_df, meta_df,OUT_PATH):

  """
    Función para realizar un análisis unifactorial de expresión diferencial utilizando DESeq2.

    Este análisis compara las condiciones de dos grupos (por ejemplo, "A" y "B") para identificar genes
    diferencialmente expresados, y guarda los resultados en un archivo de texto.

    Parámetros:
    genes_df (DataFrame): DataFrame que contiene los conteos de los genes (filas como genes, columnas como muestras).
    meta_df (DataFrame): DataFrame que contiene los metadatos de las muestras (filas como muestras, columnas como variables experimentales).
    OUT_PATH (str): Ruta del directorio donde se guardará el archivo con los resultados.

    Retorna:
    tuple: Un tuple que contiene dos elementos:
        - dds (DeseqDataSet): El objeto `DeseqDataSet` creado con los datos de entrada.
        - ds (DeseqStats): El objeto `DeseqStats` que contiene los resultados del análisis de expresión diferencial.
    """
  # Inicializar la inferencia con 8 CPUs
  inference = DefaultInference(n_cpus=8)

  # Crear el objeto DeseqDataSet con los datos de genes y metadata
  dds = DeseqDataSet(
      counts=genes_df, # Datos de expresión de los genes
      metadata=meta_df, # Metadata de las muestras
      design_factors=['condicion'], # Factor de diseño (condición experimental)
      refit_cooks=True,  # Refitar los valores de Cook's distance para control de outliers
      inference=inference, # Inferencia utilizando el número de CPUs especificado
  )

  # Realizar el análisis DESeq2
  dds.deseq2() 

  # Realizar el contraste "condición B vs A"
  ds = DeseqStats(dds, contrast=["condicion", "B", "A"], inference=inference)
  ds.summary() # Mostrar un resumen de los resultados del contraste
  results_df = ds.results_df # Obtener el DataFrame con los resultados del contraste

  # Realizar el ajuste de reducción del log2 fold change
  ds.lfc_shrink(coeff="condicion_B_vs_A")

  # Guardar los resultados en un archivo de texto en la ruta especificada
  with open(OUT_PATH+"ds_results_df.txt", "w") as archivo:
    # Usar print y redirigir la salida al archivo
    print(ds.results_df, file=archivo)

  # Retornar los objetos para su posible uso posterior
  return dds, ds