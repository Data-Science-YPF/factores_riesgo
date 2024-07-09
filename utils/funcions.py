import pandas as pd


# Calculo de nulos y porcentaje, devuelve un DataFrame
def calcular_nulos_y_porcentaje(df):
    nulos_por_columna = df.isnull().sum()
    total_filas = len(df)
    porcentaje_nulos = (nulos_por_columna / total_filas) * 100
    resultados = pd.DataFrame({
        'Nulos': nulos_por_columna,
        'Porcentaje': porcentaje_nulos})
    return resultados


# Función para convertir a snake_case
def to_snake_case(column_name):
    return column_name.strip().lower().replace(' ', '_')


# Calculo de cantidad de tipos de tabaco fumado
# Por cada tipo de tabaco respondido como '1' (Sí) suma 1 al total
def calcular_tipos_tabaco(df, columnas):
    # Contar los 1s en el subconjunto de columnas
    return df[columnas].apply(lambda row: (row == 1).sum(), axis=1)


# Renombrar las columnas de un DataFrame
def rename_df_to_snake_Case(df):
    df.columns = [to_snake_case(col) for col in df.columns]


# Almacenamos el value_counts() de cada columna en un diccionario
# Formato del diccionario {nombre_columna: resultado_value_counts}
def calcular_valores_columna(df):
    value_counts_dict = {col: df[col].value_counts(normalize=True) for col in df.columns}

    # Imprimimos los resultados
    for col, counts in value_counts_dict.items():
        print(f"Proporción de valores para la columna {col}:\n{counts}\n")

def filtrar_columnas(dataset, columnas_interes):
    # Verificar que todas las columnas en column_list existan en el DataFrame original
    for columna in columnas_interes:
        if columna not in dataset.columns:
            raise ValueError(f"La columna '{columna}' no existe en el DataFrame original.")
    
    # Crear el DataFrame derivado seleccionando solo las columnas especificadas
    dataframe_filtrado = dataset[columnas_interes].copy()
    
    return dataframe_filtrado

def obtener_valores_nulos_con_id(df, columna_interes, columnas_objetivo):
    # Filtrar las filas donde la columna de interés tiene valores nulos
    filas_nulas = df[df[columna_interes].isna()]   
    # Obtener los valores de las columnas objetivo para estas filas
    valores_objetivo = filas_nulas[columnas_objetivo] 
    return valores_objetivo