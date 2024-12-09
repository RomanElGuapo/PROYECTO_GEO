# Introducción

Este programa está diseñado para realizar un análisis de expresión diferencial en datos genéticos, permitiendo al usuario realizar análisis unifactoriales o multifactoriales. El análisis incluye la comparación de diferentes condiciones experimentales (por ejemplo, condición A vs. condición B) y la identificación de genes diferencialmente expresados. Los resultados se presentan mediante gráficos MA y mapas de calor (heatmaps), que se guardan en archivos de imagen para facilitar su interpretación.

# Requisitos

- **Python 3.6 o superior**.
- Las siguientes librerías de Python:
    - `pydeseq2`: Para el análisis de expresión diferencial.
    - `numpy`, `pandas`: Para la manipulación de datos.
    - `seaborn`, `matplotlib`: Para la visualización de datos.
    - `argparse`: Para la gestión de argumentos en línea de comandos.

# Instalación

Para instalar las dependencias necesarias, puede usar el siguiente comando:
```
pip install pydeseq2 numpy pandas seaborn matplotlib argparse
```

# Estructura del Proyecto

El código está compuesto por varios módulos:

- **limpieza_archivos.py**: Realiza la limpieza y preparación de los archivos de entrada.
- **analisis_multifactorial.py**: Realiza el análisis de expresión diferencial multifactorial (por grupo y condición).
- **unifactorial.py**: Realiza el análisis unifactorial (solo por condición).
- **heatmap.py**: Genera los mapas de calor (heatmaps) para la visualización de los resultados.
- **main.py**: El script principal que ejecuta el programa.

# Ejecución del Programa

El script principal `main.py` permite ejecutar los análisis desde la línea de comandos. A continuación se describe cómo usar el programa:

1. **Preparar los archivos de entrada:**
    
    - Se requieren 4 archivos que contengan los datos de expresión génica para las dos condiciones experimentales (A y B) y dos grupos experimentales (X y Y).
    - Los archivos deben estar en formato `.txt` o `.csv`, con los conteos de expresión génica por muestra. Asegúrese de que cada archivo contenga una columna llamada `Unique gene reads` con los datos de expresión para cada gen.
2. **Sintaxis de la línea de comandos:**
    

El programa se ejecuta desde la línea de comandos con los siguientes parámetros:
```
python main.py -1A archivo_1A.txt -1B archivo_1B.txt -2A archivo_2A.txt -2B archivo_2B.txt --multifactorial
```
ó
```
python main.py -1A archivo_1A.txt -1B archivo_1B.txt -2A archivo_2A.txt -2B archivo_2B.txt --unifactorial
```

**Argumentos:**

- `-1A`: Archivo de datos para el grupo 1, condición A.
- `-1B`: Archivo de datos para el grupo 1, condición B.
- `-2A`: Archivo de datos para el grupo 2, condición A.
- `-2B`: Archivo de datos para el grupo 2, condición B.
- `--multifactorial`: Realiza un análisis multifactorial que compara grupos y condiciones.
- `--unifactorial`: Realiza un análisis unifactorial que compara solo las condiciones.

**Nota:** El uso de `--multifactorial` y `--unifactorial` es excluyente. Solo puede elegir uno de los dos análisis a la vez.

3. **Salida de resultados:**

El programa genera los siguientes resultados y los guarda en el directorio `./output/`:

- **Gráficos MA:**
    
    - `MA_CONDICIONES.jpg`: Gráfico MA para la comparación entre las condiciones (A vs. B).
    - `MA_GRUPOS.jpg`: Gráfico MA para la comparación entre los grupos (X vs. Y).
- **Mapas de calor (Heatmaps):**
    
    - `HEATMAP_CONDICIONES.jpg`: Mapa de calor para los genes significativos entre las condiciones.
    - `HEATMAP_GRUPOS.jpg`: Mapa de calor para los genes significativos entre los grupos.

4. **Descripción de los resultados:**

- **Gráfico MA (MA plot):**
    
    - El gráfico MA muestra la relación entre el log2 del fold change y el promedio de la expresión para cada gen. Es útil para identificar genes diferencialmente expresados entre las condiciones o grupos.
- **Mapa de calor (Heatmap):**
    
    - El mapa de calor visualiza los patrones de expresión de los genes significativos entre las condiciones o grupos. Los genes están representados en filas y las muestras en columnas.

# Funciones del Programa

1. **`parse_arguments()`**:
    
    - Esta función gestiona los argumentos pasados por línea de comandos. Asegura que el usuario especifique correctamente los archivos de entrada y el tipo de análisis a realizar.
2. **`limpieza_archivos.limpieza_archivos()`**:
    
    - Limpia y organiza los archivos de entrada. Se asegura de que solo los genes con al menos 10 lecturas sean conservados para el análisis. También organiza los datos en un formato adecuado para DESeq2.
3. **`analisis_multifactorial.analisis_multifactorial()`**:
    
    - Realiza un análisis multifactorial de expresión diferencial utilizando los datos de los genes y los metadatos. Compara las condiciones y los grupos, generando resultados estadísticos y gráficos.
4. **`unifactorial.analisis_unifactorial()`**:
    
    - Realiza un análisis unifactorial de expresión diferencial. Solo compara las condiciones (por ejemplo, A vs. B).
5. **`heatmap.heatmap()`**:
    
    - Genera mapas de calor para visualizar los resultados del análisis de expresión diferencial. Los mapas de calor se generan para las condiciones o grupos, según el análisis realizado.

# Ejemplo de Ejecución

```
python .\main.py --multifactorial -1A ..\data\GSM1493956_Root_Nodule_NaPlus1.txt -1B ..\data\GSM1493959_Root_Nodule_NaMinus1.txt -2A ..\data\GSM1493957_Root_Nodule_NaPlus2.txt -2B ..\data\GSM1493960_Root_Nodule_NaMinus2.txt
```

Este comando realizará un análisis multifactorial utilizando los archivos proporcionados para los dos grupos y dos condiciones. Los resultados, incluidos los gráficos MA y los mapas de calor, se guardarán en el directorio `./output/`.

# Consideraciones

- Asegúrese de que los archivos de datos de entrada estén en el formato adecuado y contengan los datos correctos.
- El programa crea un directorio `./output/` para guardar los resultados. Si el directorio ya existe, los archivos se sobrescribirán.
- El análisis multifactorial requiere que los datos contengan información sobre grupos y condiciones. Si desea realizar solo un análisis por condición, use el análisis unifactorial.

# Soporte

Si tiene problemas o preguntas sobre el uso del programa, puede contactar al equipo de soporte o consultar la documentación adicional disponible en el repositorio del código.

---

Este manual proporciona las instrucciones completas para ejecutar y utilizar el programa de análisis de expresión diferencial, con detalles sobre la preparación de los datos, la ejecución desde la línea de comandos y la interpretación de los resultados.
