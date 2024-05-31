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

