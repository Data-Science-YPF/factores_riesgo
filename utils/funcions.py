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