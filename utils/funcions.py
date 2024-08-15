import pandas as pd


# Calculo de nulos y porcentaje, devuelve un DataFrame
def calcular_nulos_y_porcentaje(df):
    nulos_por_columna = df.isnull().sum()
    total_filas = len(df)
    porcentaje_nulos = (nulos_por_columna / total_filas) * 100
    porcentaje_nulos_redondeado = porcentaje_nulos.round(2).astype(str) + '%'

    resultados = pd.DataFrame({
        'Nulos': nulos_por_columna,
        'Porcentaje': porcentaje_nulos_redondeado})
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


# Muestra los distintos valores que toma la columna pasada como parámetro
# Si se proporciona un diccionario para reemplazar valores codificados
# se muestra el valor correspondiente
def mostrar_valores_columna(df, columna, diccionario_reemplazo=None):
    # Obtener los valores únicos y sus conteos
    conteo_valores = df[columna].value_counts(dropna=False)
    total_valores = len(df[columna])

    # Si hay diccionario de reemplazo, se usan esos valores
    if diccionario_reemplazo:
        valores_reemplazados = {val: diccionario_reemplazo.get(val, val) for val in conteo_valores.index}
        conteo_valores.index = conteo_valores.index.map(lambda x: valores_reemplazados.get(x, x))

    # Calcular la proporción
    proporciones = (conteo_valores / total_valores) * 100

    # Crear el DataFrame de resultados
    resultados = pd.DataFrame({
        'Valor': conteo_valores.index,
        'Cantidad': conteo_valores.values,
        'Proporción (%)': proporciones.round(2).astype(str) + '%'
    }).reset_index(drop=True)
 
    return resultados


# Funcion para variables numericas continuas
# Forma 2 grupos, uno de NaN y otro del resto de valores
# calcula la cantidad y proporcion de cada grupo y los muestra
def mostrar_valores_columna_numerica(df, columna):
    # Obtener el total de valores en la columna
    total_valores = len(df[columna])

    # Contar los valores NaN y los valores no NaN
    valores_nan = df[columna].isna().sum()
    valores_no_nan = total_valores - valores_nan

    # Calcular la proporción
    nan_proporcion = (valores_nan / total_valores) * 100
    no_nan_proporcion = (valores_no_nan / total_valores) * 100

    # Crear el DataFrame de resultados
    resultados = pd.DataFrame({
        'Valor': ['NaN', 'Otros'],
        'Cantidad': [valores_nan, valores_no_nan],
        'Proporción (%)': [f"{nan_proporcion:.2f}%", f"{no_nan_proporcion:.2f}%"]
    })
 
    return resultados

# Definir una funcion para eliminar los outliers
def eliminar_outliers(df, cols_to_check):
    df_clean = df.copy()

    for col in cols_to_check:
        # Calcular los percentiles 25 y 75 (primer y tercer cuartil)
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        # Calcular el rango intercuartil (IQR)
        IQR = Q3 - Q1
        # Definir los límites para detectar outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Filtrar el DataFrame para eliminar los registros con outliers
        df_clean = df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)]

    return df_clean

# Función para calcular el porcentaje de outliers en una columna
def calcular_porcentaje_outliers(col):
    Q1 = col.quantile(0.25)
    Q3 = col.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = col[(col < lower_bound) | (col > upper_bound)]
    porcentaje_outliers = (len(outliers) / len(col)) * 100
    return porcentaje_outliers, len(outliers)

def eliminar_outliers2(df, cols_to_check):
    """
    Elimina registros que contengan outliers en al menos una de las columnas especificadas.
    
    Parameters:
    df (pd.DataFrame): DataFrame en el que se buscarán y eliminarán outliers.
    cols_to_check (list): Lista de nombres de columnas en las que se verificarán outliers.

    Returns:
    pd.DataFrame: DataFrame sin registros que contienen outliers en las columnas especificadas.
    """
    df_clean = df.copy()
    outliers_mask = pd.Series([False] * len(df_clean))  # Máscara booleana inicializada en False

    for col in cols_to_check:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Actualizar la máscara booleana si hay outliers en la columna actual
        outliers_mask = outliers_mask | (df_clean[col] < lower_bound) | (df_clean[col] > upper_bound)

    # Filtrar el DataFrame para mantener solo las filas que no son outliers
    df_clean = df_clean[~outliers_mask]

    return df_clean
