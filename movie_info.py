
"""
Buscar información de película según su código. Entre los datos de la información debe estar:
Título.
Géneros.
Argumento.
Duración.
...
Y enlace a su web en IMDB.
"""

from credentials import BASE_URL, API_KEY  # importamos las credenciales API_KEY Y BASE_URL
import requests
from exceptions import exception_connection_error


def get_movie_info_by_id():
    if exception_connection_error() is True:
        return
    # datos para hacer la petición
    movie_id = input("Dime el id de la película cuya información quieras saber: ")
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}"
    params = {"language": "es-ES"}

    # petición
    response = requests.get(url, params)
    if response.status_code != 200:
        print("\nNo se han encontrados resultados. Error al hacer la petición:", response.status_code)
        print("")
        return

    response_json = response.json()

    # sacamos los datos que necesitamos de json

    movie_title = response_json["title"]
    movie_genre = response_json["genres"]
    movie_overview = response_json["overview"]
    movie_duration = response_json["runtime"]
    movie_url_imdb = response_json["imdb_id"]

    # mostramos los datos
    print("")
    print("----------------------")
    print("Información encontrada")
    print("----------------------")
    print(f"Título: {movie_title}")
    print(f"Géneros:", )
    for x in range(len(movie_genre)):
        print(f'    -{movie_genre[x]["name"]}')
    print(f"Argumento: {movie_overview}")
    print(f"Duración: {movie_duration} minutes")
    print(f"Enlace: https://www.imdb.com/title/{movie_url_imdb}/")
    print("")


if __name__ == '__main__':
    get_movie_info_by_id()
