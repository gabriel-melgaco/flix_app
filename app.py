import streamlit as st
from genres.page import show_genres, create_genre
from actors.page import show_actors, create_actor
from movies.page import show_movies, create_movie
from reviews.page import show_reviews, create_reviews
from login.page import show_login, show_logout
from home.page import show_home



def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('Flix App')

        menu_option = st.sidebar.selectbox(
            'Selecione uma opção',
            ['Início', 'Gêneros', 'Atores/Atrizes', 'Filmes', 'Avaliações'],
        )

        show_logout()

        if menu_option == 'Início':
            st.write('Seja Bem-vindo ao Flix App!')
            show_home()

        if menu_option == 'Gêneros':
            show_genres()
            create_genre()
        
        if menu_option == 'Atores/Atrizes':
            show_actors()
            create_actor()

        if menu_option == 'Filmes':
            show_movies()
            create_movie()

        if menu_option == 'Avaliações':
            show_reviews()
            create_reviews()


if __name__ == '__main__':
    main()