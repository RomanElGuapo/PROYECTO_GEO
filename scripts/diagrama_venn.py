import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

data_frame_N2 = pd.read_csv('data/gene_expression_N2.txt', sep='\t')
data_frame_N2 = data_frame_N2.fillna(0)
RPKM_1_N2 = pd.Series(data_frame_N2['RPKM'])

data_frame_NH4 = pd.read_csv('data/gene_expression_NH4.txt', sep='\t')
data_frame_NH4 = data_frame_NH4.fillna(0)
RPKM_1_NH4 = pd.Series(data_frame_NH4['RPKM'])

df_1 = pd.DataFrame({'RPKM_1_N2':RPKM_1_N2,
                    'RPKM_1_NH4':RPKM_1_NH4})

region_df = pd.read_csv('data/gene_region_N2.txt', sep='\t')
#print(region_df)
region_NH4_df =pd.read_csv('data/gene_region_NH4.txt', sep='\t')
#print(region_NH4_df)

# Esta solo es una comprobación de que ambos data frames contienen las mismas regiones.
print(region_df.equals(region_NH4_df))

# Comprobación de que dentro del mismo data frame, las regiones son iguales
print(region_df.iloc[:, 0].equals(region_df.iloc[:, 1]))
print(region_df.iloc[:, 1].equals(region_df.iloc[:, 2]))
print(region_df.iloc[:, 2].equals(region_df.iloc[:, 0]))

intersection = []
N2 = []
NH4 = []

for i in df_1.iloc[:,0].index:
  if df_1.iloc[i, 0] != 0:
    N2.append(df_1.iloc[i,0])
    continue
  if df_1.iloc[i, 1] != 0:
    NH4.append(df_1.iloc[i,1])
    continue
  if df_1.iloc[i, 1] == df_1.iloc[i, 0]:
    intersection.append(df_1.iloc[i,0])

print(intersection)
print(N2)
print(NH4)

# Esta parte del código solamente es para comprobar la longitud de las cadenas
# La suma de la longitud de las cadenas debe ser igual a la longitud de una columna del dataframe original (7,191)

len = __builtins__.len

len_intersection = (len(intersection))
len_N2 = (len(N2))
len_NH4 = (len(NH4))

print(len_N2)
print(len_intersection)
print(len_NH4)

venn2((len_N2, len_NH4, len_intersection), set_labels=('NH2', 'NH4'))
plt.show()