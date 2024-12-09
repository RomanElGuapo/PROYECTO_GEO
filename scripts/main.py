import os
import analisis_multifactorial
import limpieza_archivos
import heatmap
import unifactorial
import matplotlib.pyplot as plt
import argparse

def parse_arguments():
    """
    Función que configura y parsea los argumentos de línea de comandos.

    Retorna:
    argparse.Namespace: Un objeto con los valores de los argumentos proporcionados 
    por el usuario al ejecutar el script.
    """

    # Crear un parser para la línea de comandos
    parser = argparse.ArgumentParser(description="Programa de análisis de expresión diferencial")

    # Definir argumentos mutuamente excluyentes para elegir entre análisis multifactorial o unifactorial
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--multifactorial', action='store_true', help='Realizar análisis por grupo y condición')
    group.add_argument('--unifactorial', action='store_true', help='Realizar análisis solo por condición')

    # Definir los argumentos para los archivos de expresión génica
    parser.add_argument('-1A', type=str, dest='archivo_1A', help='Archivo para grupo 1, condición A', required=True)
    parser.add_argument('-1B', type=str, dest='archivo_1B', help='Archivo para grupo 1, condición B', required=True)
    parser.add_argument('-2A', type=str, dest='archivo_2A', help='Archivo para grupo 2, condición A', required=True)
    parser.add_argument('-2B', type=str, dest='archivo_2B', help='Archivo para grupo 2, condición B', required=True)

    # Parsear los argumentos proporcionados en la línea de comandos
    return parser.parse_args()

if __name__ == "__main__":
    # Parsear los argumentos de la línea de comandos
    args = parse_arguments()
    OUT_PATH = './output/'
    # Verifica si la carpeta ya existe
    if os.path.exists(OUT_PATH):
        # Elimina la carpeta existente y su contenido
        shutil.rmtree(OUT_PATH)
    
    # Crea la carpeta nuevamente
    os.makedirs(OUT_PATH)

    # Realizar la limpieza de los archivos de entrada
    genes_df, df_meta = limpieza_archivos.limpieza_archivos(args.archivo_1A, args.archivo_1B, args.archivo_2A, args.archivo_2B)

    # Si se seleccionó el análisis multifactorial
    if args.multifactorial:
        # Realizar el análisis multifactorial
        dds, ds_B_vs_A, ds_Y_vs_X = analisis_multifactorial.analisis_multifactorial(genes_df, df_meta, OUT_PATH)
        
        # Generar y guardar los gráficos MA para condiciones y grupos
        ds_B_vs_A.plot_MA(s=20)
        plt.savefig(OUT_PATH + "MA_CONDICIONES.jpg", bbox_inches='tight')
        
        ds_Y_vs_X.plot_MA(s=20)
        plt.savefig(OUT_PATH + "MA_GRUPOS.jpg", bbox_inches='tight')
        
        # Generar y guardar los mapas de calor para condiciones y grupos
        heatmap.heatmap(dds, ds_B_vs_A)
        plt.savefig(OUT_PATH + "HEATMAP_CONDICIONES.jpg", bbox_inches='tight')
        
        heatmap.heatmap(dds, ds_Y_vs_X)
        plt.savefig(OUT_PATH + "HEATMAP_GRUPOS.jpg", bbox_inches='tight')
      
    # Si se seleccionó el análisis unifactorial
    if args.unifactorial:
        # Realizar el análisis unifactorial
        dds, ds = unifactorial.analisis_unifactorial(genes_df, df_meta, OUT_PATH)
        
        # Generar y guardar el gráfico MA para condiciones
        ds.plot_MA(s=20)
        plt.savefig(OUT_PATH + "MA_CONDICIONES.jpg", bbox_inches='tight')
        
        # Generar y guardar el mapa de calor para condiciones
        heatmap.heatmap(dds, ds)
        plt.savefig(OUT_PATH + "HEATMAP_CONDICIONES.jpg", bbox_inches='tight')
