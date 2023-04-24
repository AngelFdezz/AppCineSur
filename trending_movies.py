"""
Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma.
Al usuario le preguntamos si quiere un género concreto o si los quiere todos.
"""
import requests
from credentials import API_KEY, BASE_URL
from movie_genres import get_all_movie_genres
from exceptions import exception_connection_error


def get_5_trending_movies():
    if exception_connection_error() is True:
        return
    # elige si quiere trending global o de un género específico
    while True:
        choice = input("¿Quieres ver el trending global o de un género en concreto?(Global/Género): ")
        if choice.upper() == "GLOBAL" or choice.upper() == "GÉNERO":
            break
        else:
            print("No has introducido Global o Género.")

    # en caso de que haya elegido género específico, muestro todos los géneros con sus ids para que elija y
    # comprueba que el género introducido existe
    id_genre = 0
    if choice.upper() == "GÉNERO":
        genres_ids = ["28", "12", "16", "35", "802", "99", "18", "10751", "14", "36", "27", "10402", "9648", "10749",
                      "878", "10770", "53", "10752", "37"]
        get_all_movie_genres()
        while True:
            print("")
            id_genre = input("Dime el id de un género en específico: ")
            print("")
            if str(id_genre) in genres_ids:
                break
            else:
                print("Ese id de género no existe. Vuelva a introducir uno.\n")

    # preguntamos si quiere el trending semanal o diario
    while True:
        day_or_week = input("¿Quieres el trending de la semana o del día? ")
        if day_or_week.upper() == "SEMANA" or day_or_week.upper() == "DÍA":
            if day_or_week.upper() == 'SEMANA':
                type_week_or_day = 'week'
                break
            else:
                type_week_or_day = 'day'
                break
        else:
            print("Valor no válido, vuelva a escribirlo.\n")

    # si ha elegido el género global hacemos la petición
    if choice.upper() == "GLOBAL":
        url1 = f'{BASE_URL}/trending/movie/{type_week_or_day}?api_key={API_KEY}'
        params1 = {"language": "es"}
        response1 = requests.get(url1, params1)

        # comprobamos que la petición ha sido correcta.
        if response1.status_code != 200:
            print("\nNo se han encontrados resultados. Error al hacer la petición:", response1.status_code)
            print("")
            exit(1)

        response1_json = response1.json()

        # printeamos los datos obtenidos
        for x in range(5):
            print(f'Nº{x + 1}')
            print('\nTitulo:', response1_json["results"][x]["title"])
            print('Fecha de lanzamiento:', response1_json["results"][x]["release_date"])
            print('Id:', response1_json["results"][x]["id"])
            print('Valoración media:', response1_json["results"][x]["vote_average"])
            print('Cuento de votos:', response1_json["results"][x]["vote_count"])
            print("")

    # en caso de que haya elegido género específico hacemos petición,si no encuentra en la primera pag pasa a la segunda
    else:
        # contador de páginas y películas
        page = 1
        movie_counter = 0
        while True:
            x = None
            url2 = f'{BASE_URL}/trending/movie/{type_week_or_day}?api_key={API_KEY}'
            params2 = {"page": page, "language": "es"}
            response2 = requests.get(url2, params2)

            # comprobamos que la petición ha sido correcta.
            if response2.status_code != 200:
                print("\nNo se han encontrados resultados. Error al hacer la petición:", response2.status_code)
                print("")
                return
            response2_json = response2.json()

            # aumento de página en caso de que no encuentre en la primera y finaliza cuando tenga 5 pelis.
            while True:
                num_results = len(response2_json["results"])
                if x == num_results - 1:
                    page += 1
                    break
                for x in range(num_results):
                    if movie_counter == 5:
                        return
                    genres = response2_json["results"][x]["genre_ids"]
                    # print de datos
                    if int(id_genre) in genres:
                        print("Nº", movie_counter + 1)
                        print('\nTitulo:', response2_json["results"][x]["title"])
                        print('Fecha de lanzamiento:', response2_json["results"][x]["release_date"])
                        print('Id:', response2_json["results"][x]["id"])
                        print('Valoración media:', response2_json["results"][x]["vote_average"])
                        print('Número de votaciones:', response2_json["results"][x]["vote_count"])
                        print("")
                        movie_counter += 1


if __name__ == '__main__':
    get_5_trending_movies()
