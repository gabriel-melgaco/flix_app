import streamlit as st
from login.service import login, logout


def show_login():
    st.title('Login')

    username = st.text_input('Usuário')
    password = st.text_input(label='Senha', type='password')

    if st.button('Entrar'):
        login(
            username = username,
            password=password,
        )


def show_logout():
    if st.sidebar.button('Logout'):
        logout()