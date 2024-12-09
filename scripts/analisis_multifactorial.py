#SCRIPT DE ANÁLISIS MULTIFACTORIAL

import pydeseq2
from pydeseq2.dds import DeseqDataSet
from pydeseq2.default_inference import DefaultInference
from pydeseq2.ds import DeseqStats
import numpy as np
import pandas as pd

def analisis_multifactorial(genes_df, df_meta, OUT_PATH):
    """
    Función para realizar un análisis multifactorial utilizando DESeq2.
    
    Esta función realiza un análisis de expresión diferencial utilizando la librería `pydeseq2` 
    para identificar genes diferencialmente expresados entre distintos grupos y condiciones, 
    y guarda los resultados en archivos de texto.

    Parámetros:
    genes_df (DataFrame): DataFrame que contiene los conteos de los genes (filas como genes, columnas como muestras).
    df_meta (DataFrame): DataFrame que contiene la metadata de las muestras (filas como muestras, columnas como variables).
    OUT_PATH (str): Ruta del directorio donde se guardarán los resultados en archivos de texto.

    Retorna:
    tuple: Un tuple que contiene tres objetos:
        - dds (DeseqDataSet): El objeto `DeseqDataSet` creado con los datos de entrada.
        - ds_B_vs_A (DeseqStats): El objeto `DeseqStats` con los resultados para el contraste "condición B vs A".
        - ds_Y_vs_X (DeseqStats): El objeto `DeseqStats` con los resultados para el contraste "grupo Y vs X".
    """
    
    # Crear el objeto DeseqDataSet con los datos de genes y metadata
    dds = DeseqDataSet(
        counts=genes_df,  # Datos de expresión de los genes
        metadata=df_meta,  # Metadata de las muestras
        design_factors=['grupo', 'condicion'],  # Factores de diseño (variables del experimento)
        inference=DefaultInference(n_cpus=8)  # Configuración para realizar inferencia en 8 hilos
    )

    # Realizar el análisis DESeq2
    dds.deseq2()

    # Realizar el contraste "condición B vs A"
    ds_B_vs_A = DeseqStats(dds, contrast=["condicion", "B", "A"])
    ds_B_vs_A.summary()  # Resumen de los resultados para este contraste
    ds_B_vs_A.results_df  # DataFrame con los resultados del contraste
    ds_B_vs_A.lfc_shrink(coeff="condicion_B_vs_A")  # Realizar el ajuste de reducción del log2 fold change

    # Guardar los resultados del contraste "B vs A" en un archivo de texto
    with open(OUT_PATH + "ds_B_vs_A_results_df.txt", "w") as archivo:
        print(ds_B_vs_A.results_df, file=archivo)

    # Realizar el contraste "grupo Y vs X"
    ds_Y_vs_X = DeseqStats(dds, contrast=["grupo", "Y", "X"])
    ds_Y_vs_X.summary()  # Resumen de los resultados para este contraste
    ds_Y_vs_X.results_df  # DataFrame con los resultados del contraste
    ds_Y_vs_X.lfc_shrink(coeff="grupo_Y_vs_X")  # Realizar el ajuste de reducción del log2 fold change

    # Guardar los resultados del contraste "Y vs X" en un archivo de texto
    with open(OUT_PATH + "ds_Y_vs_X_results_df.txt", "w") as archivo:
        print(ds_Y_vs_X.results_df, file=archivo)

    # Retornar los objetos para su posible uso posterior
    return dds, ds_B_vs_A, ds_Y_vs_X
