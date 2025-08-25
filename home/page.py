import streamlit as st
from movies.service import MovieService
import plotly.express as px


def show_home():

    movie_service = MovieService().get_movies_stats()
    st.title('Estatísticas de filmes')


    if len(movie_service['movies_by_genre']) > 0:
        fig = px.pie(
            movie_service['movies_by_genre'],
            values = 'total',
            names='genre__name',
            title='Filmes por Gênero'
        )
        st.plotly_chart(fig)
    else:
        st.warning('Não há estatísticas a serem apresentadas.')


    st.subheader('Total de Filmes Cadastrados:')
    st.write(movie_service['total_movies'])

    st.subheader('Total de Avaliações Cadastradas:')
    st.write(movie_service['total_reviews'])

    st.subheader('Média Geral de Estrelas nas Avaliações:')
    st.write(movie_service['average_stars'])


