import pandas as pd

NH4_1 = pd.read_excel('../data/EANpec1_NH4_N2/GSM1573196_Batch_1_EAN1pec_NH4.xlsx')
N2_1 = pd.read_excel('../data/EANpec1_NH4_N2/GSM1573197_Batch_1_EAN1pec_N2.xlsx')

NH4_1['RPKM'] - N2_1['RPKM']