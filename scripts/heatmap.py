import numpy as np
import seaborn as sns
import pandas as pd

def heatmap(dds, ds):
  dds.layers['loglp'] = np.log1p(dds.layers['normed_counts'])
  significante = ds.results_df[ds.results_df['pvalue'] < 0.05]
  dds_significantes = dds[:, significante.index]
  grapher = pd.DataFrame(dds_significantes.layers['loglp'].T,
                       index=dds_significantes.var_names, columns=dds_significantes.obs_names)
  graph = sns.clustermap(grapher, z_score=0, cmap='RdYlBu_r')
  return graph
