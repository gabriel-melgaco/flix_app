import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from actors.service import ActorService
import datetime


def show_actors():
    st.title('Lista de Atores/Atrizes:')
    actors = ActorService().get_actors()

    if actors:
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid',
            )
    else:
        st.warning('Nenhum ator/atriz encontrado.')

def create_actor():
    st.title('Cadastrar novo ator')
    name = st.text_input('Nome do ator/atriz:')
    birthday = st.date_input(
        label='Data de nascimento',
        value=datetime.date.today(),
        min_value=datetime.date(1900, 1, 1),
        max_value=datetime.date.today(),
        format='DD/MM/YYYY',
    )
    nationality = st.selectbox('Nacionalidade', ['BRAZIL', 'EUA'])
    if st.button('Cadastrar'):
       new_actor =  ActorService().create_actor(
            name = name,
            birthday = birthday,
            nationality = nationality,
        )
       if new_actor:
          st.rerun()
       else:
          st.error('Erro ao cadastrar ator/atriz. Verifique os dados e tente novamente.')
    