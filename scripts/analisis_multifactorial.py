#SCRIPT DE ANÁLISIS MULTIFACTORIAL
import pydeseq2
from pydeseq2.dds import DeseqDataSet
from pydeseq2.default_inference import DefaultInference
from pydeseq2.ds import DeseqStats
import numpy as np
import pandas as pd

def analisis_multifactorial(genes_df,df_meta,OUT_PATH):
  dds = DeseqDataSet(
      counts=genes_df,
      metadata=df_meta,
      design_factors= ['grupo','condicion'],
      inference=DefaultInference(n_cpus=8),)

  dds.deseq2()

  ds_B_vs_A = DeseqStats(dds, contrast=["condicion", "B", "A"])
  ds_B_vs_A.summary()
  ds_B_vs_A.results_df
  ds_B_vs_A.lfc_shrink(coeff="condicion_B_vs_A")
  
  with open(OUT_PATH+"ds_B_vs_A_results_df.txt", "w") as archivo:
      # Usar print y redirigir la salida al archivo
      print(ds_B_vs_A.results_df, file=archivo)

  ds_Y_vs_X = DeseqStats(dds, contrast=["grupo", "Y", "X"])
  ds_Y_vs_X.summary()
  ds_Y_vs_X.results_df
  ds_Y_vs_X.lfc_shrink(coeff="grupo_Y_vs_X")

  with open(OUT_PATH+"ds_Y_vs_X_results_df.txt", "w") as archivo:
      # Usar print y redirigir la salida al archivo
      print(ds_Y_vs_X.results_df, file=archivo)

  return dds, ds_B_vs_A, ds_Y_vs_X