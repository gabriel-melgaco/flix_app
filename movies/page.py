import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from actors.service import ActorService
from genres.service import GenreService
from movies.service import MovieService
import datetime


def show_movies():
    
    movies = MovieService().get_movies()

    if movies:
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['id','actors', 'genre_id'], errors='ignore')
        st.title('Lista de gêneros:')
        AgGrid(
            data=pd.DataFrame(movies_df),
            reload_data=True,
            key='moview_grid',
            )
    else:
        st.warning('Nenhum filme encontrado.')

    
def create_movie():
    st.title('Cadastrar novo filme')
    title = st.text_input('Título do filme:')

    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.date.today(),
        min_value=datetime.date(1900, 1, 1),
        max_value=datetime.date.today(),
        format='DD/MM/YYYY',
    )
    resume = st.text_area('Resumo do filme:')

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['name']:genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Gênero', genre_names.keys())

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_names = st.multiselect('Atores/Atrizes', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actors_names]

    if st.button('Cadastrar'):
        new_movie = MovieService().create_movie(
            title=title,
            release_date=release_date,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadastrar filme. Verifique os dados e tente novamente.')
