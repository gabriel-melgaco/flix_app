import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from reviews.service import ReviewsService
from movies.service import MovieService

def show_reviews():

    reviews_service = ReviewsService().get_reviews()
    st.title('Lista de Reviews:')
    if reviews_service:
        reviews_df = pd.json_normalize(reviews_service)
    
        AgGrid(
            data=reviews_df,
            reload_data=True,
            key='reviews_grid',
            )
    else:
        st.warning('Não há reviews disponíveis no momento.')

def create_reviews():
    st.title('Criar Review:')
    movies = MovieService().get_movies()
    movie_id = {movie['title']:movie['id'] for movie in movies}
    movie_selected = st.selectbox('Selecione o filme:', list(movie_id.keys()))

    stars = st.number_input('Estrelas (0-5):', min_value=0, max_value=5, step=1)
    comment = st.text_area('Comentário:')


    if st.button("Cadastrar"):
        new_review = ReviewsService().create_review(
            stars=stars,
            comment=comment,
            movie=movie_id[movie_selected],
        )
        if new_review:
            st.rerun()
        else:
            st.error("Erro ao cadastrar a review.")

        