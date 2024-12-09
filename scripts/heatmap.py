import numpy as np
import seaborn as sns
import pandas as pd

def heatmap(dds, ds):

  """
  Función para generar un mapa de calor (heatmap) de los genes significativos
  basado en los valores de log(p-value) obtenidos en un análisis de expresión diferencial.

  Esta función selecciona los genes que presentan un valor p significativo (p < 0.05)
  y genera un mapa de calor usando las expresiones normalizadas de estos genes.

  Parámetros:
  dds (DeseqDataSet): El objeto `DeseqDataSet` que contiene los datos de expresión de los genes.
  ds (DeseqStats): El objeto `DeseqStats` que contiene los resultados del análisis de expresión diferencial
                      (incluyendo valores p, fold changes, etc.).

  Retorna:
  seaborn.axisgrid.ClusterGrid: Un objeto `ClusterGrid` que contiene el mapa de calor generado.
  """

  # Calcular el logaritmo base 1 del valor p de las cuentas normalizadas (log(p-value))
  dds.layers['loglp'] = np.log1p(dds.layers['normed_counts'])
  
  # Filtrar los genes con p-value < 0.05 para seleccionar los significativos
  significante = ds.results_df[ds.results_df['pvalue'] < 0.05]
  
  # Filtrar las muestras correspondientes a los genes significativos
  dds_significantes = dds[:, significante.index]

  # Crear un DataFrame con las cuentas normalizadas logarítmicas para los genes significativos
  grapher = pd.DataFrame(dds_significantes.layers['loglp'].T,
                        index=dds_significantes.var_names, columns=dds_significantes.obs_names)
  
  # Generar el mapa de calor usando seaborn, con agrupamiento jerárquico (clustermap)
  graph = sns.clustermap(grapher, z_score=0, cmap='RdYlBu_r')
  
  # Retornar el objeto generado que contiene el mapa de calor
  return graph
