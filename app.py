import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Julian Course | Mi Propuesta para SuraTech",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Colores
PRIMARY = "#044B93"
SECONDARY = "#00A99D"
ACCENT = "#16BBE5"

# CSS mínimo
st.markdown("""
    <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# HERO
st.markdown(f"""
    <div style="background: linear-gradient(135deg, {PRIMARY} 0%, {ACCENT} 100%); padding: 60px 40px; border-radius: 15px; color: white; margin-bottom: 30px;">
        <h1 style="margin: 0; font-size: 2.5em;">🚀 Mi Aporte a SuraTech</h1>
        <p style="margin: 10px 0 0 0; font-size: 1.2em;">Diseño de procesos centrado en la humanidad, no en la tecnología</p>
    </div>
""", unsafe_allow_html=True)

# FILOSOFÍA
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
        <div style="background: white; border-radius: 10px; padding: 30px; border-left: 5px solid {PRIMARY};">
            <h3 style="color: {PRIMARY}; margin-top: 0;">🎯 Mi Filosofía</h3>
            <p><strong>No soy un técnico que intenta entender a las personas.</strong></p>
            <p style="color: {SECONDARY}; font-weight: 600;">Soy alguien que entiende a las personas primero, y luego busca la tecnología que las sirve.</p>
            <p style="color: #666; font-style: italic;">Los procesos no fallan por software. Fallan porque no entendemos la realidad del cliente.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.metric("Mi Enfoque", "Holístico", "100% Humano")

st.markdown("---")

# EL PROBLEMA
st.markdown(f"<h2 style='color: {PRIMARY}; border-bottom: 3px solid {SECONDARY}; padding-bottom: 10px;'>📍 El Problema: Modificación de Seguros</h2>", unsafe_allow_html=True)

st.markdown("""
**El cliente llama y dice:** *"Quiero cambiar algo"*

**Lo que eso realmente significa:**
- Una vida que cambió (nuevo trabajo, nueva casa, más hijos)
- Una decisión tomada en 5 minutos, pero con impacto en todo
- Un proceso que será frustrante si no lo diseñamos bien
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("⏱️ Tiempo Dedicado", "15 min", "Para un cambio crucial")

with col2:
    st.metric("😤 Puntos de Frustración", "6-8", "En la jornada actual")

with col3:
    st.metric("📈 Impacto Real", "3x", "Más reclamaciones")

st.markdown("---")

# ENFOQUE
st.markdown(f"<h2 style='color: {PRIMARY}; border-bottom: 3px solid {SECONDARY}; padding-bottom: 10px;'>🧭 Cómo Yo Diseñaría Este Proceso</h2>", unsafe_allow_html=True)

st.markdown(f"""
<div style="background: #f0f5fa; border-left: 5px solid {SECONDARY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
    <h3 style="color: {PRIMARY}; margin-top: 0;">Paso 1: Empatía Radical (La Base)</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    **👥 Con Quién Me Siento:**
    - El cliente final (quien tiene miedo)
    - El ejecutivo de cuenta (quien recibe el llamado)
    - Reclamaciones (quien ve las confusiones)
    - Sistemas (quien dice "es complejo")
    """)

with col2:
    st.markdown(f"""
    **🔍 Qué Miro:**
    - **Afuera:** ¿Qué pasó en la vida del cliente?
    - **Adentro:** ¿Dónde se rompe el proceso?
    - **Conversaciones:** Entrevistas reales, no formularios
    """)

st.markdown(f"""
<div style="background: linear-gradient(120deg, {ACCENT}20, {SECONDARY}20); border-left: 5px solid {SECONDARY}; padding: 20px; border-radius: 8px; margin: 20px 0;">
    <h3 style="color: {PRIMARY}; margin-top: 0;">💡 Insight Clave</h3>
    <p style="font-size: 1.05em;">
        La gente no quiere un "proceso de modificación". 
        <br><strong style="color: {SECONDARY};">Quiere paz mental</strong> de que su cambio está correcto y que su protección sigue vigente.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="background: linear-gradient(135deg, {ACCENT}08, {PRIMARY}08); border-left: 5px solid {ACCENT}; padding: 20px; border-radius: 8px; margin: 20px 0;">
    <h3 style="color: {ACCENT}; margin-top: 0;">Paso 2: No Linealidad - Iteración Rápida</h3>
    <p><strong>No diseño en waterfall. Diseño en ciclos pequeños:</strong></p>
    <ul>
        <li><strong>1️⃣ Prototipo Humano:</strong> Simulo el cambio en una hoja, viendo qué dice el cliente</li>
        <li><strong>2️⃣ Test con 5 Clientes:</strong> Veo dónde dudan, dónde se confunden</li>
        <li><strong>3️⃣ Ajusto el Flujo:</strong> Cambio, no espero a que sea perfecto</li>
        <li><strong>4️⃣ Repito:</strong> Hasta que el cliente dice "así sí tiene sentido"</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# FLUJO
st.markdown(f"<h2 style='color: {PRIMARY}; border-bottom: 3px solid {SECONDARY}; padding-bottom: 10px;'>🔄 El Proceso Rediseñado</h2>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 Flujo Visual", "💡 Detalles", "🎯 Particularidades"])

with tab1:
    st.markdown("""
    **Los 7 Pasos del Proceso:**
    
    1. 📞 **Cliente Llama/Contacta** — Momento crítico: el cliente está decidiendo
    2. 👂 **Escucha Real** — Sin interrumpir, el ejecutivo entiende QUÉ cambiar
    3. ❓ **Clarificación Inmediata** — ¿Qué? ¿Cuándo? ¿Por qué?
    4. 📊 **Simulación en Tiempo Real** — Mostrar impacto: Anterior vs Nuevo vs Diferencia
    5. ✅ **Confirmación Explícita** — Cliente dice SÍ de forma clara y documentada
    6. 📄 **Documentación Clara** — Resumen en lenguaje humano (No contrato)
    7. 🔔 **Confirmación Recurrente** — 24h y 7 días después: "Tu cambio está procesado"
    """)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div style="background: white; border-left: 5px solid {SECONDARY}; padding: 20px; border-radius: 8px; margin: 10px 0;">
            <h4 style="color: {SECONDARY}; margin-top: 0;">🎧 Escucha Real</h4>
            <p><strong>Qué:</strong> El ejecutivo escucha sin llenar formularios</p>
            <p><strong>Por qué:</strong> Los formularios hacen que el cliente omita contexto</p>
            <p><strong>Cómo:</strong> 2 minutos de conversación > 10 minutos de formulario</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: white; border-left: 5px solid {ACCENT}; padding: 20px; border-radius: 8px; margin: 10px 0;">
            <h4 style="color: {ACCENT}; margin-top: 0;">📊 Simulación Transparente</h4>
            <p><strong>Qué:</strong> El cliente ve ANTES de confirmar</p>
            <p><strong>Por qué:</strong> Reduce reclamaciones por "sorpresa"</p>
            <p><strong>Cómo:</strong> Tabla clara: Anterior | Nuevo | Diferencia</p>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown(f"""
    <div style="background: white; border-left: 5px solid {SECONDARY}; padding: 20px; border-radius: 8px;">
        <h3 style="color: {SECONDARY}; margin-top: 0;">🎯 Particularidades para Este Proceso</h3>
        
        <h4 style="color: {PRIMARY};">1️⃣ Tipo de Seguro Importa</h4>
        <ul>
            <li><strong>Vida:</strong> Cliente tiene miedo a cambiar cobertura (¿si me pasa algo?)</li>
            <li><strong>Auto:</strong> Cliente quiere que sea rápido (ocupado)</li>
            <li><strong>Hogar:</strong> Cliente compara (con competencia)</li>
        </ul>
        
        <h4 style="color: {PRIMARY};">2️⃣ El Deducible es CRÍTICO</h4>
        <p>Cuando el cliente quiere bajar deducible (pagar más cuota), asume menos riesgo. Nuestro trabajo: que entienda que paga MENOS cuando algo malo sucede.</p>
        
        <h4 style="color: {PRIMARY};">3️⃣ Cobertura Adicional >> Reducida</h4>
        <p>Es 10x más fácil vender más cobertura. Si quiere PERDER protección, es bandera roja de que NO entiende.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# MÉTRICAS
st.markdown(f"<h2 style='color: {PRIMARY}; border-bottom: 3px solid {SECONDARY}; padding-bottom: 10px;'>📈 Cómo Medimos (Sin Encuestas Tedias)</h2>", unsafe_allow_html=True)

st.markdown("### Para el Cliente B2C (Final)")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("⏱️ Tiempo Procesamiento", "48h", "Meta: 24h")

with col2:
    st.metric("📉 Reclamaciones Reducidas", "-40%", "Por confirmación explícita")

with col3:
    st.metric("🤝 Referrals Generados", "+25%", "Cliente recomienda")

st.markdown("### Para el Cliente B2B (Canal)")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🔌 Disponibilidad APIs", "95%", "Meta: 99.5%")

with col2:
    st.metric("✅ Documentación Regulatoria", "100%", "Cero inconsistencias")

with col3:
    st.metric("😊 Satisfacción Equipo", "⭐⭐⭐⭐", "Menos manual, más estrategia")

st.markdown("---")

# EXPANSIÓN REGIONAL
st.markdown(f"<h2 style='color: {PRIMARY}; border-bottom: 3px solid {SECONDARY}; padding-bottom: 10px;'>🌎 Implementación Regional</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div style="background: white; border-left: 5px solid {ACCENT}; padding: 20px; border-radius: 8px;">
        <h4 style="color: {ACCENT}; margin-top: 0;">✅ Elementos Transversales (Reutilizar)</h4>
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
    <div style="background: white; border-left: 5px solid {SECONDARY}; padding: 20px; border-radius: 8px;">
        <h4 style="color: {SECONDARY}; margin-top: 0;">🌍 Elementos Locales (Adaptar)</h4>
        <ul>
            <li><strong>Regulación:</strong> Colombia ≠ Chile ≠ Uruguay</li>
            <li><strong>Canales:</strong> WhatsApp, SMS, email</li>
            <li><strong>Horarios:</strong> Zona horaria + cultura</li>
            <li><strong>Documentación:</strong> Firma digital vs. física</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# RESUMEN
st.markdown(f"<h2 style='color: {PRIMARY}; border-bottom: 3px solid {SECONDARY}; padding-bottom: 10px;'>💬 Mi Propuesta en Síntesis</h2>", unsafe_allow_html=True)

st.markdown(f"""
<div style="background: white; border-left: 5px solid {SECONDARY}; padding: 30px; border-radius: 8px;">
    <p style="font-size: 1.1em; line-height: 1.8;">
        No vengo a "digitalizar" todo. Vengo a diseñar procesos donde:
    </p>
    
    <ul style="font-size: 1.05em; line-height: 1.8;">
        <li>✅ El <strong>cliente</strong> entiende qué pasa en cada paso</li>
        <li>✅ El <strong>ejecutivo de cuenta</strong> tiene herramientas para ayudar</li>
        <li>✅ El <strong>equipo interno</strong> trabaja en casos que importan</li>
        <li>✅ <strong>Suramericana</strong> crece porque genera CONFIANZA</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# FOOTER
st.markdown(f"""
<div style="background: linear-gradient(135deg, {PRIMARY}05, {ACCENT}05); border-top: 3px solid {SECONDARY}; padding: 30px; border-radius: 8px; text-align: center; margin-top: 50px;">
    <h3 style="color: {PRIMARY}; margin-top: 0;">Julian Course</h3>
    <p style="font-size: 1.1em; color: {PRIMARY}; font-weight: 600; margin: 5px 0;">Responsable de Experiencia y Procesos</p>
    <p style="font-style: italic; color: #666; margin: 5px 0;">Diseñador de procesos centrado en humanidad, no en tecnología</p>
    
    <hr style="border: none; border-top: 2px solid #e0e0e0; margin: 20px 0;">
    
    <p style="color: {PRIMARY}; font-weight: 600; margin: 5px 0;">📧 <strong>ebetancurc@sura.com</strong></p>
    <p style="color: #666; font-size: 0.95em; margin: 0;">Asunto: "Mi Propuesta para SuraTech - Responsable de Experiencia y Procesos"</p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align: center; padding: 20px; color: #999; font-size: 0.85em;">
    <p>Propuesta creada con Streamlit | {datetime.now().strftime('%Y')}</p>
</div>
""", unsafe_allow_html=True)
