import pydeseq2
from pydeseq2.dds import DeseqDataSet
from pydeseq2.default_inference import DefaultInference
from pydeseq2.ds import DeseqStats
import numpy as np
import pandas as pd

def analisis_unifactorial(genes_df, meta_df,OUT_PATH):
  inference = DefaultInference(n_cpus=8)
  dds = DeseqDataSet(
      counts=genes_df,
      metadata=meta_df,
      design_factors=['condicion'],
      refit_cooks=True,
      inference=inference,
  )
  dds.deseq2() 
  ds = DeseqStats(dds, contrast=["condicion", "B", "A"], inference=inference)
  ds.summary()
  results_df = ds.results_df
  ds.lfc_shrink(coeff="condicion_B_vs_A")
  with open(OUT_PATH+"ds_results_df.txt", "w") as archivo:
    # Usar print y redirigir la salida al archivo
    print(ds.results_df, file=archivo)

  return dds, ds