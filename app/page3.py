import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def show_page():
    # Título principal
    st.title("Biblioteca de Controles Adicionales en Streamlit")

    # Subtítulo
    st.subheader("Ejemplos de otros controles adicionales disponibles en Streamlit")

    # Control select_slider
    col1, col2 = st.columns(2)
    with col1:
        option = st.select_slider('Selecciona un valor', options=['Bajo', 'Medio', 'Alto'])
        st.write('Valor seleccionado:', option)
    with col2:
        st.write("```python\noption = st.select_slider('Selecciona un valor', options=['Bajo', 'Medio', 'Alto'])\nst.write('Valor seleccionado:', option)\n```")

    # Control de audio
    col1, col2 = st.columns(2)
    with col1:
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    with col2:
        st.write("```python\nst.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')\n```")

    # Control de video
    col1, col2 = st.columns(2)
    with col1:
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    with col2:
        st.write("```python\nst.video('https://www.w3schools.com/html/mov_bbb.mp4')\n```")

    # Control de entrada de cámara
    col1, col2 = st.columns(2)
    with col1:
        image = st.camera_input("Toma una foto")
        if image:
            st.image(image)
    with col2:
        st.write("```python\nimage = st.camera_input('Toma una foto')\nif image:\n    st.image(image)\n```")

    # Control de métricas
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Temperatura", value="70 °F", delta="1.2 °F")
    with col2:
        st.write("```python\nst.metric(label='Temperatura', value='70 °F', delta='1.2 °F')\n```")

    # Disposición en columnas
    col1, col2 = st.columns(2)
    with col1:
        col1_1, col1_2, col1_3 = st.columns(3)
        with col1_1:
            st.metric(label="Column 1", value="Value 1")
        with col1_2:
            st.metric(label="Column 2", value="Value 2")
        with col1_3:
            st.metric(label="Column 3", value="Value 3")
    with col2:
        st.write(
            "```python\ncol1, col2, col3 = st.columns(3)\nwith col1:\n    st.metric(label='Column 1', value='Value 1')\nwith col2:\n    st.metric(label='Column 2', value='Value 2')\nwith col3:\n    st.metric(label='Column 3', value='Value 3')\n```"
        )

    # Formularios
    col1, col2 = st.columns(2)
    with col1:
        with st.form(key='my_form'):
            name = st.text_input('Introduce tu nombre')
            age = st.number_input('Introduce tu edad', min_value=0, max_value=100)
            submitted = st.form_submit_button('Enviar')
            if submitted:
                st.write(f'Nombre: {name}, Edad: {age}')
    with col2:
        st.write(
            "```python\nwith st.form(key='my_form'):\n    name = st.text_input('Introduce tu nombre')\n    age = st.number_input('Introduce tu edad', min_value=0, max_value=100)\n    submitted = st.form_submit_button('Enviar')\n    if submitted:\n        st.write(f'Nombre: {name}, Edad: {age}')\n```"
        )

    # Fin del código de ejemplo


if __name__ == "__main__":
    show_page()
