# factores_riesgo
Este proyecto es parte del trabajo final para el curso de Data Science dictado por Fundación YPF - 2024

## Integrantes GRUPO 7
* Casco
* Romina Torres
* Camila Breide
* Cristin Bianca
* Yelos

## Datasets utilizados
Utilizaremos las bases de datos proporcionadas por el Indec para el año 2018
https://www.indec.gob.ar/indec/web/Institucional-Indec-BasesDeDatos-2
En la seccion salud, especificamente : "Encuesta Nacional de Factores de Riesgo (ENFR)"
De ser necesario para el proyecto, ampliaremos el uso a las bases de datos correspondientes a los años 200, 2009 y 2013

## Estructura del repositorio
analisisBD.ipynb
README.txt
datasets - carpeta con los archivos correspondientes a todos los años
utils - carpeta con archivos de utilidad
    codificaciones.py - diccionarios correspondientes a toda la codificacion usada en los datasets
    functions.py - funciones creadas para el uso comun en todo el analisis 

## Organizacion del trabajo
El objetivo de nuestro trabajo es el siguiente:

+ Desarrollar un modelo predictivo para identificar individuos con alto riesgo de
desarrollar enfermedades crónicas (como hipertensión, diabetes, colesterol alto) basándose
en sus comportamientos y condiciones de vida.

Para un manejo mejor y mas prolijo, separamos las columnas por tablas tematicas:
● Ubicacion : Refiere a la ubicacion del sujeto encuestado
● Características del encuestado 
● Salud general y actividad física
● Tabaquismo 
● Hipertensión 
● Peso corporal 
● Alimentación 
● Colesterol 
● Consumo alcohol 
● Diabetes 

## Reparticion de tablas
Para un trabajo mas rapido, nos separamos las tablas por cantidad similar de columnas, para trabajar individualmente en tareas de limpieza. Cada una realizaria sobre sus tablas:
+ Cambios en el nombre de las columnas, para hacerlos mas descriptivos
+ Creacion de diccionarios correspondientes a los codigos para cada respuesta
+ Eliminacion de columnas innecesarias o derivadas de otras

La reparticion final fue:
* Romina Torres:
Tabaquismo: 42 columnas
Total: 42 columnas

* Camila Breide:
Salud general y actividad física: 25 columnas
Peso corporal: 9 columnas
Total: 25 + 9 = 34 columnas

* Bianca Cristin:
Consumo de alcohol: 23 columnas
Identificación y ubicación: 7 columnas
Colesterol: 8 columnas
Total: 23 + 7 + 8 = 38 columnas

* Diana Yelos:
Hipertensión: 20 columnas
Características del encuestado: 15 columnas
Total: 20 + 15 = 35 columnas

* Casco :
Alimentación: 18 columnas
Diabetes: 19 columnas
Total: 18 + 19 = 37 columnas

## Trabajo grupal
Una vez "limpias" las tablas por tematica, se uniran para formar la base de datos final a utilizar. Esto por motivo de que la base de datos del INDEC (original) tiene columnas que no son necesarias, a nuestro criterio, para la realizacion del objetivo.

### Pre - entrega 04/06/2024
Las modificaciones/ graficos creados son los siguientes:
+ Describir
—---------------------------------------------------------------------
## Notas sobre documentacion 
Debemos crear un documento, en primera instancia .doc / .pdf , para el detalle en los cambios en columnas, los tipos de variables de cada columna, la razon de valores nulos, y demas temas que creamos relevantes para brindarle claridad al proyecto y nuestro proceso de trabajo.

