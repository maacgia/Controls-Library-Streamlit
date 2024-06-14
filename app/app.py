import streamlit as st
from streamlit_option_menu import option_menu

# Título principal de la aplicación
st.set_page_config(layout="wide")
st.title("Aplicación de Ejemplo con Múltiples Páginas")

# Menú de navegación
with st.sidebar:
    selected = option_menu(menu_title="Menú de Navegación",
                           options=["Página 1", "Página 2", "Página 3", "Página 4", "Página 5"],
                           icons=["house", "file-earmark-text", "gear", "list-task", "cloud-upload"],
                           menu_icon="cast",
                           default_index=0)

# Navegación a las páginas correspondientes
if selected == "Página 1":
    st.subheader("Página 1")
    import page1
    page1.show_page()
elif selected == "Página 2":
    st.subheader("Página 2")
    import page2
    page2.show_page()
elif selected == "Página 3":
    st.subheader("Página 3")
    import page3
    page3.show_page()
elif selected == "Página 4":
    st.subheader("Página 4")
    import page4
    page4.show_page()
elif selected == "Página 5":
    st.subheader("Página 5")
    import page5
    page5.show_page()
