import pandas as pd
import seaborn as sb
import numpy as np
<<<<<<< HEAD
from scipy import stats
=======
>>>>>>> 63966eac1c69a7b71f8d0088f46904a2273c7344

NH4_1 = pd.read_excel('GSM1573196_Batch_1_EAN1pec_NH4.xlsx')
N2_1 = pd.read_excel('GSM1573197_Batch_1_EAN1pec_N2.xlsx')

#Se rearregla a dos dimensiones el vector de RPKMs de NH4
#a dos dimensiones para después restarle cada uno de los
#valores de N2

Matriz_diferencial = NH4_1['RPKM'].values[:,None] - N2_1['RPKM'].values

<<<<<<< HEAD
sb.heatmap(data = Matriz_diferencial,cmap = 'vlag')
=======
sb.heatmap(data = Matriz_diferencial,cmap = 'vlag')
>>>>>>> 63966eac1c69a7b71f8d0088f46904a2273c7344
