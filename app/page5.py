import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt
import folium
from streamlit_folium import st_folium
from PyPDF2 import PdfReader


def show_page():
    # Título principal
    st.title("Controles y Funcionalidades Adicionales en Streamlit")

    # Visualización de datos geoespaciales en un mapa
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Visualización en Mapa")
        df = pd.DataFrame(np.random.randn(100, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
        st.map(df)
    with col2:
        st.code('''\
df = pd.DataFrame(np.random.randn(100, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)
''')

    # Gráficos interactivos con Plotly
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Gráficos Interactivos con Plotly")
        df = px.data.iris()
        fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', title="Plotly Scatter Plot")
        st.plotly_chart(fig)
    with col2:
        st.code('''\
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', title="Plotly Scatter Plot")
st.plotly_chart(fig)
''')

    # Gráficos interactivos con Altair
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Gráficos Interactivos con Altair")
        chart = alt.Chart(df).mark_circle(size=60).encode(x='sepal_width',
                                                          y='sepal_length',
                                                          color='species',
                                                          tooltip=['species', 'sepal_width', 'sepal_length']).interactive()
        st.altair_chart(chart, use_container_width=True)
    with col2:
        st.code('''\
chart = alt.Chart(df).mark_circle(size=60).encode(
    x='sepal_width', y='sepal_length', color='species', 
    tooltip=['species', 'sepal_width', 'sepal_length']).interactive()
st.altair_chart(chart, use_container_width=True)
''')

    # Integración con Folium para mapas avanzados
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Mapa Interactivo con Folium")
        m = folium.Map(location=[37.76, -122.4], zoom_start=12)
        folium.Marker([37.76, -122.4], popup="San Francisco").add_to(m)
        st_folium(m, width=700, height=500)
    with col2:
        st.code('''\
m = folium.Map(location=[37.76, -122.4], zoom_start=12)
folium.Marker([37.76, -122.4], popup="San Francisco").add_to(m)
st_folium(m, width=700, height=500)
''')

    # Control para subir y mostrar una imagen
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Carga y Visualización de Imágenes")
        uploaded_image = st.file_uploader("Sube una imagen", type=["png", "jpg", "jpeg"])
        if uploaded_image is not None:
            st.image(uploaded_image, caption="Imagen subida", use_column_width=True)
    with col2:
        st.code('''\
uploaded_image = st.file_uploader("Sube una imagen", type=["png", "jpg", "jpeg"])
if uploaded_image is not None:
    st.image(uploaded_image, caption="Imagen subida", use_column_width=True)
''')

    # Almacenamiento en caché
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Ejemplo de Almacenamiento en Caché")

        @st.cache_data
        def load_data():
            return np.random.randn(1000)

        data = load_data()
        st.write(data)
    with col2:
        st.code('''\
@st.cache_data
def load_data():
    return np.random.randn(1000)
data = load_data()
st.write(data)
''')

    # Control de carga de archivo PDF y visualización
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Carga y Visualización de Archivos PDF")
        uploaded_pdf = st.file_uploader("Sube un archivo PDF", type=["pdf"])
        if uploaded_pdf is not None:
            pdf_reader = PdfReader(uploaded_pdf)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                st.text(page.extract_text())
    with col2:
        st.code('''\
uploaded_pdf = st.file_uploader("Sube un archivo PDF", type=["pdf"])
if uploaded_pdf is not None:
    pdf_reader = PdfReader(uploaded_pdf)
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        st.text(page.extract_text())
''')


if __name__ == "__main__":
    show_page()
