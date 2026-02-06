import streamlit as st

def render():
    st.markdown('<h2 class="section-title">🔍 El Problema Real</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3 style="color: #003366; margin-top: 0;">👤 María, 32 años, recién mamá</h3>
        <p style="font-size: 1.1em;">
        Necesita agregar cobertura familiar. Proceso actual: 
        <strong>3 transferencias, 5 días, 6-8 frustraciones</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 🗺️ Journey Emocional")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown('<div style="text-align: center;"><h1>🤔</h1><p>Necesidad<br>😐</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div style="text-align: center;"><h1>📞</h1><p>Contacto<br>😕</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div style="text-align: center;"><h1>⏰</h1><p>Espera<br>😤</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div style="text-align: center;"><h1>✅</h1><p>Proceso<br>🙂</p></div>', unsafe_allow_html=True)
    with col5:
        st.markdown('<div style="text-align: center;"><h1>😊</h1><p>Confirmación<br>😊</p></div>', unsafe_allow_html=True)
