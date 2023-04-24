
"""
Queremos ir al cine con nuestras amistades, pero no queremos ir a ver cualquier película, para ello queremos
información antes de decidir qué vamos a ver. Esta información la vamos a sacar de un servicio web, en concreto de TMDB.
 Nuestro programa tendrá un menú (usando la clase diseñada para este fin) con las siguientes opciones:

Películas a recomendar si nos gusta una película concreta.
"""
from credentials import BASE_URL, API_KEY  # importamos las credenciales API_KEY Y BASE_URL
import requests
from exceptions import exception_connection_error


def get_recommends_movies():
    if exception_connection_error() is True:
        return
    # contador y cambio de página
    movie_counter = 1
    page = 1
    movie_id = input("Dime el id de la película para recomendarte películas relacionadas: ")

    while True:
        # datos y parámetros para hacer la petición
        url = f"{BASE_URL}/movie/{movie_id}/recommendations?api_key={API_KEY}"
        params = {"page": page, "language": "es"}

        # petición
        response = requests.get(url, params)
        if response.status_code != 200:
            print("\nNo se han encontrados resultados. Error al hacer la petición:", response.status_code)
            print("")
            return
        response_json = response.json()

        # Le mostramos los resultados encontrados
        print("")
        print(f"Estos son los resultados que he encontrado: \n")

        for x in range(len(response_json["results"])):
            print(f"Nº{movie_counter}")
            print("Título:", response_json["results"][x]["title"])
            print("Argumento:", response_json["results"][x]["overview"])
            print("Año:", response_json["results"][x]["release_date"])
            print("")
            movie_counter += 1

        # preguntamos si quiere ver más resultados
        while True:
            user_answer = input("¿Quieres ver más resultados?(Si/No): ")
            if user_answer.upper() == "NO":
                return
            elif user_answer.upper() == "SI":
                page += 1
                if page > response_json["total_pages"]:
                    print("")
                    print("No se han encontrado más resultados.\n")
                    return
                break
            else:
                print("No has introducido un valor válido.")


if __name__ == '__main__':
    get_recommends_movies()
