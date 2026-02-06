import streamlit as st
from datetime import datetime

# ═══════════════════════════════════════════════════════════════
# CONFIGURACIÓN INICIAL
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Julian Course | Mi Propuesta para SuraTech",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ═══════════════════════════════════════════════════════════════
# COLORES
# ═══════════════════════════════════════════════════════════════
COLORS = {
    "primary": "#044B93",
    "secondary": "#00A99D",
    "accent": "#16BBE5",
    "light": "#F0F5FA",
    "dark": "#222222",
}

# ═══════════════════════════════════════════════════════════════
# CSS
# ═══════════════════════════════════════════════════════════════
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
    
    * {{
        font-family: 'Poppins', sans-serif;
    }}
    
    .main {{
        background: linear-gradient(135deg, {COLORS['light']} 0%, #FFFFFF 100%);
    }}
    
    .hero {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['accent']} 100%);
        padding: 80px 50px;
        border-radius: 20px;
        color: white;
        margin-bottom: 50px;
        box-shadow: 0 15px 40px rgba(4, 75, 147, 0.25);
    }}
    
    .hero h1 {{
        font-size: 3.5em;
        font-weight: 800;
        margin: 0 0 15px 0;
    }}
    
    .hero p {{
        font-size: 1.4em;
        margin: 0;
        opacity: 0.95;
    }}
    
    .card {{
        background: white;
        border-radius: 15px;
        padding: 35px;
        margin: 25px 0;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
        border-left: 6px solid {COLORS['primary']};
        transition: all 0.3s;
    }}
    
    .card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
    }}
    
    .card.secondary {{
        border-left-color: {COLORS['secondary']};
    }}
    
    .card.accent {{
        border-left-color: {COLORS['accent']};
    }}
    
    .section-title {{
        color: {COLORS['primary']};
        font-size: 2.5em;
        font-weight: 800;
        margin: 50px 0 25px 0;
        padding-bottom: 20px;
        border-bottom: 4px solid {COLORS['secondary']};
    }}
    
    .highlight {{
        background: linear-gradient(120deg, {COLORS['accent']}20, {COLORS['secondary']}20);
        padding: 25px;
        border-radius: 12px;
        margin: 20px 0;
        border-left: 5px solid {COLORS['secondary']};
    }}
    
    .metric-box {{
        background: linear-gradient(135deg, {COLORS['primary']}08, {COLORS['accent']}08);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        border-top: 4px solid {COLORS['primary']};
    }}
    
    .metric-value {{
        font-size: 2.8em;
        font-weight: 800;
        color: {COLORS['primary']};
        margin: 15px 0;
    }}
    
    .metric-label {{
        color: {COLORS['dark']};
        font-size: 0.95em;
        font-weight: 600;
        text-transform: uppercase;
    }}
    
    .footer {{
        background: linear-gradient(135deg, {COLORS['primary']}05, {COLORS['accent']}05);
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        margin-top: 60px;
        border-top: 3px solid {COLORS['secondary']};
    }}
    </style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""
    <div class="hero">
        <h1>🚀 Mi Aporte a SuraTech</h1>
        <p>Diseño de procesos centrado en la humanidad, no en la tecnología</p>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1.6, 1.4])

with col1:
    st.markdown(f"""
    <div class="card">
        <h3 style="color: {COLORS['primary']}; margin-top: 0;">🎯 Mi Filosofía</h3>
        <p style="font-size: 1.05em; line-height: 1.8;">
            No soy un técnico que intenta entender a las personas.
        </p>
        <p style="font-size: 1.05em; line-height: 1.8; color: {COLORS['secondary']}; font-weight: 600;">
            Soy alguien que entiende a las personas primero.
        </p>
        <hr style="border: none; border-top: 2px solid {COLORS['light']}; margin: 20px 0;">
        <p style="color: #666; font-style: italic;">
            Los procesos no fallan por software. Fallan porque no entendemos la realidad del cliente.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Mi Enfoque</div>
        <div class="metric-value">Holístico</div>
        <p style="color: #666;">100% Centrado en Humanidad</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SECTION 1
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""<h2 class="section-title">📍 El Problema: Modificación de Seguros</h2>""", unsafe_allow_html=True)

st.markdown("""
**El cliente llama y dice:** *"Quiero cambiar algo"*

**Lo que eso realmente significa:**
- Una vida que cambió (nuevo trabajo, nueva casa, más hijos)
- Una decisión en 5 minutos, pero con impacto en todo
- Un proceso que será frustrante si no lo diseñamos bien
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">⏱️ Tiempo Dedicado</div>
        <div class="metric-value">15 min</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">😤 Puntos de Frustración</div>
        <div class="metric-value">6-8</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">📈 Impacto Real</div>
        <div class="metric-value">3x</div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SECTION 2
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""<h2 class="section-title">🧭 Cómo Yo Diseñaría Este Proceso</h2>""", unsafe_allow_html=True)

st.markdown(f"""
<div class="card secondary">
    <h3 style="color: {COLORS['secondary']}; margin-top: 0;">Paso 1: Empatía Radical</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="highlight">
        <h4 style="color: {COLORS['primary']}; margin-top: 0;">👥 Con Quién Me Siento</h4>
        <ul>
            <li><strong>El cliente final</strong> — quien tiene miedo de cambiar</li>
            <li><strong>El ejecutivo de cuenta</strong> — quien recibe el llamado</li>
            <li><strong>Reclamaciones</strong> — quien ve las confusiones</li>
            <li><strong>Sistemas</strong> — quien dice "es complejo"</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="highlight">
        <h4 style="color: {COLORS['primary']}; margin-top: 0;">🔍 Qué Miro</h4>
        <ul>
            <li><strong>Afuera:</strong> ¿Qué pas�� en la vida del cliente?</li>
            <li><strong>Adentro:</strong> ¿Dónde se rompe el proceso?</li>
            <li><strong>Conversaciones:</strong> Entrevistas reales</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
<div class="highlight">
    <h3 style="color: {COLORS['primary']}; margin-top: 0;">💡 Insight Clave</h3>
    <p style="font-size: 1.1em;">
        La gente no quiere un "proceso de modificación". 
        <br><strong style="color: {COLORS['secondary']};">Quiere paz mental</strong> de que su cambio está correcto.
    </p>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SECTION 3
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""<h2 class="section-title">🔄 El Proceso Rediseñado</h2>""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 Flujo Visual", "💡 Detalles", "🎯 Particularidades"])

with tab1:
    st.markdown("""
    **Los 7 Pasos del Proceso:**
    
    1. 📞 **Cliente Llama** — Momento crítico
    2. 👂 **Escucha Real** — Sin interrumpir
    3. ❓ **Clarificación** — ¿Qué? ¿Cuándo? ¿Por qué?
    4. 📊 **Simulación en Tiempo Real** — Mostrar impacto
    5. ✅ **Confirmación Explícita** — Cliente dice SÍ
    6. 📄 **Documentación Clara** — En lenguaje humano
    7. 🔔 **Confirmación Recurrente** — 24h y 7 días después
    """)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="card secondary">
            <h4 style="color: {COLORS['secondary']}; margin-top: 0;">🎧 Escucha Real</h4>
            <p><strong>Qué:</strong> El ejecutivo escucha sin formularios</p>
            <p><strong>Por qué:</strong> Los formularios omiten contexto</p>
            <p><strong>Cómo:</strong> 2 minutos conversación > 10 minutos formulario</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="card accent">
            <h4 style="color: {COLORS['accent']}; margin-top: 0;">📊 Simulación</h4>
            <p><strong>Qué:</strong> El cliente ve ANTES de confirmar</p>
            <p><strong>Por qué:</strong> Reduce reclamaciones por sorpresa</p>
            <p><strong>Cómo:</strong> Tabla: Anterior | Nuevo | Diferencia</p>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown(f"""
    <div class="card secondary">
        <h3 style="color: {COLORS['secondary']}; margin-top: 0;">🎯 Particularidades</h3>
        
        <h4 style="color: {COLORS['primary']};">1️⃣ Tipo de Seguro Importa</h4>
        <ul>
            <li><strong>Vida:</strong> Cliente tiene miedo a cambiar cobertura</li>
            <li><strong>Auto:</strong> Cliente quiere que sea rápido</li>
            <li><strong>Hogar:</strong> Cliente compara con competencia</li>
        </ul>
        
        <h4 style="color: {COLORS['primary']};">2️⃣ El Deducible es CRÍTICO</h4>
        <p>El cliente asume que bajar deducible = menos riesgo. Pero es lo opuesto: paga menos CUANDO algo malo sucede.</p>
        
        <h4 style="color: {COLORS['primary']};">3️⃣ Cobertura Adicional >> Reducida</h4>
        <p>Es 10x más fácil vender más cobertura. Si el cliente quiere PERDER protección, es bandera roja.</p>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SECTION 4
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""<h2 class="section-title">📈 Cómo Medimos</h2>""", unsafe_allow_html=True)

st.markdown("### Para el Cliente B2C (Final)")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">⏱️ Tiempo Procesamiento</div>
        <div class="metric-value">48h</div>
        <p style="color: {COLORS['secondary']}; font-weight: 600;">Meta: 24h</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">📉 Reclamaciones Reducidas</div>
        <div class="metric-value">-40%</div>
        <p style="color: #28A745; font-weight: 600;">Por confirmación explícita</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">🤝 Referrals</div>
        <div class="metric-value">+25%</div>
        <p style="color: #28A745; font-weight: 600;">Cliente recomienda</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### Para el Cliente B2B (Canal)")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">🔌 Disponibilidad APIs</div>
        <div class="metric-value">95%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">✅ Documentación</div>
        <div class="metric-value">100%</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">😊 Satisfacción Equipo</div>
        <div class="metric-value">⭐⭐⭐⭐</div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SECTION 5
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""<h2 class="section-title">🌎 Expansión Regional</h2>""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="card accent">
        <h4 style="color: {COLORS['accent']}; margin-top: 0;">✅ Elementos Transversales (Reutilizar)</h4>
        <ul>
            <li>Estructura: Escucha → Simulación → Confirmación → Follow-up</li>
            <li>Principio: Transparencia ANTES de acción</li>
            <li>KPI: Reclamaciones por confusión</li>
            <li>API estándar para cambios</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card secondary">
        <h4 style="color: {COLORS['secondary']}; margin-top: 0;">🌍 Elementos Locales (Adaptar)</h4>
        <ul>
            <li><strong>Regulación:</strong> Colombia ≠ Chile ≠ Uruguay</li>
            <li><strong>Canales:</strong> WhatsApp, SMS, email</li>
            <li><strong>Horarios:</strong> Zona horaria + cultura</li>
            <li><strong>Documentación:</strong> Firma digital vs. física</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# RESUMEN
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""<h2 class="section-title">💬 Mi Propuesta en Síntesis</h2>""", unsafe_allow_html=True)

st.markdown(f"""
<div class="card secondary">
    <p style="font-size: 1.15em; line-height: 2;">
        No vengo a "digitalizar" todo. Vengo a diseñar procesos donde:
    </p>
    
    <ul style="font-size: 1.05em; line-height: 2;">
        <li>✅ El <strong>cliente</strong> entiende qué pasa en cada paso</li>
        <li>✅ El <strong>ejecutivo de cuenta</strong> tiene herramientas para ayudar</li>
        <li>✅ El <strong>equipo interno</strong> trabaja en casos que importan</li>
        <li>✅ <strong>Suramericana</strong> crece por confianza, no por precio barato</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""
<div class="footer">
    <h3 style="margin-top: 0;">Julian Course</h3>
    <p style="font-size: 1.1em; color: {COLORS['primary']}; font-weight: 600;">
        Responsable de Experiencia y Procesos
    </p>
    <p style="font-style: italic; color: #666;">
        Diseñador de procesos centrado en humanidad
    </p>
    
    <hr style="border: none; border-top: 2px solid {COLORS['light']}; margin: 20px 0;">
    
    <p style="color: {COLORS['primary']}; font-weight: 600;">
        📧 Enviar a: <strong>ebetancurc@sura.com</strong>
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown(f"""
<div style="text-align: center; padding: 20px; color: #999; font-size: 0.85em;">
    <p>Propuesta creada con Streamlit | {datetime.now().strftime('%Y')}</p>
</div>
""", unsafe_allow_html=True)
