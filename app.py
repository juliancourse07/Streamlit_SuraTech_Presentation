import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime

# ============================================
# CONFIGURACIÓN Y BRANDING SURAMERICANA
# ============================================

st.set_page_config(
    page_title="Julian Course | Propuesta SuraTech",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# COLORES OFICIALES SURAMERICANA
SURA_BLUE = "#0072CE"
SURA_CYAN = "#00C9DB"
SURA_NAVY = "#003366"
SURA_GRAY = "#9EA0A3"
SURA_WHITE = "#FFFFFF"

# CSS PERSONALIZADO CON ANIMACIONES
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    
    * {{
        font-family: 'Montserrat', sans-serif;
    }}
    
    .main {{
        background: linear-gradient(135deg, {SURA_WHITE} 0%, #E8F4F8 100%);
    }}
    
    /* Hero Section */
    .hero {{
        background: linear-gradient(135deg, {SURA_BLUE} 0%, {SURA_CYAN} 100%);
        padding: 80px 40px;
        border-radius: 20px;
        text-align: center;
        color: white;
        box-shadow: 0 10px 40px rgba(0,114,206,0.3);
        animation: fadeInUp 1s ease-out;
        margin-bottom: 40px;
    }}
    
    .hero h1 {{
        font-size: 3.5em;
        font-weight: 700;
        margin-bottom: 20px;
        animation: slideInLeft 1.2s ease-out;
    }}
    
    .hero p {{
        font-size: 1.4em;
        font-weight: 300;
        animation: slideInRight 1.2s ease-out;
    }}
    
    /* Cards Interactivas */
    .card {{
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        margin: 20px 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-left: 5px solid {SURA_CYAN};
    }}
    
    .card:hover {{
        transform: translateY(-10px);
        box-shadow: 0 15px 40px rgba(0,201,219,0.3);
    }}
    
    /* Secciones */
    .section-title {{
        color: {SURA_NAVY};
        font-size: 2.5em;
        font-weight: 700;
        margin: 60px 0 30px 0;
        border-bottom: 4px solid {SURA_CYAN};
        padding-bottom: 15px;
        animation: fadeIn 1s ease-out;
    }}
    
    /* Métricas */
    .metric-box {{
        background: linear-gradient(135deg, {SURA_BLUE} 0%, {SURA_CYAN} 100%);
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        color: white;
        box-shadow: 0 5px 15px rgba(0,114,206,0.2);
    }}
    
    .metric-number {{
        font-size: 3em;
        font-weight: 700;
    }}
    
    .metric-label {{
        font-size: 1.1em;
        font-weight: 300;
        margin-top: 10px;
    }}
    
    /* Botones */
    .stButton>button {{
        background: linear-gradient(135deg, {SURA_BLUE} 0%, {SURA_CYAN} 100%);
        color: white;
        border: none;
        padding: 15px 40px;
        font-size: 1.1em;
        font-weight: 600;
        border-radius: 50px;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,114,206,0.3);
    }}
    
    .stButton>button:hover {{
        transform: scale(1.05);
        box-shadow: 0 8px 25px rgba(0,201,219,0.5);
    }}
    
    /* Animaciones */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    @keyframes slideInLeft {{
        from {{
            opacity: 0;
            transform: translateX(-50px);
        }}
        to {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    @keyframes slideInRight {{
        from {{
            opacity: 0;
            transform: translateX(50px);
        }}
        to {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    
    /* Timeline */
    .timeline-item {{
        position: relative;
        padding-left: 40px;
        padding-bottom: 30px;
        border-left: 3px solid {SURA_CYAN};
    }}
    
    .timeline-item::before {{
        content: '';
        position: absolute;
        left: -8px;
        top: 0;
        width: 15px;
        height: 15px;
        border-radius: 50%;
        background: {SURA_CYAN};
        border: 3px solid white;
        box-shadow: 0 0 0 3px {SURA_CYAN};
    }}
    
    /* Expander personalizado */
    .streamlit-expanderHeader {{
        background: linear-gradient(135deg, {SURA_BLUE} 0%, {SURA_CYAN} 100%);
        color: white !important;
        border-radius: 10px;
        font-weight: 600;
    }}
    
    /* Tooltips */
    .tooltip {{
        position: relative;
        display: inline-block;
        cursor: help;
        color: {SURA_BLUE};
        font-weight: 600;
        border-bottom: 2px dotted {SURA_CYAN};
    }}
    
    /* Sidebar */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {SURA_NAVY} 0%, {SURA_BLUE} 100%);
    }}
    
    [data-testid="stSidebar"] * {{
        color: white !important;
    }}
</style>
""", unsafe_allow_html=True)

# ============================================
# HERO SECTION
# ============================================

st.markdown("""
<div class="hero">
    <h1>🚀 Diseñando Experiencias desde la Humanidad</h1>
    <p>Una propuesta disruptiva para Responsable de Experiencia y Procesos en SuraTech</p>
    <p style="font-size: 1em; margin-top: 20px; opacity: 0.9;">
        Por: <strong>Julian Course</strong> | Postulación para Suramericana Tech
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================
# SECCIÓN 1: MI VISIÓN
# ============================================

st.markdown('<h2 class="section-title">🎯 Mi Visión: Procesos con Alma</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div class="card">
        <h3 style="color: #0072CE;">💡 ¿Qué significa ser dueño de los procesos?</h3>
        <p style="font-size: 1.1em; line-height: 1.8;">
        Para mí, ser <strong>"dueño, amo y señor"</strong> de un proceso no es controlarlo desde la rigidez técnica, 
        sino <strong>orquestarlo desde la empatía radical</strong>.
        </p>
        <ul style="font-size: 1.05em; line-height: 2;">
            <li>🧭 <strong>Navegar la incertidumbre</strong>: Aceptar que los clientes no saben lo que necesitan hasta que lo sienten</li>
            <li>🔄 <strong>Iterar sin miedo</strong>: Fallar rápido, aprender más rápido</li>
            <li>🤝 <strong>Co-crear con multiversos</strong>: Banca, tecnología, operaciones, y sobre todo, el cliente final</li>
            <li>📊 <strong>Medir lo invisible</strong>: No solo NPS, sino momentos de verdad</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3 style="color: #00C9DB;">🌟 Mi Diferencial</h3>
        <p style="font-size: 1.1em; line-height: 1.8;">
        Vengo con una <strong>óptica holística</strong> que combina:
        </p>
        <ul style="font-size: 1.05em; line-height: 2;">
            <li>🎨 <strong>Design Thinking</strong> aplicado a seguros</li>
            <li>🧠 <strong>Psicología del usuario</strong> en momentos de estrés (siniestros, modificaciones)</li>
            <li>⚡ <strong>Agilidad</strong> sin perder la humanidad</li>
            <li>🌎 <strong>Visión regional</strong>: Entiendo LATAM, sus diferencias y puentes</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# SECCIÓN 2: EL PROBLEMA REAL
# ============================================

st.markdown('<h2 class="section-title">🔍 El Problema Real: El Viaje de María</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3 style="color: #003366;">👤 Cliente: María, 32 años, recién mamá</h3>
    <p style="font-size: 1.2em; line-height: 1.8;">
    María contrató un seguro de auto a través de su banco hace 2 años. Ahora tuvo un bebé y necesita 
    <strong>agregar cobertura de accidentes personales familiar</strong>, lo que aumenta su prima.
    </p>
</div>
""", unsafe_allow_html=True)

# Journey Map Interactivo
st.markdown("#### 🗺️ Journey Map: Del Dolor a la Solución")

journey_data = pd.DataFrame({
    'Etapa': ['Necesidad', 'Contacto', 'Espera', 'Modificación', 'Confirmación'],
    'Emoción': [3, 2, 1, 4, 5],
    'Descripción': [
        '🤔 "Necesito proteger a mi familia"',
        '📞 "Llamo al banco, me transfieren 3 veces"',
        '⏰ "Me piden documentos, demora 5 días"',
        '✅ "¡Finalmente se procesa!"',
        '😊 "Recibo confirmación clara y rápida"'
    ]
})

fig_journey = go.Figure()

fig_journey.add_trace(go.Scatter(
    x=journey_data['Etapa'],
    y=journey_data['Emoción'],
    mode='lines+markers+text',
    text=journey_data['Descripción'],
    textposition='top center',
    textfont=dict(size=10, color=SURA_NAVY),
    line=dict(color=SURA_CYAN, width=4),
    marker=dict(size=20, color=[SURA_BLUE if e < 4 else '#00D98E' for e in journey_data['Emoción']]),
    hovertemplate='<b>%{x}</b><br>Nivel emocional: %{y}<extra></extra>'
))

fig_journey.update_layout(
    title="Estado Emocional de María durante el Proceso",
    xaxis_title="Fase del Proceso",
    yaxis_title="Nivel de Satisfacción",
    yaxis=dict(range=[0, 6], tickmode='linear', tick0=0, dtick=1),
    height=400,
    template="plotly_white",
    font=dict(family="Montserrat", size=12)
)

st.plotly_chart(fig_journey, use_container_width=True)

# ============================================
# SECCIÓN 3: MI PROPUESTA DE PROCESO
# ============================================

st.markdown('<h2 class="section-title">⚙️ Proceso de Modificaciones: Mi Diseño</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3 style="color: #0072CE;">🎯 Enfoque: Modificaciones que cambian el valor a pagar</h3>
    <p style="font-size: 1.1em;">
    Este proceso es crítico porque impacta directamente el bolsillo del cliente y su percepción de valor.
    </p>
</div>
""", unsafe_allow_html=True)

# Acordeón de Metodología
with st.expander("📋 FASE 1: Empatía Radical - ¿Con quién me siento?"):
    st.markdown("""
    <div style="background: #F0F9FF; padding: 20px; border-radius: 10px; border-left: 5px solid #0072CE;">
        <h4>👥 Stakeholders Clave:</h4>
        <ul style="line-height: 2;">
            <li><strong>Cliente Final (B2C)</strong>: María y 10 personas como ella (mamás, jóvenes, adultos mayores)</li>
            <li><strong>Canal B2B</strong>: Gerente de banca del cliente, call center, asesores digitales</li>
            <li><strong>Interno SuraTech</strong>: Tech (APIs), operaciones (procesamiento), legal/compliance</li>
            <li><strong>Regulación</strong>: Superintendencia de cada país</li>
        </ul>
        
        <h4>🔍 ¿Qué investigo?</h4>
        <ul style="line-height: 2;">
            <li>🌍 <strong>Benchmarking externo</strong>: ¿Cómo lo hace Netflix al cambiar planes? ¿Spotify? ¿Mercado Libre?</li>
            <li>📊 <strong>Data interna</strong>: Tasa de abandono actual, tiempo promedio, motivos de contacto</li>
            <li>🎤 <strong>Entrevistas profundas</strong>: 15 sesiones de 1 hora con clientes que modificaron recientemente</li>
            <li>🕵️ <strong>Shadowing</strong>: Observar 20 llamadas reales de modificaciones (con consentimiento)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with st.expander("🎨 FASE 2: Ideación y Prototipado Temprano"):
    st.markdown("""
    <div style="background: #F0FFF4; padding: 20px; border-radius: 10px; border-left: 5px solid #00C9DB;">
        <h4>💡 Sesiones de Co-creación:</h4>
        <ul style="line-height: 2;">
            <li><strong>Workshop 1</strong>: Con el canal B2B - ¿Qué necesitan para vender más modificaciones?</li>
            <li><strong>Workshop 2</strong>: Con clientes - ¿Cómo imaginan el proceso ideal?</li>
            <li><strong>Workshop 3</strong>: Con tech - ¿Qué es viable en 2 semanas vs 2 meses?</li>
        </ul>
        
        <h4>🖼️ Prototipo de Baja Fidelidad:</h4>
        <p>Sketch en papel del flujo → Test con 5 usuarios → Iterar → Prototipo en Figma → Test con 15 usuarios</p>
        
        <h4>🎯 Principios del Diseño:</h4>
        <ul style="line-height: 2;">
            <li>✅ <strong>Transparencia total</strong>: Mostrar el nuevo valor ANTES de confirmar</li>
            <li>⚡ <strong>Velocidad</strong>: Resolución en < 3 minutos para modificaciones simples</li>
            <li>🤝 <strong>Opcionalidad</strong>: Ofrecer canales (app, web, teléfono, presencial)</li>
            <li>🛡️ <strong>Seguridad</strong>: Validación OTP para cambios que aumentan > 30% el valor</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with st.expander("🏗️ FASE 3: Diseño Detallado del Flujo"):
    st.markdown("### 🔄 Flujo del Proceso de Modificaciones")
    
    steps = [
        {"fase": "Inicio", "acción": "Cliente solicita modificación", "canal": "App/Web/Tel", "tiempo": "0 min", "impacto": "Alto"},
        {"fase": "Validación", "acción": "Verificar identidad y póliza", "canal": "Automático", "tiempo": "30 seg", "impacto": "Crítico"},
        {"fase": "Simulación", "acción": "Calcular nuevo valor en tiempo real", "canal": "Motor de cálculo", "tiempo": "10 seg", "impacto": "Alto"},
        {"fase": "Aprobación Cliente", "acción": "Mostrar comparativa viejo vs nuevo", "canal": "Interfaz visual", "tiempo": "2 min", "impacto": "Crítico"},
        {"fase": "Validación Negocio", "acción": "Reglas de suscripción automáticas", "canal": "Motor reglas", "tiempo": "15 seg", "impacto": "Medio"},
        {"fase": "Confirmación", "acción": "Enviar póliza actualizada + resumen", "canal": "Email/SMS/App", "tiempo": "Inmediato", "impacto": "Alto"},
        {"fase": "Seguimiento", "acción": "Encuesta contextual (a las 48hs)", "canal": "In-app message", "tiempo": "+2 días", "impacto": "Medio"}
    ]
    
    for i, step in enumerate(steps):
        color = SURA_BLUE if step["impacto"] == "Crítico" else SURA_CYAN if step["impacto"] == "Alto" else SURA_GRAY
        st.markdown(f"""
        <div class="timeline-item">
            <h4 style="color: {color};">{step["fase"]}</h4>
            <p><strong>Acción:</strong> {step["acción"]}</p>
            <p><strong>Canal:</strong> {step["canal"]} | <strong>Tiempo:</strong> {step["tiempo"]} | <strong>Impacto:</strong> {step["impacto"]}</p>
        </div>
        """, unsafe_allow_html=True)

with st.expander("📊 FASE 4: Indicadores de Impacto Potencial"):
    st.markdown("### 🎯 KPIs en Instancias Clave")
    
    metrics_data = pd.DataFrame({
        'Instancia': ['Simulación', 'Aprobación Cliente', 'Validación Negocio', 'Confirmación'],
        'KPI': ['% Abandonos', 'Tiempo decisión', 'Tasa auto-aprobación', 'Claridad percibida'],
        'Objetivo': ['< 5%', '< 3 min', '> 85%', '> 4.5/5'],
        'Cómo Medir': [
            'Analytics en funnel',
            'Timestamp de interacciones',
            'Reglas ejecutadas sin escalar',
            'Pregunta única post-proceso'
        ]
    })
    
    st.table(metrics_data)
    
    st.markdown("""
    <div style="background: #FFF4E6; padding: 20px; border-radius: 10px; margin-top: 20px;">
        <h4>💎 Indicadores Disruptivos (no el típico NPS):</h4>
        <ul style="line-height: 2;">
            <li>🎤 <strong>"Effortless Score"</strong>: "¿Qué tan fácil fue?" (escala 1-5) → Pregunta DESPUÉS de confirmar</li>
            <li>🔄 <strong>Tasa de Completitud</strong>: % que inicia Y termina el proceso</li>
            <li>💬 <strong>Sentiment Analysis</strong>: Análisis de texto en chat/email de soporte post-modificación</li>
            <li>📱 <strong>Micro-interacciones</strong>: ¿Cuántas veces vuelven a la simulación antes de decidir? (indica claridad)</li>
            <li>⏱️ <strong>Time to Value</strong>: Desde solicitud hasta póliza actualizada en mano del cliente</li>
            <li>🎁 <strong>Recomendación Implícita</strong>: % de clientes que hacen otra modificación en 6 meses (indica confianza)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# SECCIÓN 4: MEDICIÓN DE EXPERIENCIA
# ============================================

st.markdown('<h2 class="section-title">📊 Midiendo lo que Realmente Importa</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-number">⚡</div>
        <div class="metric-label">Velocidad Percibida</div>
        <p style="font-size: 0.9em; margin-top: 10px;">No cuánto tarda, sino cuán rápido SE SIENTE</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-number">🧠</div>
        <div class="metric-label">Carga Cognitiva</div>
        <p style="font-size: 0.9em; margin-top: 10px;">¿Cuánto tiene que pensar el cliente?</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-number">💚</div>
        <div class="metric-label">Confianza Generada</div>
        <p style="font-size: 0.9em; margin-top: 10px;">¿Volvería a modificar sin miedo?</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("### 🎯 Framework de Medición: B2B vs B2C")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h4 style="color: #0072CE;">👔 Cliente B2B (Banca/Canal)</h4>
        <ul style="line-height: 2;">
            <li><strong>Conversion Rate</strong>: % de modificaciones iniciadas que se completan</li>
            <li><strong>Enablement Score</strong>: ¿El canal se siente empoderado para vender modificaciones?</li>
            <li><strong>API Performance</strong>: Latencia, uptime, errores</li>
            <li><strong>Training Time</strong>: Tiempo que toma capacitar a un nuevo agente</li>
            <li><strong>Support Tickets</strong>: Cantidad de escalamientos del canal a SuraTech</li>
        </ul>
        <p><strong>Cómo:</strong> Dashboard compartido con el canal, reuniones mensuales de feedback, sesiones de co-creación trimestrales</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4 style="color: #00C9DB;">👤 Cliente B2C (Usuario Final)</h4>
        <ul style="line-height: 2;">
            <li><strong>Effortless Score</strong>: Pregunta única post-proceso</li>
            <li><strong>Completion Rate</strong>: % que inicia y termina</li>
            <li><strong>Sentiment</strong>: Análisis de texto en interacciones</li>
            <li><strong>Micro-feedback</strong>: 👍👎 en pasos clave del flujo</li>
            <li><strong>Repeat Usage</strong>: % que vuelve a usar el proceso</li>
        </ul>
        <p><strong>Cómo:</strong> In-app messages, micro-encuestas (1 pregunta), análisis de comportamiento, A/B testing continuo</p>
    </div>
    """, unsafe_allow_html=True)

# Gráfico de ejemplo de medición
st.markdown("#### 📈 Ejemplo: Evolución de Effortless Score")

weeks = pd.date_range('2026-01-01', periods=8, freq='W')
score_data = pd.DataFrame({
    'Fecha': weeks,
    'Score': [3.2, 3.5, 3.8, 4.0, 4.2, 4.4, 4.5, 4.6],
    'Objetivo': [4.5] * 8
})

fig_score = go.Figure()
fig_score.add_trace(go.Scatter(
    x=score_data['Fecha'], y=score_data['Score'],
    mode='lines+markers', name='Score Real',
    line=dict(color=SURA_CYAN, width=3),
    marker=dict(size=10)
))
fig_score.add_trace(go.Scatter(
    x=score_data['Fecha'], y=score_data['Objetivo'],
    mode='lines', name='Objetivo',
    line=dict(color=SURA_BLUE, dash='dash', width=2)
))
fig_score.update_layout(
    title="¿Qué tan fácil fue modificar tu seguro? (1=Muy difícil, 5=Muy fácil)",
    yaxis=dict(range=[0, 5]),
    template="plotly_white",
    font=dict(family="Montserrat")
)
st.plotly_chart(fig_score, use_container_width=True)

# ============================================
# SECCIÓN 5: EXPANSIÓN REGIONAL
# ============================================

st.markdown('<h2 class="section-title">🌎 Expansión Inteligente: De País X a País Y</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3 style="color: #003366;">🧩 El Desafío: Mismo proceso, múltiples realidades</h3>
    <p style="font-size: 1.1em; line-height: 1.8;">
    Cuando un proceso funciona en Colombia pero debe implementarse en Chile, Perú o México, 
    necesitamos distinguir entre lo <strong>universal</strong> y lo <strong>local</strong>.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card" style="border-left-color: #00D98E;">
        <h4 style="color: #00D98E;">✅ Elementos TRANSVERSALES (Reutilizables)</h4>
        <ul style="line-height: 2;">
            <li>🎨 <strong>Principios de UX</strong>: Transparencia, velocidad, opcionalidad</li>
            <li>🏗️ <strong>Arquitectura técnica base</strong>: APIs, motor de cálculo, flujo de datos</li>
            <li>📊 <strong>Framework de métricas</strong>: Qué medir (aunque los targets varíen)</li>
            <li>🧠 <strong>Metodología de diseño</strong>: Empatía radical, prototipado temprano</li>
            <li>🔄 <strong>Lógica de negocio genérica</strong>: Validación, simulación, confirmación</li>
            <li>📱 <strong>Componentes UI</strong>: Sistema de diseño (botones, forms, colores Sura)</li>
            <li>🎓 <strong>Playbooks de capacitación</strong>: Estructura de onboarding de canales</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card" style="border-left-color: #FF6B6B;">
        <h4 style="color: #FF6B6B;">🎯 Elementos LOCALES (Adaptación Obligatoria)</h4>
        <ul style="line-height: 2;">
            <li>⚖️ <strong>Regulación</strong>: Superintendencia de cada país (tiempos, aprobaciones, documentación)</li>
            <li>💰 <strong>Medios de pago</strong>: Efectivo, tarjetas, transferencias locales</li>
            <li>🗣️ <strong>Lenguaje y tono</strong>: "Póliza" vs "Seguro", "Vos" vs "Tú", formalidad</li>
            <li>📅 <strong>Comportamientos culturales</strong>: Preferencia por teléfono vs digital</li>
            <li>📞 <strong>Canales dominantes</strong>: WhatsApp en México, SMS en otros</li>
            <li>🏦 <strong>Integración con Banca</strong>: Sistemas legacy, APIs disponibles</li>
            <li>📊 <strong>Contexto competitivo</strong>: ¿Qué hacen los competidores locales?</li>
            <li>🎨 <strong>Expectativas de servicio</strong>: Velocidad esperada, soporte 24/7 o no</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("### 🛠️ Mi Checklist de Expansión")

expansion_checklist = pd.DataFrame({
    'Paso': [
        '1. Inmersión Local',
        '2. Mapeo Regulatorio',
        '3. Adaptación del Diseño',
        '4. Piloto Controlado',
        '5. Escalamiento'
    ],
    'Acción Clave': [
        'Entrevistar 10 clientes locales + 5 del canal B2B',
        'Workshop con legal local + benchmarking competencia',
        'Adaptar lenguaje, canales y flujos según feedback',
        'Lanzar con 1 canal en 1 ciudad, medir 4 semanas',
        'Replicar con ajustes, automatizar onboarding'
    ],
    'Output': [
        'Documento de insights locales',
        'Matriz de restricciones regulatorias',
        'Prototipo adaptado + tests de usabilidad',
        'Dashboard de métricas + aprendizajes',
        'Playbook de expansión actualizado'
    ]
})

st.table(expansion_checklist)

# ============================================
# SECCIÓN 6: CIERRE INSPIRADOR
# ============================================

st.markdown('<h2 class="section-title">💫 Por Qué Yo para Este Rol</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="hero" style="background: linear-gradient(135deg, #003366 0%, #0072CE 100%);">
    <h3 style="margin-bottom: 30px;">🎯 Mi Propuesta de Valor</h3>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; text-align: left;">
        <div>
            <h4>🧠 Pensamiento Holístico</h4>
            <p>Veo el proceso como un ecosistema, no como pasos aislados</p>
        </div>
        <div>
            <h4>❤️ Empatía Radical</h4>
            <p>Diseño desde el miedo, la urgencia y la esperanza del cliente</p>
        </div>
        <div>
            <h4>⚡ Ejecución Ágil</h4>
            <p>Prototipo rápido, mido más rápido, aprendo aún más rápido</p>
        </div>
        <div>
            <h4>🌎 Visión Regional</h4>
            <p>Entiendo las diferencias sin perder la coherencia de marca</p>
        </div>
    </div>
    <p style="margin-top: 40px; font-size: 1.3em;">
        <strong>No solo diseño procesos. Diseño momentos que transforman la relación cliente-marca.</strong>
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================

st.markdown("---")

st.markdown(f"""
<div style="text-align: center; padding: 40px; background: #F8F9FA; border-radius: 15px; margin-top: 40px;">
    <p style="font-size: 1.2em; color: {SURA_NAVY}; margin-bottom: 20px;">
        <strong>¿Listo para co-crear el futuro de seguros digitales en LATAM?</strong>
    </p>
    <p style="font-size: 1em; color: {SURA_GRAY};">
        📧 ebetancurc@sura.com | 🚀 Preparado por Julian Course para SuraTech
    </p>
    <p style="font-size: 0.9em; color: {SURA_GRAY}; margin-top: 20px;">
        Desarrollado con ❤️ y Streamlit | Branding oficial Suramericana | {datetime.now().strftime('%Y')}
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================
# SIDEBAR (Navegación opcional)
# ============================================

with st.sidebar:
    st.image("https://www.sura.com/Style%20Library/Sura/Assets/images/header-sura-logo.png", width=200)
    st.markdown("### 📍 Navegación Rápida")
    st.markdown("""
    - 🎯 Mi Visión
    - 🔍 El Problema
    - ⚙️ Mi Propuesta
    - 📊 Medición
    - 🌎 Expansión
    - 💫 Cierre
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Métricas de esta app")
    st.info("Desarrollada en 1 sprint\nCon empatía radical 💙")
