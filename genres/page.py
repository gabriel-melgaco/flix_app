import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd
from genres.service import GenreService





def show_genres():
    genres = GenreService().get_genres()

    if genres:
        st.title('Lista de gêneros:')
        genres_df = pd.json_normalize(genres)#transfromin Json to DataFrame
        AgGrid(
            data=genres_df,
            reload_data=True,
            key='genres_grid',
            )
        
    else:
        st.warning('Nenhum gênero encontrado.')

def create_genre():
    st.title('Cadastrar novo gênenero')
    name = st.text_input('Nome do gênero')
    if st.button('Cadastrar'):
        response = GenreService().create_genre(name)
        if response:
            st.rerun()
        else:
            st.error(f'Erro ao cadastrar gênero. Verifique se o nome {name} já foi cadastrado.')
            