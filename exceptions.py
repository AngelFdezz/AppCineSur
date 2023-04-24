from credentials import BASE_URL, API_KEY
import requests
from requests.exceptions import ConnectionError


def exception_connection_error():
    url = f'{BASE_URL}/movie/550?api_key={API_KEY}'
    try:
        requests.get(url)
    except ConnectionError:
        print(f'Error de conexión: No tienes conexión internet, inténtalo más tarde.')
        return True


if __name__ == '__main__':
    exception_connection_error()
