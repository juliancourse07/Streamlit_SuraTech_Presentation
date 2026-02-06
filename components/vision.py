import streamlit as st

def render():
    st.markdown('<h2 class="section-title">🎯 Mi Visión: Procesos con Alma</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3 style="color: #0072CE; margin-top: 0;">💡 Ser dueño del proceso</h3>
            <p>Significa <strong>orquestarlo desde la empatía radical</strong>.</p>
            <ul style="line-height: 1.9;">
                <li>🧭 <strong>Navegar la incertidumbre</strong></li>
                <li>🔄 <strong>Iterar sin miedo</strong></li>
                <li>🤝 <strong>Co-crear con todos</strong></li>
                <li>📊 <strong>Medir momentos de verdad</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3 style="color: #00C9DB; margin-top: 0;">🌟 Mi Diferencial</h3>
            <ul style="line-height: 1.9;">
                <li>🎨 <strong>Design Thinking</strong> aplicado</li>
                <li>🧠 <strong>Psicología del usuario</strong></li>
                <li>⚡ <strong>Agilidad humana</strong></li>
                <li>🌎 <strong>Visión LATAM</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
