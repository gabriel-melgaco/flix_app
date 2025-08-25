import requests


class Auth:

    def __init__(self):
        self.__base_url = 'https://gabrielmelgacom.pythonanywhere.com/api/v1/'
        self.__auth_url = f'{self.__base_url}authentication/token/'

    def get_token(self, username, password):
        auth_payload = {
            'username': username,
            'password': password,
        }
        auth_response = requests.post(
            self.__auth_url,
            json=auth_payload
        )
        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f'Erro na autenticação {auth_response.status_code}'}