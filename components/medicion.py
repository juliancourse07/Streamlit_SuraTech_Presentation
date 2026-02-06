import streamlit as st

def render():
    st.markdown('<h2 class="section-title">📊 Midiendo lo que Importa</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-box"><h3>⚡</h3><p><strong>Velocidad Percibida</strong></p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-box"><h3>🧠</h3><p><strong>Carga Cognitiva</strong></p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-box"><h3>💚</h3><p><strong>Confianza</strong></p></div>', unsafe_allow_html=True)
