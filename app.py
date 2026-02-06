import streamlit as st
from utils.styles import load_css
from components import hero, vision, problema, propuesta, medicion, expansion, footer

# Configuración
st.set_page_config(
    page_title="Julian Course | SuraTech",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS
st.markdown(load_css(), unsafe_allow_html=True)

# Renderizar componentes
hero.render()
vision.render()
problema.render()
propuesta.render()
medicion.render()
expansion.render()
footer.render()

# Sidebar
with st.sidebar:
    st.image("https://www.sura.com/Style%20Library/Sura/Assets/images/header-sura-logo.png", width=160)
    st.markdown("### 📍 Navegación")
    st.markdown("- 🎯 Visión\n- 🔍 Problema\n- ⚙️ Propuesta")
    st.success("⚡ Optimizado")
