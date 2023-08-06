from fastapi import FastAPI, HTTPException
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


#http://127.0.0.1:8000

df = pd.read_csv('Datasets/movies.csv')

app = FastAPI()


#Búsqueda con idioma de la película
@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma: str):

    if idioma not in df['language'].values:
        raise HTTPException(status_code=404, detail="El idioma ingresado no existe en el dataset")

    cantidad_peliculas = df[df['language'] == idioma].shape[0]
    return {'idioma': idioma, 'cantidad': cantidad_peliculas}


#Búsqueda de duración y año de las películas
@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula: str):

    if pelicula not in df['title'].values:
        raise HTTPException(status_code=404, detail="La película ingresada no existe en el dataset")
    
    movie_data = df[df['title']==pelicula]
    
    duracion = int(movie_data['runtime'].iloc[0])
    anio = str(movie_data['year'].iloc[0])

    return {'pelicula': pelicula, 'duracion': duracion, 'anio': anio}



#Búsqueda de la franquicia de la pelicula 
@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):

    if franquicia not in df['collections'].values:
        raise HTTPException(status_code=404, detail="La película ingresada no existe en el dataset")
    
    franquicia_data = df[df['collections']==franquicia]
    
    respuesta = franquicia_data['title'].shape[0]
    ganancia_total = franquicia_data['revenue'].sum()
    ganancia_promedio = franquicia_data['revenue'].mean()
    return {'franquicia':franquicia, 'cantidad':respuesta, 'ganancia_total':ganancia_total, 'ganancia_promedio':ganancia_promedio}



#Búsqueda de películas por país
@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    if pais not in df['country'].values:
        raise HTTPException(status_code=404, detail="la pelicula ingresada no existe en el dataset")
    
    pais_data = df[df['country']==pais]
    
    respuesta = pais_data['title'].shape[0]
    return {'pais':pais, 'cantidad':respuesta}


#Búsqueda de películas por productora
@app.get('/productoras_exitosas/{company}')
def productoras_exitosas(company:str):
 
    if company not in df['company'].values:
        raise HTTPException(status_code=404, detail="La productora ingresada no existe en el dataset")
    
    company_data = df[df['company']==company]

    revenue = company_data['revenue'].sum()
    cantidad = company_data['title'].shape[0]
    
    return {'productora':company, 'revenue_total': revenue ,'cantidad':cantidad}



#Búsqueda por nombre del director
@app.get('/get_director/{director}')
def get_director(director:str):

    if director not in df['director'].values:
        raise HTTPException(status_code=404, detail="El nombre del director ingresado no existe en el dataset")
    
    retorno_total = df[df['director']==director]['return'].sum()
    peliculas = df[df['director']==director]['title'].tolist()
    anios = df[df['director']==director]['year'].tolist()
    budget = df[df['director']==director]['budget'].tolist()
    revenue = df[df['director']==director]['revenue'].tolist()
    retorno =  df[df['director']==director]['return'].tolist()
    revenue = df[df['director']==director]['revenue'].tolist()
    
    return {'director': director, 'retorno_total_director':retorno_total ,
    'peliculas':peliculas, 'anios':anios, 'retorno_pelicula': retorno, 'budget_pelicula':budget, 'revenue_pelicula':revenue}



#Desarrollo del modelo ML
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo: str):

    if titulo not in df['title'].values:
        raise HTTPException(status_code=404, detail="La película ingresada no existe en el dataset")
    
    tfidf = TfidfVectorizer(stop_words="english")
    df['overview'] = df['overview'].fillna('')
    tfidf_matrix = tfidf.fit_transform(df["overview"])

    indices = pd.Series(df.index, index=df['title']).drop_duplicates() 

    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    idx = indices[titulo]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    respuesta = df['title'].iloc[movie_indices].values.tolist()

    return {'lista_recomendada': respuesta}
