"""
        Programa que saca información de películas. Esta información la vamos a sacar de un servicio web, en concreto
        de TMDB. Nuestro programa tendrá un menú (usando la clase diseñada para este fin) con las siguientes opciones:

        Buscar código de película según su nombre.
        Buscar información de película según su código. Entre los datos de la información debe estar:
        Título.
        Géneros.
        Argumento.
        Duración.
        ...
        Y enlace a su web en IMDB.
        Películas a recomendar si nos gusta una película concreta.
        Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma. Al
        usuario le preguntamos si quiere un género concreto o si los quiere todos.
        Mostrar géneros disponibles.

    Autor: Angel fernandez Ariza
    Curso: 2022-2023
"""
import sys
from movie_id import get_movie_id
from movie_info import get_movie_info_by_id
from recommends_movies import get_recommends_movies
from trending_movies import get_5_trending_movies
from movie_genres import get_all_movie_genres
from menu import Menu

SALIDA_DEL_PROGRAMA_CON_EXITO = 0
menu_cartelera = Menu(
             "Buscar código de película.",
             "Buscar información de película.",
             "Películas a recomendar.",
             "Obtener 5 películas trending topic.",
             "Mostrar géneros disponibles.",
             "Salir del programa."
             )

while True:
    option = menu_cartelera.choose()
    match option:

        case 1:
            get_movie_id()

        case 2:
            get_movie_info_by_id()

        case 3:
            get_recommends_movies()

        case 4:
            get_5_trending_movies()

        case 5:
            get_all_movie_genres()

        case 6:
            sys.exit(SALIDA_DEL_PROGRAMA_CON_EXITO)
