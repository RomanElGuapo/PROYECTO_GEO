import os
import analisis_multifactorial
import limpieza_archivos
import heatmap
import unifactorial
import matplotlib.pyplot as plt
import argparse

def parse_arguments():
    # Crear un parser
    parser = argparse.ArgumentParser(description="Programa de análisis de expresion diferencial")

    # Definir argumentos

        # Crear un grupo mutuamente excluyente
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--multifactorial', action='store_true', help='Hacer el analisis por grupo y condición')
    group.add_argument('--unifactorial', action='store_true', help='Hacer el análisis solo por condicion')

    parser.add_argument('-1A', type=str, dest='archivo_1A',help='Archivo grupo1, condicion A',required = True)
    parser.add_argument('-1B', type=str, dest='archivo_1B',help='Archivo grupo1, condicion B',required = True)
    parser.add_argument('-2A', type=str, dest='archivo_2A',help='Archivo grupo2, condicion A',required = True)
    parser.add_argument('-2B', type=str, dest='archivo_2B',help='Archivo grupo2, condicion B',required = True)

    return parser.parse_args()

if __name__ == "__main__":

    args = parse_arguments()
    
    OUT_PATH = "./output/"
    os.makedirs(OUT_PATH, exist_ok=True)

    genes_df, df_meta = limpieza_archivos.limpieza_archivos(args.archivo_1A,
                                                            args.archivo_1B,
                                                            args.archivo_2A,
                                                            args.archivo_2B)
    if args.multifactorial:
      
      dds, ds_B_vs_A, ds_Y_vs_X = analisis_multifactorial.analisis_multifactorial(genes_df,df_meta,OUT_PATH)
      ds_B_vs_A.plot_MA(s=20)
      plt.savefig(OUT_PATH + "MA_CONDICIONES.jpg", bbox_inches='tight')
      ds_Y_vs_X.plot_MA(s=20)
      plt.savefig(OUT_PATH + "MA_GRUPOS.jpg", bbox_inches='tight')
      heatmap.heatmap(dds, ds_B_vs_A)
      plt.savefig(OUT_PATH + "HEATMAP_CONDICIONES.jpg", bbox_inches='tight')
      heatmap.heatmap(dds, ds_Y_vs_X)
      plt.savefig(OUT_PATH + "HEATMAP_GRUPOS.jpg", bbox_inches='tight')
      
    if args.unifactorial:
      dds, ds = unifactorial.analisis_unifactorial(genes_df, df_meta,OUT_PATH)
      ds.plot_MA(s=20)
      plt.savefig(OUT_PATH + "MA_CONDICIONES.jpg", bbox_inches='tight')
      heatmap.heatmap(dds, ds)
      plt.savefig(OUT_PATH + "HEATMAP_CONDICIONES.jpg", bbox_inches='tight')