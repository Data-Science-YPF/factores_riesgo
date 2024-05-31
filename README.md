# factores_riesgo
Este proyecto es parte del trabajo final para el curso de Data Science dictado por Fundación YPF - 2024

## Integrantes
* Casco
* Romina Torres
* Breide
* Cristin
* Yelos

## Datasets utilizados
Utilizaremos las bases de datos proporcionadas por el Indec para los años 2005 - 2009 - 2013 - 2018
https://www.indec.gob.ar/indec/web/Institucional-Indec-BasesDeDatos-2

## Estructura del repositorio
analisisBD.ipynb
README.txt

datasets - carpeta con los archivos correspondientes a todos los años
utils - carpeta con archivos de utilidad
    codificaciones.py - diccionarios correspondientes a toda la codificacion usada en los datasets
    functions.py - funciones creadas para el uso comun en todo el analisis 

## Organizacion del trabajo
Separe las columnas teniendo en cuenta el objetivo del tp como:
1. Predicción de Enfermedades Crónicas

Objetivo: Desarrollar un modelo predictivo para identificar individuos con alto riesgo de
desarrollar enfermedades crónicas (como hipertensión, diabetes, colesterol alto) basándose
en sus comportamientos y condiciones de vida.
Métodos: Clasificación usando algoritmos como regresión logística, random forest,
XGBoost, o redes neuronales.
Variables Relevantes: Preguntas de salud general, actividad física, consumo de tabaco,
alimentación, consumo de alcohol, mediciones antropométricas, y bioquímicas.

Nota:Las mediciones antropométricas y bioquímicas no se encuentran en las bases
de 2009 y 2013, por lo que no las inclui en los bloques temáticos.
Nota 2 : Siempre podemos cambiar el objetivo en el futuro, ahorita lo primordial sería
tener que entregar el martes 04/06. Podemos agregar más columnas a futuro si a
alguna le parece necesario o si capas se adapta a otro objetivo que planteemos.

-Bloques de columnas por temática:
● Identificacion y ubicacion [7] Columnas
● Características del encuestado [15]
● Salud general y actividad física [25]
● Tabaquismo [42]
● Hipertensión [20]
● Peso corporal [9]
● Alimentación [18]
● Colesterol [8]
● Consumo alcohol [23]
● Diabetes [19]

Para repartirnos los temas seria :
* Romina Torres:
Tabaquismo: 42 columnas
Total: 42 columnas

* Persona 2:
Salud general y actividad física: 25 columnas
Peso corporal: 9 columnas
Total: 25 + 9 = 34 columnas

* Persona 3:
Consumo de alcohol: 23 columnas
Identificación y ubicación: 7 columnas
Colesterol: 8 columnas
Total: 23 + 7 + 8 = 38 columnas

* Persona 4:
Hipertensión: 20 columnas
Características del encuestado: 15 columnas
Total: 20 + 15 = 35 columnas

* Persona 5:
Alimentación: 18 columnas
Diabetes: 19 columnas
Total: 18 + 19 = 37 columnas


—---------------------------------------------------------------------
Creo que la mejor forma de trabajar, es que cada una tome los tema/s que les corresponden
y:
1. A partir de la base de datos, cree un dataframe individual para cada tema
2. Elimine o conserve dentro de las tablas que le tocaron, las columnas que le
parezcan irrelevantes, siguiendo el objetivo
3. Renombre las columnas con nombres más fáciles de recordar o más descriptivos (recomiendo usar la funcion to_snake_case())
4. Estudie cómo se responden las preguntas, es decir, si los valores corresponden a
preguntas sí o no o ns/nc (no sabe/no contesta) o preguntas de altura o peso donde
la respuesta es un número. Y lo escriba en algún lado para que los demás tengan
una noción de esos datos sin tener que volver a ver la documentación de cero.
    Recomiendo usar un archivo por separado, detallando en un diccionario el codigo y el valor para futuras referencias.
    Recomiendo crear el detalle de cada variable en un archivo de documentacion, como este mismo README.txt
5. Sí hay categorías, como por ejemplo provincia o género o nivel de educación, etc.
Cambie las columnas del número de respuesta a directamente el nombre de la
categoría. (YO NO RECOMIENDO ESTO porque estos cambios son parte de la optimizacion del procesamiento)
6. Una vez realizadas las transformaciones de variable, analice el nivel de utilidad de
c/columna en base a si las respuestas son nulas porque algún índice era 0 por el
tipo de respuesta u otro factor. En ese caso, tenerlo anotado para discutirlo entre
todas, para decidir si sirve o no, o si rellenarlo como vimos en clase con algún valor
7. Una vez listo, me pasan las tablas de manera individual, en formato .csv y yo las
uno en una sola base de datos grande ya lista para que podamos hacer gráficos y
buscar relaciones entre columnas
