import streamlit as st
import requests
from login.service import logout


class MovieRepository:
    def __init__(self):
        self.__base_url = "https://gabrielmelgacom.pythonanywhere.com/api/v1/"
        self.__url = f"{self.__base_url}movies/"
        self.__headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

    def get_movies(self):
        response = requests.get(
            self.__url,
            headers=self.__headers,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f"Erro ao obter dados da API. Status code: {response.status_code}")
    
    def create_movie(self, movie):
        response = requests.post(
            self.__url,
            headers=self.__headers,
            data=movie,
        )

        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        if response.status_code == 400:
            st.warning(f'Seu resumo deve ter pelo menos 20 caracteres. Status code: 400')
        raise Exception(f"Erro ao criar filme. Status code: {response.status_code}")
    
    def get_movies_stats(self):
        self.__reviews_stats_url = f'{self.__url}/stats'
        response = requests.get(
            self.__reviews_stats_url,
            headers = self.__headers,
        )

        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao buscar estatísticas de filmes {response.status_code}')