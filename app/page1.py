import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def show_page():
    # Título principal
    st.title("Biblioteca de Controles en Streamlit")

    # Subtítulo
    st.subheader("Ejemplos de diferentes controles disponibles en Streamlit")

    # Control de botón
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Haz clic aquí'):
            st.write('¡Botón presionado!')
    with col2:
        st.write("```python\nif st.button('Haz clic aquí'):\n    st.write('¡Botón presionado!')\n```")

    # Control de checkbox
    col1, col2 = st.columns(2)
    with col1:
        checkbox_state = st.checkbox('Mostrar mensaje')
        if checkbox_state:
            st.write('¡Checkbox activado!')
    with col2:
        st.write("```python\ncheckbox_state = st.checkbox('Mostrar mensaje')\nif checkbox_state:\n    st.write('¡Checkbox activado!')\n```")

    # Control de radio buttons
    col1, col2 = st.columns(2)
    with col1:
        opcion = st.radio("Elige una opción:", ('Opción 1', 'Opción 2', 'Opción 3'))
        if opcion == 'Opción 1':
            st.write('Has elegido la Opción 1')
        elif opcion == 'Opción 2':
            st.write('Has elegido la Opción 2')
        else:
            st.write('Has elegido la Opción 3')
    with col2:
        st.write(
            "```python\nopcion = st.radio('Elige una opción:', ('Opción 1', 'Opción 2', 'Opción 3'))\n\nif opcion == 'Opción 1':\n    st.write('Has elegido la Opción 1')\nelif opcion == 'Opción 2':\n    st.write('Has elegido la Opción 2')\nelse:\n    st.write('Has elegido la Opción 3')\n```"
        )

    # Control de select box
    col1, col2 = st.columns(2)
    with col1:
        seleccion = st.selectbox('Selecciona un valor', ('Valor 1', 'Valor 2', 'Valor 3'))
        st.write('Has seleccionado:', seleccion)
    with col2:
        st.write("```python\nseleccion = st.selectbox('Selecciona un valor', ('Valor 1', 'Valor 2', 'Valor 3'))\nst.write('Has seleccionado:', seleccion)\n```")

    # Control de multiselect
    col1, col2 = st.columns(2)
    with col1:
        opciones = st.multiselect('Selecciona múltiples opciones', ['A', 'B', 'C', 'D'])
        st.write('Has seleccionado:', opciones)
    with col2:
        st.write("```python\nopciones = st.multiselect('Selecciona múltiples opciones', ['A', 'B', 'C', 'D'])\nst.write('Has seleccionado:', opciones)\n```")

    # Control de texto
    col1, col2 = st.columns(2)
    with col1:
        texto = st.text_input('Introduce tu nombre')
        st.write('Tu nombre es:', texto)
    with col2:
        st.write("```python\ntexto = st.text_input('Introduce tu nombre')\nst.write('Tu nombre es:', texto)\n```")

    # Control de número
    col1, col2 = st.columns(2)
    with col1:
        numero = st.number_input('Introduce un número', 0, 100)
        st.write('Número introducido:', numero)
    with col2:
        st.write("```python\nnumero = st.number_input('Introduce un número', 0, 100)\nst.write('Número introducido:', numero)\n```")

    # Control de fecha
    col1, col2 = st.columns(2)
    with col1:
        fecha = st.date_input('Selecciona una fecha')
        st.write('Fecha seleccionada:', fecha)
    with col2:
        st.write("```python\nfecha = st.date_input('Selecciona una fecha')\nst.write('Fecha seleccionada:', fecha)\n```")

    # Tabla de datos
    col1, col2 = st.columns(2)
    with col1:
        data = {'Columna 1': [1, 2, 3, 4], 'Columna 2': [10, 20, 30, 40]}
        df = pd.DataFrame(data)
        st.table(df)
    with col2:
        st.write("```python\ndata = {'Columna 1': [1, 2, 3, 4], 'Columna 2': [10, 20, 30, 40]}\ndf = pd.DataFrame(data)\nst.table(df)\n```")

    # Gráfica de línea
    col1, col2 = st.columns(2)
    with col1:
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
        st.line_chart(chart_data)
    with col2:
        st.write("```python\nchart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])\nst.line_chart(chart_data)\n```")

    # Gráfica de barras
    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(chart_data)
    with col2:
        st.write("```python\nst.bar_chart(chart_data)\n```")

    # Gráfica de dispersión con matplotlib
    col1, col2 = st.columns(2)
    with col1:
        x = np.random.randn(100)
        y = np.random.randn(100)
        fig, ax = plt.subplots()
        ax.scatter(x, y)
        st.pyplot(fig)
    with col2:
        st.write("```python\nx = np.random.randn(100)\ny = np.random.randn(100)\nfig, ax = plt.subplots()\nax.scatter(x, y)\nst.pyplot(fig)\n```")

    # Gráfica de área
    col1, col2 = st.columns(2)
    with col1:
        st.area_chart(chart_data)
    with col2:
        st.write("```python\nst.area_chart(chart_data)\n```")

    # Código adicional para agrupar elementos (opcional)
    st.markdown("### Controles Agrupados")
    col1, col2 = st.columns(2)
    with col1:
        col1_1, col1_2, col1_3 = st.columns(3)
        with col1_1:
            st.button('Botón en Columna 1')
        with col1_2:
            st.button('Botón en Columna 2')
        with col1_3:
            st.button('Botón en Columna 3')
    with col2:
        st.write(
            "```python\ncol1, col2, col3 = st.columns(3)\nwith col1:\n    st.button('Botón en Columna 1')\nwith col2:\n    st.button('Botón en Columna 2')\nwith col3:\n    st.button('Botón en Columna 3')\n```"
        )

    st.markdown("### Controles dentro de un Expander")
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("Haz clic para expandir"):
            st.write("Contenido expandido")
            st.slider('Slider dentro del expander', 0, 100, 50)
            st.selectbox('Selectbox dentro del expander', ['Opción A', 'Opción B', 'Opción C'])
    with col2:
        st.write(
            "```python\nwith st.expander('Haz clic para expandir'):\n    st.write('Contenido expandido')\n    st.slider('Slider dentro del expander', 0, 100, 50)\n    st.selectbox('Selectbox dentro del expander', ['Opción A', 'Opción B', 'Opción C'])\n```"
        )

    st.markdown("### Controles en una Sidebar")
    col1, col2 = st.columns(2)
    with col1:
        st.sidebar.title("Controles en la Sidebar")
        st.sidebar.button('Botón en Sidebar')
        st.sidebar.radio('Radio en Sidebar', ['A', 'B', 'C'])
    with col2:
        st.write(
            "```python\nst.sidebar.title('Controles en la Sidebar')\nst.sidebar.button('Botón en Sidebar')\nst.sidebar.radio('Radio en Sidebar', ['A', 'B', 'C'])\n```"
        )

    # Fin del código de ejemplo


if __name__ == "__main__":
    show_page()
