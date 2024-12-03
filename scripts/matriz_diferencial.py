import pandas as pd
import seaborn as sb
import numpy as np

NH4_1 = pd.read_excel('../data/EANpec1_NH4_N2/GSM1573196_Batch_1_EAN1pec_NH4.xlsx')
N2_1 = pd.read_excel('../data/EANpec1_NH4_N2/GSM1573197_Batch_1_EAN1pec_N2.xlsx')

#Se rearregla a dos dimensiones el vector de RPKMs de NH4
#a dos dimensiones para después restarle cada uno de los
#valores de N2

Matriz_diferencial = NH4_1['RPKM'].values[:,None] - N2_1['RPKM'].values

sb.heatmap(data = Matriz_diferencial,cmap = 'vlag')
