import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data_frame_N2 = pd.read_csv('data/gene_expression_N2.txt', sep='\t')
data_frame_N2 = data_frame_N2.fillna(0)
RPKM_1_N2 = pd.Series(data_frame_N2['RPKM'])

data_frame_NH4 = pd.read_csv('data/gene_expression_NH4.txt', sep='\t')
data_frame_NH4 = data_frame_NH4.fillna(0)
RPKM_1_NH4 = pd.Series(data_frame_NH4['RPKM'])

df_1 = pd.DataFrame({'RPKM_1_N2':RPKM_1_N2,
                    'RPKM_1_NH4':RPKM_1_NH4})

pca = PCA(n_components=2)
pca_results = pca.fit_transform(df_1)

data_pca = pd.DataFrame(pca_results, columns=['PC1', 'PC2'])

fig, ax = plt.subplots()
scatter = ax.scatter(x=data_pca.PC1, y=data_pca.PC2, c='blue')

ax.set_title('PCA')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2') 

ax.grid("TRUE")
plt.show()

RPKM_2_N2 = pd.Series(data_frame_N2['RPKM.1'])

RPKM_2_NH4 = pd.Series(data_frame_NH4['RPKM.1'])

df_2 = pd.DataFrame({'RPKM_2_N2':RPKM_2_N2,
                     'RPKM_2_NH4': RPKM_2_NH4})

pca = PCA(n_components=2)
pca_results = pca.fit_transform(df_2)

data_pca = pd.DataFrame(pca_results, columns=['PC1', 'PC2'])

fig, ax = plt.subplots()
scatter = ax.scatter(x=data_pca.PC1, y=data_pca.PC2, c='pink')

ax.set_title('PCA')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2') 

ax.grid("TRUE")
plt.show()

RPKM_3_N2 = pd.Series(data_frame_N2['RPKM'])

RPKM_3_NH4 = pd.Series(data_frame_NH4['RPKM'])

df_3 = pd.DataFrame({'RPKM_3_N2':RPKM_3_N2,
                    'RPKM_3_NH4':RPKM_3_NH4})

pca = PCA(n_components=2)
pca_results = pca.fit_transform(df_3)

data_pca = pd.DataFrame(pca_results, columns=['PC1', 'PC2'])
#print(data_pca)

fig, ax = plt.subplots()
scatter = ax.scatter(x=data_pca.PC1, y=data_pca.PC2, c='purple')

ax.set_title('PCA')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2') 

ax.grid("TRUE")
plt.show()

# PCA GENERAL: 

df_total = pd.DataFrame({'RPKM_1_N2':RPKM_1_N2,
                    'RPKM_1_NH4':RPKM_1_NH4, 
                         'RPKM_2_N2':RPKM_2_N2,
                     'RPKM_2_NH4': RPKM_2_NH4,
                        'RPKM_3_N2':RPKM_3_N2,
                    'RPKM_3_NH4':RPKM_3_NH4 })

pca = PCA(n_components=6)
pca_results = pca.fit_transform(df_total)

data_pca = pd.DataFrame(pca_results, columns=['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6'])
#print(data_pca)

fig, ax = plt.subplots()
scatter = ax.scatter(x=data_pca.PC1, y=data_pca.PC2, c='blue')
scatter = ax.scatter(x=data_pca.PC3, y=data_pca.PC4, c='pink')
scatter = ax.scatter(x=data_pca.PC5, y=data_pca.PC6, c='purple')

ax.set_title('PCA')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2') 

ax.grid("TRUE")
plt.show()