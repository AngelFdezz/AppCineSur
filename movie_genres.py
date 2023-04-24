"""
Mostrar géneros disponibles.
"""

from credentials import BASE_URL, API_KEY  # importamos las credenciales API_KEY Y BASE_URL
import requests
from exceptions import exception_connection_error


def get_all_movie_genres():
    if exception_connection_error() is True:
        return
    # datos para hacer la petición
    url = f'{BASE_URL}/genre/movie/list?api_key={API_KEY}'
    params = {"language": "es-ES"}

    # petición
    response = requests.get(url, params)
    if response.status_code != 200:
        print("No se han encontrados resultados. Error al hacer la petición:", response.status_code)
        return
    response_json = response.json()

    # mostrar los géneros en pantalla
    print("")
    print(f'Se han encontrado {len(response_json["genres"])} géneros: ')
    print("-----------------------------")

    genre_counter = 1  # contador para los géneros
    for x in range(len(response_json["genres"])):
        print(f'Género Nº{genre_counter}:', response_json["genres"][x]["name"])
        print('ID:', response_json["genres"][x]["id"])
        print("")
        genre_counter += 1


if __name__ == '__main__':
    get_all_movie_genres()
