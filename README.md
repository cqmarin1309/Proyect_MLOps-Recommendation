# Proyect_MLOps-Recommendation
A continuación se presenta el proyecto Individual que se trabajo el cual consitió en desarrollar un sistema de recomendación  basado en un daatset de películas.

## Tabla de contenidos

- [ETL](##ETL)
- [EDA](##EDA)
- [Machine Learning](##MachineLearning)
- [FastApi](#FastApi)
- [Render](#Render)
- [Conclusiones](#Conclusiones)
- [Links](#licencia)

## ETL
Se llevaron a cabo los siguientes pasos:

**1. Cargar los archivos: movies.csv y credits.csv**

**2. Información general del proyecto** 

El dataset de movies original tenía más de 40000 filas y muchas de las columnas tenían valores nulos. Por otro lado el daatset de credits no tenía valores nulos

**3. Cambiar las columnas por el tipo adecuado**

- La columna "id" necesitaba cambiarse a int
- Las columnas budget y popularity se cambiarona  float
- La columna release date se cambio a tipo datetime
- 
**4. Merge de ambos dataset por al columna común "id"**

Se unieron los datasets para poder trabajar con uno solo 

**5. Revisión de duplicados**

Descubrimos que existian 3259 películas repetidas, se procedió a eliminarlas

**6. Procesamiento de valores nulos**

Se utilizó al librería missingno para visualizar de forma gráfica los valores nulos de cada columna

**7. Desanidación de columnas y valores a procesar**

 Las columnas a desniadar eran: belongs_to_collection, production_companies, production_countries, spoken_languages, crew, cast y genres

**8. Creación de nuevas columnas**

Se procedió a extraer el año de la columna release_date y se creo la columna "return" para obtener el dato de cuantas veces una película había logrado superar su presupuesto: revenue/budget

**9. Eliminar columnas que desanidamos**

Se eliminaron las columnas que desanidamos: belongs_to_collection, production_companies, production_countries, spoken_languages, crew, cast y genres; además se eliminaron columnas como video, status, poster_path, entre otras

**10. Reducción de Dataset**

Para fines de este proyecto se procedio a obtener una muestra del dataset total, del total de las compañias famosas se procedió a quedarse con las más importantes, por ejemplo: Warner Bros, Pixar Animations, Disney, Dreamworks, Marvel, DC. etc. El dataset se redujo a 5300 filas, pero contienen películas bastante reconocidas y famosas pertenecientes a dichas casas productoras. 

**11. Exportación de dataset**

Se exportó el dataset trabajado en formato movies.csv
    
## EDA
Se llevaron a cabo los siguientes pasos:
1. Cargar los datos: movies.csv
2. Forma del dataset
3. Información general del dataset
4. Revisión de nulos
5. Análisis de columnas numéricas
6. Análisis de columnas categóricas

Desarrollo del Proyecto Individual de Henry 
Link de proyecto: https://proyecto-individual-henry-u9nx.onrender.com/docs
