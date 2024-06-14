import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


def show_page():
    # Título principal
    st.title("Biblioteca de Controles Adicionales en Streamlit")

    # Subtítulo
    st.subheader("Ejemplos de otros controles disponibles en Streamlit")

    # Control para carga de archivo
    col1, col2 = st.columns(2)
    with col1:
        uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])
        if uploaded_file is not None:
            try:
                data = pd.read_csv(uploaded_file)
                st.dataframe(data)
            except Exception as e:
                pass
    with col2:
        st.write(
            "```python\nuploaded_file = st.file_uploader('Sube un archivo CSV', type=['csv'])\n\nif uploaded_file is not None:\n    try:\n        data = pd.read_csv(uploaded_file)\n        st.dataframe(data)\n    except Exception as e:\n        pass\n```"
        )

    # Control para entrada de texto en varias líneas
    col1, col2 = st.columns(2)
    with col1:
        multiline_text = st.text_area("Introduce un texto largo")
        st.write("Texto introducido:", multiline_text)
    with col2:
        st.write("```python\nmultiline_text = st.text_area('Introduce un texto largo')\nst.write('Texto introducido:', multiline_text)\n```")

    # Control para seleccionar un color
    col1, col2 = st.columns(2)
    with col1:
        color = st.color_picker("Selecciona un color", "#00f900")
        st.write("Color seleccionado:", color)
    with col2:
        st.write("```python\ncolor = st.color_picker('Selecciona un color', '#00f900')\nst.write('Color seleccionado:', color)\n```")

    # Control para seleccionar una hora
    col1, col2 = st.columns(2)
    with col1:
        hora = st.time_input('Selecciona una hora')
        st.write('Hora seleccionada:', hora)
    with col2:
        st.write("```python\nhora = st.time_input('Selecciona una hora')\nst.write('Hora seleccionada:', hora)\n```")

    # Control para seleccionar un intervalo de fechas
    col1, col2 = st.columns(2)
    with col1:
        date_range = st.date_input('Selecciona un rango de fechas', [])
        st.write('Rango de fechas seleccionado:', date_range)
    with col2:
        st.write("```python\ndate_range = st.date_input('Selecciona un rango de fechas', [])\nst.write('Rango de fechas seleccionado:', date_range)\n```")

    # Gráfica de mapa de calor
    col1, col2 = st.columns(2)
    with col1:
        heatmap_data = np.random.rand(10, 10)
        fig, ax = plt.subplots()
        cax = ax.matshow(heatmap_data, cmap='coolwarm')
        fig.colorbar(cax)
        st.pyplot(fig)
    with col2:
        st.write(
            "```python\nheatmap_data = np.random.rand(10, 10)\nfig, ax = plt.subplots()\ncax = ax.matshow(heatmap_data, cmap='coolwarm')\nfig.colorbar(cax)\nst.pyplot(fig)\n```"
        )

    # Control de progreso
    col1, col2 = st.columns(2)
    with col1:
        st.write("Progreso del proceso")
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.05)
            progress_bar.progress(i + 1)
    with col2:
        st.write(
            "```python\nst.write('Progreso del proceso')\nprogress_bar = st.progress(0)\nfor i in range(100):\n    time.sleep(0.05)\n    progress_bar.progress(i + 1)\n```"
        )

    # Mensaje de alerta
    col1, col2 = st.columns(2)
    with col1:
        st.warning("Esto es una advertencia")
        st.error("Esto es un error")
        st.info("Esto es información")
        st.success("Esto es un éxito")
    with col2:
        st.write(
            "```python\nst.warning('Esto es una advertencia')\nst.error('Esto es un error')\nst.info('Esto es información')\nst.success('Esto es un éxito')\n```"
        )

    # Mensaje de código
    col1, col2 = st.columns(2)
    with col1:
        st.code("print('Hola, Mundo!')", language='python')
    with col2:
        st.write("```python\nst.code(\"print('Hola, Mundo!')\", language='python')\n```")

    # Spinner
    col1, col2 = st.columns(2)
    with col1:
        with st.spinner('Esperando...'):
            time.sleep(2)
        st.success('¡Hecho!')
    with col2:
        st.write("```python\nwith st.spinner('Esperando...'):\n    time.sleep(2)\nst.success('¡Hecho!')\n```")

    # Control para selección de opciones con etiquetas
    col1, col2 = st.columns(2)
    with col1:
        tags = st.text_input('Introduce etiquetas separadas por comas', 'python, streamlit')
        st.write('Etiquetas introducidas:', [tag.strip() for tag in tags.split(',')])
    with col2:
        st.write(
            "```python\ntags = st.text_input('Introduce etiquetas separadas por comas', 'python, streamlit')\nst.write('Etiquetas introducidas:', [tag.strip() for tag in tags.split(',')])\n```"
        )

    # Fin del código de ejemplo


if __name__ == "__main__":
    show_page()
