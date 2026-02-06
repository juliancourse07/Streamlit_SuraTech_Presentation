import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
import requests
from io import BytesIO

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
# PALETA DE COLORES SURAMERICANA
# ═══════════════════════════════════════════════════════════════
COLORS = {
    "primary": "#044B93",      # Azul SURA corporativo
    "secondary": "#00A99D",    # Verde dinámico
    "accent": "#16BBE5",       # Celeste moderno
    "light": "#F0F5FA",        # Fondo claro
    "dark": "#222222",         # Texto oscuro
    "white": "#FFFFFF",
    "success": "#28A745",
    "warning": "#FFC107",
    "danger": "#E74C3C"
}

# ═══════════════════════════════════════════════════════════════
# CSS PERSONALIZADO - BRANDING DINÁMICO
# ═══════════════════════════════════════════════════════════════
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
    
    * {{
        font-family: 'Poppins', sans-serif;
    }}
    
    .main {{
        background: linear-gradient(135deg, {COLORS['light']} 0%, {COLORS['white']} 100%);
    }}
    
    /* HERO SECTION */
    .hero {{
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['accent']} 100%);
        padding: 80px 50px;
        border-radius: 20px;
        color: white;
        margin-bottom: 50px;
        box-shadow: 0 15px 40px rgba(4, 75, 147, 0.25);
        animation: slideDown 0.8s ease-out;
        position: relative;
        overflow: hidden;
    }}
    
    .hero::before {{
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        border-radius: 50%;
    }}
    
    .hero-content {{
        position: relative;
        z-index: 1;
    }}
    
    .hero h1 {{
        font-size: 3.5em;
        font-weight: 800;
        margin: 0 0 15px 0;
        line-height: 1.1;
        letter-spacing: -2px;
    }}
    
    .hero p {{
        font-size: 1.4em;
        margin: 0;
        opacity: 0.95;
        font-weight: 500;
    }}
    
    @keyframes slideDown {{
        from {{
            opacity: 0;
            transform: translateY(-30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    /* CARDS */
    .card {{
        background: white;
        border-radius: 15px;
        padding: 35px;
        margin: 25px 0;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
        border-left: 6px solid {COLORS['primary']};
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
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
    
    .card.danger {{
        border-left-color: {COLORS['danger']};
    }}
    
    /* SECTION TITLES */
    .section-title {{
        color: {COLORS['primary']};
        font-size: 2.5em;
        font-weight: 800;
        margin: 50px 0 25px 0;
        padding-bottom: 20px;
        border-bottom: 4px solid {COLORS['secondary']};
        display: flex;
        align-items: center;
        gap: 15px;
    }}
    
    /* HIGHLIGHTS */
    .highlight {{
        background: linear-gradient(120deg, {COLORS['accent']}20, {COLORS['secondary']}20);
        padding: 25px;
        border-radius: 12px;
        margin: 20px 0;
        border-left: 5px solid {COLORS['secondary']};
    }}
    
    .highlight strong {{
        color: {COLORS['primary']};
    }}
    
    /* METRIC BOXES */
    .metric-box {{
        background: linear-gradient(135deg, {COLORS['primary']}08, {COLORS['accent']}08);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        border-top: 4px solid {COLORS['primary']};
        transition: transform 0.3s;
    }}
    
    .metric-box:hover {{
        transform: translateY(-5px);
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
        letter-spacing: 1px;
    }}
    
    .metric-description {{
        color: #666;
        font-size: 0.9em;
        margin-top: 10px;
    }}
    
    /* PROCESS FLOW */
    .flow-step {{
        background: white;
        padding: 25px;
        border-radius: 12px;
        margin: 15px 0;
        display: flex;
        gap: 20px;
        align-items: flex-start;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        border-left: 5px solid {COLORS['secondary']};
    }}
    
    .flow-step.critical {{
        border-left-color: {COLORS['danger']};
        background: rgba({int('E7', 16)}, {int('4C', 16)}, {int('3C', 16)}, 0.05);
    }}
    
    .step-icon {{
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, {COLORS['primary']}, {COLORS['accent']});
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.8em;
        font-weight: bold;
        flex-shrink: 0;
    }}
    
    .step-content h4 {{
        color: {COLORS['primary']};
        margin: 0 0 10px 0;
        font-size: 1.1em;
    }}
    
    .step-content p {{
        margin: 0;
        color: #666;
        font-size: 0.95em;
        line-height: 1.6;
    }}
    
    /* TABS STYLING */
    .streamlit-tabs {{
        background: white;
        border-radius: 12px;
        padding: 20px;
    }}
    
    /* CTA BUTTON */
    .cta-button {{
        background: linear-gradient(135deg, {COLORS['secondary']}, {COLORS['primary']});
        color: white;
        padding: 15px 40px;
        border-radius: 50px;
        border: none;
        font-weight: 700;
        font-size: 1.1em;
        cursor: pointer;
        transition: all 0.3s;
        display: inline-block;
        text-decoration: none;
        box-shadow: 0 5px 20px rgba(0, 169, 157, 0.3);
    }}
    
    .cta-button:hover {{
        transform: scale(1.05);
        box-shadow: 0 8px 30px rgba(0, 169, 157, 0.4);
    }}
    
    /* FOOTER */
    .footer {{
        background: linear-gradient(135deg, {COLORS['primary']}05, {COLORS['accent']}05);
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        margin-top: 60px;
        border-top: 3px solid {COLORS['secondary']};
    }}
    
    .footer h3 {{
        color: {COLORS['primary']};
        margin: 0 0 10px 0;
    }}
    
    .footer p {{
        color: #666;
        margin: 5px 0;
    }}
    
    /* RESPONSIVE */
    @media (max-width: 768px) {{
        .hero {{
            padding: 40px 25px;
        }}
        
        .hero h1 {{
            font-size: 2em;
        }}
        
        .section-title {{
            font-size: 1.8em;
        }}
        
        .flow-step {{
            flex-direction: column;
            gap: 10px;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# HERO SECTION - MI PROPUESTA
# ═══════════════════════════════════════════════════════════════
st.markdown(f"""
    <div class="hero">
        <div class="hero-content">
            <h1>🚀 Mi Aporte a SuraTech</h1>
            <p>Diseño de procesos centrado en la humanidad, no en la tecnología</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# INTRODUCCIÓN - MI FILOSOFÍA
# ═══════════════════════════════════════════════════════════════

col1, col2 = st.columns([1.6, 1.4], gap="large")

with col1:
    st.markdown(f"""
    <div class="card">
        <h3 style="color: {COLORS['primary']}; margin-top: 0;">🎯 Mi Filosofía</h3>
        <p style="font-size: 1.05em; line-height: 1.8;">
            No soy un técnico que intenta entender a las personas.
        </p>
        <p style="font-size: 1.05em; line-height: 1.8; color: {COLORS['secondary']}; font-weight: 600;">
            Soy alguien que entiende a las personas primero, y luego busco la tecnología que las sirve.
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
        <div class="metric-description">100% Centrado en Humanidad</div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SECTION 1: EL PROBLEMA
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""<h2 class="section-title">📍 El Problema: Modificación de Seguros</h2>""", unsafe_allow_html=True)

st.markdown("""
**El cliente llama y dice:** *"Quiero cambiar algo"*

**Lo que eso realmente significa:**
- Una vida que cambió (nuevo trabajo, nueva casa, más hijos, mudanza)
- Una decisión tomada en 5 minutos, pero con impacto en todo
- Un proceso que probablemente será frustrante si no lo diseñamos bien
"")

# Visualización del problema actual
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">⏱️ Tiempo Dedicado</div>
        <div class="metric-value">15 min</div>
        <div class="metric-description">Para un cambio que afecta su protección</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">😤 Puntos de Frustración</div>
        <div class="metric-value">6-8</div>
        <div class="metric-description">En la jornada actual</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">📈 Impacto Real</div>
        <div class="metric-value">3x</div>
        <div class="metric-description">Más reclamaciones por confusión</div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SECTION 2: MI ENFOQUE
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""<h2 class="section-title">🧭 Cómo Yo Diseñaría Este Proceso</h2>""", unsafe_allow_html=True)

# Tab 1: Empatía Radical
st.markdown(f"""
<div class="card secondary">
    <h3 style="color: {COLORS['secondary']}; margin-top: 0;">Paso 1: Empatía Radical (La Base)</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown(f"""
    <div class="highlight">
        <h4 style="color: {COLORS['primary']}; margin-top: 0;">👥 Con Quién Me Siento</h4>
        <ul style="margin: 10px 0;">
            <li><strong>El cliente final</strong> — quien tiene miedo de cambiar y que se dañe algo</li>
            <li><strong>El ejecutivo de cuenta</strong> — quien recibe el llamado y no sabe bien qué hacer</li>
            <li><strong>Reclamaciones</strong> — quien ve las confusiones después</li>
            <li><strong>Sistemas</strong> — quien dice "pero eso es complejo"</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="highlight">
        <h4 style="color: {COLORS['primary']}; margin-top: 0;">🔍 Qué Miro</h4>
        <ul style="margin: 10px 0;">
            <li><strong>Afuera:</strong> ¿Qué está pasando en la vida del cliente que lo hizo llamar HOY?</li>
            <li><strong>Adentro:</strong> ¿Dónde se rompe el proceso? ¿Dónde pierde confianza?</li>
            <li><strong>Conversaciones:</strong> Entrevistas reales, no formularios</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
<div class="highlight">
    <h3 style="color: {COLORS['primary']}; margin-top: 0;">💡 Insight Clave</h3>
    <p style="font-size: 1.1em; line-height: 1.8;">
        La gente no quiere un <em>"proceso de modificación"</em>. 
        <br><strong style="color: {COLORS['secondary']};">Quiere paz mental</strong> de que su cambio está correcto y que su protección sigue vigente.
    </p>
</div>
""", unsafe_allow_html=True)

# No linealidad
st.markdown(f"""
<div class="card accent">
    <h3 style="color: {COLORS['accent']}; margin-top: 0;">Paso 2: No Linealidad - Iteración Rápida</h3>
    <p>No diseño en waterfall. Diseño en ciclos pequeños:</p>
    
    <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
        <tr style="background: {COLORS['light']};">
            <td style="padding: 12px; border: 1px solid {COLORS['accent']}; font-weight: 600; color: {COLORS['primary']};">1️⃣ Prototipo Humano</td>
            <td style="padding: 12px; border: 1px solid {COLORS['accent']};">Simulo el cambio en una hoja, viendo qué dice el cliente</td>
        </tr>
        <tr>
            <td style="padding: 12px; border: 1px solid {COLORS['accent']}; font-weight: 600; color: {COLORS['primary']};">2️⃣ Test con 5 Clientes</td>
            <td style="padding: 12px; border: 1px solid {COLORS['accent']};">Veo dónde dudan, dónde se confunden</td>
        </tr>
        <tr style="background: {COLORS['light']};">
            <td style="padding: 12px; border: 1px solid {COLORS['accent']}; font-weight: 600; color: {COLORS['primary']};">3️⃣ Ajusto el Flujo</td>
            <td style="padding: 12px; border: 1px solid {COLORS['accent']};">Cambio, no espero a que sea perfecto</td>
        </tr>
        <tr>
            <td style="padding: 12px; border: 1px solid {COLORS['accent']}; font-weight: 600; color: {COLORS['primary']};">4️⃣ Repito</td>
            <td style="padding: 12px; border: 1px solid {COLORS['accent']};">Hasta que el cliente dice "así sí tiene sentido"</td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SECTION 3: EL FLUJO REDISEÑADO
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""<h2 class="section-title">🔄 El Proceso Rediseñado</h2>""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 Flujo Visual", "💡 Detalles", "🎯 Particularidades"])

with tab1:
    st.markdown(f"""
    <div style="background: white; padding: 30px; border-radius: 15px; border-left: 6px solid {COLORS['primary']};">
    """, unsafe_allow_html=True)
    
    # Flujo paso a paso
    steps = [
        {
            "icon": "📞",
            "title": "Cliente Llama / Contacta",
            "description": "Momento crítico: el cliente está decidiendo si continuar",
            "critical": True
        },
        {
            "icon": "👂",
            "title": "Escucha Real",
            "description": "Sin interrumpir. El ejecutivo entiende QUÉ NECESITA cambiar"
        },
        {
            "icon": "❓",
            "title": "Clarificación Inmediata",
            "description": "¿Qué te hizo llamar? ¿Qué necesitas cambiar? ¿Cuándo? ¿Por qué?"
        },
        {
            "icon": "📊",
            "title": "Simulación en Tiempo Real",
            "description": "Mostrar impacto inmediato (Anterior vs. Nuevo vs. Diferencia)",
            "critical": True
        },
        {
            "icon": "✅",
            "title": "Confirmación Explícita",
            "description": "Cliente dice SÍ de forma clara y documentada",
            "critical": True
        },
        {
            "icon": "📄",
            "title": "Documentación Clara",
            "description": "Resumen en lenguaje humano (No contrato)"
        },
        {
            "icon": "🔔",
            "title": "Confirmación Recurrente",
            "description": "24h y 7 días después: 'Tu cambio está procesado. ¿Dudas?'
        }
    ]
    
    for idx, step in enumerate(steps, 1):
        critical_class = " critical" if step.get("critical") else ""
        st.markdown(f"""
        <div class="flow-step{critical_class}">
            <div class="step-icon">{step['icon']}</div>
            <div class="step-content">
                <h4>{idx}. {step['title']}</h4>
                <p>{step['description']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown(f"""
        <div class="card secondary">
            <h4 style="color: {COLORS['secondary']}; margin-top: 0;">🎧 Escucha Real</h4>
            <p><strong>Qué:</strong> El ejecutivo escucha sin llenar formularios</p>
            <p><strong>Por qué:</strong> Las formas hacen que el cliente omita contexto importante</p>
            <p><strong>Cómo:</strong> 2 minutos de conversación > 10 minutos de formulario tedioso</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="card accent">
            <h4 style="color: {COLORS['accent']}; margin-top: 0;">📊 Simulación Transparente</h4>
            <p><strong>Qué:</strong> El cliente ve ANTES de confirmar</p>
            <p><strong>Por qué:</strong> Reduce reclamaciones por "sorpresa"</p>
            <p><strong>Cómo:</strong> Tabla clara: Anterior | Nuevo | Diferencia</p>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown(f"""
        <div class="card">
            <h4 style="color: {COLORS['primary']}; margin-top: 0;">✅ Confirmación Explícita</h4>
            <p><strong>Qué:</strong> Cliente dice SÍ de forma clara y documentada</p>
            <p><strong>Por qué:</strong> Evita reclamaciones de "no pedí eso"</p>
            <p><strong>Cómo:</strong> Pregunta clara + firma digital/verificación</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="card secondary">
            <h4 style="color: {COLORS['secondary']}; margin-top: 0;">🔔 Follow-up Empático</h4>
            <p><strong>Qué:</strong> Confirmación del cambio 24h y 7 días después</p>
            <p><strong>Por qué:</strong> Genera confianza, reduce ansiedad</p>
            <p><strong>Cómo:</strong> "Tu cambio está listo. ¿Tienes dudas?"</p>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown(f"""
    <div class="card secondary">
        <h3 style="color: {COLORS['secondary']}; margin-top: 0;">🎯 Particularidades para Este Proceso</h3>
        
        <h4 style="color: {COLORS['primary']}; margin-top: 20px;">1️⃣ Tipo de Seguro Importa</h4>
        <ul style="margin: 10px 0;">
            <li><strong>Vida:</strong> Cliente tiene miedo a cambiar cobertura (¿si me pasa algo?)</li>
            <li><strong>Auto:</strong> Cliente quiere que sea rápido (ocupado, ansioso)</li>
            <li><strong>Hogar:</strong> Cliente compara (con competencia)</li>
        </ul>
        
        <h4 style="color: {COLORS['primary']}; margin-top: 20px;">2️⃣ El Deducible es CRÍTICO</h4>
        <p>
            Cuando el cliente quiere bajar el deducible (pagar más cuota), asume que hay <strong>menos riesgo</strong>.
            <br><strong style="color: {COLORS['danger']};">Nuestro trabajo:</strong> Que entienda que es lo opuesto: paga <strong>menos dinero cuando algo malo sucede</strong>.
        </p>
        
        <h4 style="color: {COLORS['primary']}; margin-top: 20px;">3️⃣ Cobertura Adicional >> Cobertura Reducida</h4>
        <p>
            Es <strong>10x más fácil</strong> vender más cobertura que convencer a alguien de "perder" algo.
            <br>Si el cliente quiere cambiar de forma que <strong>pierda protección</strong>, esa es <strong style="color: {COLORS['danger']};">bandera roja</strong> de que NO entiende.
        </p>
        
        <h4 style="color: {COLORS['primary']}; margin-top: 20px;">4️⃣ Integración Sistémica</h4>
        <ul style="margin: 10px 0;">
            <li>Si cambio cobertura, ¿qué pasa en facturación?</li>
            <li>¿El cambio es efectivo ya o es futuro?</li>
            <li>¿Se afecta documentación regulatoria?</li>
            <li>¿Impacta en sistemas de terceros (reaseguro, etc.)?</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SECTION 4: MÉTRICAS
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""<h2 class="section-title">📈 Cómo Medimos (Sin Encuestas Tedias)</h2>""", unsafe_allow_html=True)

st.markdown("""
### Para el Cliente B2C (Final)
"")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">⏱️ Tiempo Procesamiento</div>
        <div class="metric-value">48h</div>
        <p style="color: {COLORS['secondary']}; font-weight: 600;">Meta: Reducir a 24h</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">📉 Reclamaciones "No Solicitado"</div>
        <div class="metric-value">-40%</div>
        <p style="color: {COLORS['success']}; font-weight: 600;">Por confirmación explícita</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">🤝 Referrals Generados</div>
        <div class="metric-value">+25%</div>
        <p style="color: {COLORS['success']}; font-weight: 600;">Cliente recomienda por experiencia</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
### Para el Cliente B2B (Canal)
"")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">🔌 Disponibilidad APIs</div>
        <div class="metric-value">95%</div>
        <p style="color: {COLORS['warning']}; font-weight: 600;">Meta: 99.5%</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">✅ Documentación Regulatoria</div>
        <div class="metric-value">100%</div>
        <p style="color: {COLORS['success']}; font-weight: 600;">Cero inconsistencias</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">😊 Satisfacción del Equipo</div>
        <div class="metric-value">⭐⭐⭐⭐</div>
        <p style="color: {COLORS['success']}; font-weight: 600;">Menos manual, más estrategia</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
<div class="highlight">
    <h4 style="color: {COLORS['primary']}; margin-top: 0;">🔍 Cómo Medimos EN LA REALIDAD</h4>
    <ul style="margin: 10px 0; line-height: 1.8;">
        <li><strong>Behavioral:</strong> ¿El cliente vuelve? ¿Tarda menos en procesar?</li>
        <li><strong>Cualitativo:</strong> Entrevistas con 5-10 clientes/mes (conversación, no encuesta)</li>
        <li><strong>Operativo:</strong> ¿Menos back-and-forth? ¿Menos escalaciones?</li>
        <li><strong>Financiero:</strong> ¿Costo por transacción bajó? ¿Retención mejoró?</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SECTION 5: EXPANSIÓN REGIONAL
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""<h2 class="section-title">🌎 Implementación Regional: Reuso + Adaptación</h2>""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown(f"""
    <div class="card accent">
        <h4 style="color: {COLORS['accent']}; margin-top: 0;">✅ Elementos Transversales (Reutilizar)</h4>
        <p style="font-weight: 600; color: {COLORS['primary']};">Estos persisten en cualquier país:</p>
        <ul style="margin: 10px 0;">
            <li>Estructura del flujo: Escucha → Simulación → Confirmación → Follow-up</li>
            <li>Principio: Transparencia ANTES de acción</li>
            <li>KPI principal: Reclamaciones por confusión</li>
            <li>Integración: API estándar para cambios</li>
            <li>Documentación: Resumen en lenguaje humano</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card secondary">
        <h4 style="color: {COLORS['secondary']}; margin-top: 0;">🌍 Elementos Locales (Adaptar)</h4>
        <p style="font-weight: 600; color: {COLORS['primary']};">Varían por país/regulación:</p>
        <ul style="margin: 10px 0;">
            <li><strong>Regulación:</strong> Colombia ≠ Chile ≠ Uruguay ≠ Perú</li>
            <li><strong>Canales:</strong> WhatsApp, SMS, email (preferencia local)</li>
            <li><strong>Horarios:</strong> Zona horaria + cultura de atención</li>
            <li><strong>Documentación:</strong> Firma digital vs. física, consentimientos</li>
            <li><strong>Idioma/Tonalidad:</strong> Español latinoamericano tiene variantes</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
<div class="highlight">
    <h4 style="margin-top: 0; color: {COLORS['primary']};">💡 Enfoque Regional</h4>
    <p>
        El flujo y el principio de empatía son globales. 
        <br>Los detalles operativos, legales y de comunicación son locales. 
        <br><strong>Así se logra escala sin perder humanidad.</strong>
    </p>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SECTION 6: RESUMEN
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""<h2 class="section-title">💬 Mi Propuesta en Síntesis</h2>""", unsafe_allow_html=True)

st.markdown(f"""
<div class="card secondary">
    <p style="font-size: 1.15em; line-height: 2; color: {COLORS['dark']};">
        No vengo a "digitalizar" todo. Vengo a diseñar procesos donde:
    </p>
    
    <table style="width: 100%; margin-top: 20px; border-collapse: collapse;">
        <tr style="background: {COLORS['light']};">
            <td style="padding: 15px; border: 1px solid {COLORS['accent']}; font-weight: 600; color: {COLORS['primary']}; width: 5%;">✅</td>
            <td style="padding: 15px; border: 1px solid {COLORS['accent']};">El <strong>cliente</strong> entiende qué pasa en cada paso</td>
        </tr>
        <tr>
            <td style="padding: 15px; border: 1px solid {COLORS['accent']}; font-weight: 600; color: {COLORS['primary']};">✅</td>
            <td style="padding: 15px; border: 1px solid {COLORS['accent']};">El <strong>ejecutivo de cuenta</strong> tiene herramientas para ayudar (no burocracia para frenar)</td>
        </tr>
        <tr style="background: {COLORS['light']};">
            <td style="padding: 15px; border: 1px solid {COLORS['accent']}; font-weight: 600; color: {COLORS['primary']};">✅</td>
            <td style="padding: 15px; border: 1px solid {COLORS['accent']};">El <strong>equipo interno</strong> trabaja en casos que importan (no en reclamaciones evitables)</td>
        </tr>
        <tr>
            <td style="padding: 15px; border: 1px solid {COLORS['accent']}; font-weight: 600; color: {COLORS['primary']};">✅</td>
            <td style="padding: 15px; border: 1px solid {COLORS['accent']};">**Suramericana** crece porque genera <strong style="color: {COLORS['secondary']};">confianza</strong> (no porque vende más barato)</td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# FOOTER Y CALL TO ACTION
# ═══════════════════════════════════════════════════════════════

st.markdown(f"""
<div class="footer">
    <h3 style="margin-top: 0;">Julian Course</h3>
    <p style="font-size: 1.1em; color: {COLORS['primary']}; font-weight: 600;">
        Responsable de Experiencia y Procesos
    </p>
    <p style="font-style: italic; color: #666;">
        Diseñador de procesos centrado en humanidad, no en tecnología
    </p>
    
    <hr style="border: none; border-top: 2px solid {COLORS['light']}; margin: 20px 0;">
    
    <p style="color: {COLORS['primary']}; font-weight: 600; font-size: 1.05em;">
        📧 Enviar a: <strong>ebetancurc@sura.com</strong>
    </p>
    <p style="color: #666; font-size: 0.95em;">
        Asunto: "Mi Propuesta para SuraTech - Responsable de Experiencia y Procesos"
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown(f"""
<div style="text-align: center; padding: 20px; color: #999; font-size: 0.85em;">
    <p>Propuesta creada con Streamlit | Diseño visual centrado en empatía radical | {datetime.now().strftime('%Y')}</p>
</div>
""", unsafe_allow_html=True)
