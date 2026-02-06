import streamlit as st

def render():
    st.markdown('<h2 class="section-title">🌎 Expansión LATAM</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card" style="border-left-color: #00D98E;">
            <h4 style="color: #00D98E;">✅ TRANSVERSALES</h4>
            <ul><li>UX</li><li>Arquitectura</li><li>Métricas</li></ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card" style="border-left-color: #FF6B6B;">
            <h4 style="color: #FF6B6B;">🎯 LOCALES</h4>
            <ul><li>Regulación</li><li>Pagos</li><li>Lenguaje</li></ul>
        </div>
        """, unsafe_allow_html=True)
