import streamlit as st
from streamlit_option_menu import option_menu


def show_page():
    # Título principal
    st.title("Ejemplos de Menús con streamlit-option-menu")

    # Menú vertical
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Menú Vertical")
        selected_vertical = option_menu(
            menu_title="Menú Vertical",                 # Menú de título
            options=["Home", "Datos", "Configuración"], # Opciones del menú
            icons=["house", "table", "gear"],           # Iconos de las opciones
            menu_icon="cast",                           # Icono del menú
            default_index=0,                            # Índice predeterminado
        )

        if selected_vertical == "Home":
            st.write("Has seleccionado Home en el menú vertical.")
        elif selected_vertical == "Datos":
            st.write("Has seleccionado Datos en el menú vertical.")
        elif selected_vertical == "Configuración":
            st.write("Has seleccionado Configuración en el menú vertical.")

    with col2:
        st.write(
            "```python\nselected_vertical = option_menu(\n    menu_title='Menú Vertical',\n    options=['Home', 'Datos', 'Configuración'],\n    icons=['house', 'table', 'gear'],\n    menu_icon='cast',\n    default_index=0,\n)\n\nif selected_vertical == 'Home':\n    st.write('Has seleccionado Home en el menú vertical.')\nelif selected_vertical == 'Datos':\n    st.write('Has seleccionado Datos en el menú vertical.')\nelif selected_vertical == 'Configuración':\n    st.write('Has seleccionado Configuración en el menú vertical.')\n```"
        )

    # Separador
    st.markdown("---")

    # Menú horizontal
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Menú Horizontal")
        selected_horizontal = option_menu(
            menu_title=None,                          # Menú de título
            options=["Inicio", "Perfil", "Mensajes"], # Opciones del menú
            icons=["house", "person", "envelope"],    # Iconos de las opciones
            menu_icon="cast",                         # Icono del menú
            default_index=0,                          # Índice predeterminado
            orientation="horizontal")

        if selected_horizontal == "Inicio":
            st.write("Has seleccionado Inicio en el menú horizontal.")
        elif selected_horizontal == "Perfil":
            st.write("Has seleccionado Perfil en el menú horizontal.")
        elif selected_horizontal == "Mensajes":
            st.write("Has seleccionado Mensajes en el menú horizontal.")

    with col2:
        st.write(
            "```python\nselected_horizontal = option_menu(\n    menu_title=None,\n    options=['Inicio', 'Perfil', 'Mensajes'],\n    icons=['house', 'person', 'envelope'],\n    menu_icon='cast',\n    default_index=0,\n    orientation='horizontal'\n)\n\nif selected_horizontal == 'Inicio':\n    st.write('Has seleccionado Inicio en el menú horizontal.')\nelif selected_horizontal == 'Perfil':\n    st.write('Has seleccionado Perfil en el menú horizontal.')\nelif selected_horizontal == 'Mensajes':\n    st.write('Has seleccionado Mensajes en el menú horizontal.')\n```"
        )

    # Separador
    st.markdown("---")

    # Menú con estilos personalizados
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Menú con Estilos Personalizados")
        selected_custom = option_menu(
            menu_title="Menú Personalizado",              # Menú de título
            options=["Dashboard", "Reportes", "Ajustes"], # Opciones del menú
            icons=["speedometer", "bar-chart", "tools"],  # Iconos de las opciones
            menu_icon="cast",                             # Icono del menú
            default_index=0,                              # Índice predeterminado
            styles={
                "container": {
                    "padding": "5px",
                    "background-color": "#f0f2f6"
                },
                "icon": {
                    "color": "orange",
                    "font-size": "25px"
                },
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee"
                },
                "nav-link-selected": {
                    "background-color": "green"
                },
            })

        if selected_custom == "Dashboard":
            st.write("Has seleccionado Dashboard en el menú personalizado.")
        elif selected_custom == "Reportes":
            st.write("Has seleccionado Reportes en el menú personalizado.")
        elif selected_custom == "Ajustes":
            st.write("Has seleccionado Ajustes en el menú personalizado.")

    with col2:
        st.write(
            "```python\nselected_custom = option_menu(\n    menu_title='Menú Personalizado',\n    options=['Dashboard', 'Reportes', 'Ajustes'],\n    icons=['speedometer', 'bar-chart', 'tools'],\n    menu_icon='cast',\n    default_index=0,\n    styles={\n        'container': {\n            'padding': '5px',\n            'background-color': '#f0f2f6'\n        },\n        'icon': {\n            'color': 'orange',\n            'font-size': '25px'\n        },\n        'nav-link': {\n            'font-size': '16px',\n            'text-align': 'left',\n            'margin': '0px',\n            '--hover-color': '#eee'\n        },\n        'nav-link-selected': {\n            'background-color': 'green'\n        },\n    }\n)\n\nif selected_custom == 'Dashboard':\n    st.write('Has seleccionado Dashboard en el menú personalizado.')\nelif selected_custom == 'Reportes':\n    st.write('Has seleccionado Reportes en el menú personalizado.')\nelif selected_custom == 'Ajustes':\n    st.write('Has seleccionado Ajustes en el menú personalizado.')\n```"
        )


if __name__ == "__main__":
    show_page()
