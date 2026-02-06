import streamlit as st

def render():
    st.markdown('<h2 class="section-title">⚙️ Mi Propuesta</h2>', unsafe_allow_html=True)
    
    with st.expander("📋 FASE 1: Empatía Radical"):
        st.markdown("""
        **👥 Con quién:** Cliente B2C, Canal B2B, Tech/Legal
        
        **🔍 Qué investigo:** Benchmarking, data interna, 15 entrevistas
        """)
    
    with st.expander("🎨 FASE 2: Prototipado"):
        st.markdown("""
        **💡 Co-creación:** 3 workshops
        
        **🎯 Principios:** Transparencia, <3min, Multicanal, Seguridad OTP
        """)
    
    with st.expander("🏗️ FASE 3: Flujo (7 pasos)"):
        st.markdown("""
        <div class="timeline">
            <h4>1. Inicio → 2. Validación → 3. Simulación</h4>
            <h4>4. Aprobación → 5. Validación → 6. Confirmación → 7. Seguimiento</h4>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("📊 FASE 4: KPIs Disruptivos"):
        st.markdown("""
        - 🎤 Effortless Score (1-5)
        - 🔄 Tasa Completitud
        - 💬 Sentiment Analysis
        - ⏱️ Time to Value
        """)
