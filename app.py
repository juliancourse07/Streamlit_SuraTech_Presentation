import streamlit as st
import time

st.set_page_config(
    page_title="Un Día en la Vida de María | Julian Course",
    page_icon="👤",
    layout="wide"
)

# ============================================
# CSS NARRATIVO
# ============================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * { 
        font-family: 'Inter', -apple-system, sans-serif;
        transition: all 0.3s ease;
    }
    
    .main { 
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 0;
    }
    
    /* Storytelling Sections */
    .story-section {
        background: white;
        padding: 60px 40px;
        margin: 40px auto;
        max-width: 900px;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        animation: fadeIn 0.8s ease-out;
    }
    
    .story-section.dark {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .story-section.problem {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
    }
    
    .story-section.solution {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
    }
    
    .story-section.action {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        color: #1a1a1a;
    }
    
    /* Quote estilo conversación */
    .quote {
        font-size: 1.8em;
        font-weight: 300;
        font-style: italic;
        line-height: 1.6;
        margin: 30px 0;
        padding-left: 30px;
        border-left: 5px solid rgba(255,255,255,0.5);
    }
    
    .quote.dark-text {
        border-left-color: #667eea;
    }
    
    /* Personaje */
    .character {
        display: flex;
        align-items: center;
        gap: 20px;
        margin: 30px 0;
        padding: 25px;
        background: rgba(255,255,255,0.15);
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
    
    .character-avatar {
        font-size: 4em;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
    }
    
    .character-info h3 {
        margin: 0 0 10px 0;
        font-size: 1.5em;
    }
    
    .character-info p {
        margin: 0;
        opacity: 0.9;
    }
    
    /* Timeline interactivo */
    .timeline {
        position: relative;
        padding: 20px 0;
    }
    
    .timeline-item {
        display: flex;
        gap: 20px;
        margin: 30px 0;
        align-items: flex-start;
    }
    
    .timeline-icon {
        font-size: 2.5em;
        min-width: 60px;
        text-align: center;
    }
    
    .timeline-content {
        flex: 1;
        background: rgba(255,255,255,0.95);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .timeline-content h4 {
        margin: 0 0 10px 0;
        color: #667eea;
    }
    
    /* Insight boxes */
    .insight {
        background: #fffbea;
        border-left: 4px solid #f59e0b;
        padding: 20px;
        margin: 25px 0;
        border-radius: 8px;
    }
    
    .insight strong {
        color: #d97706;
    }
    
    /* Call to action buttons */
    .cta-button {
        display: inline-block;
        background: white;
        color: #667eea;
        padding: 15px 40px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1em;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin: 20px 10px;
        cursor: pointer;
        border: none;
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.25);
    }
    
    /* Emotion meter */
    .emotion-meter {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 30px 0;
        padding: 20px;
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
    }
    
    .emotion-point {
        text-align: center;
        flex: 1;
    }
    
    .emotion-point .emoji {
        font-size: 3em;
        display: block;
        margin-bottom: 10px;
    }
    
    .emotion-point .label {
        font-size: 0.9em;
        opacity: 0.8;
    }
    
    /* Principles grid */
    .principles-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }
    
    .principle-card {
        background: white;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    
    .principle-card .icon {
        font-size: 3em;
        margin-bottom: 15px;
    }
    
    .principle-card h4 {
        margin: 0 0 10px 0;
        color: #667eea;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .story-section { padding: 40px 25px; }
        .quote { font-size: 1.4em; }
        .character { flex-direction: column; text-align: center; }
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# TRACKING DE PROGRESO
# ============================================

if 'step' not in st.session_state:
    st.session_state.step = 0

def avanzar():
    st.session_state.step += 1

def resetear():
    st.session_state.step = 0

# ============================================
# NAVEGACIÓN STORYTELLING
# ============================================

# INTRO
if st.session_state.step == 0:
    st.markdown("""
    <div class="story-section dark">
        <div style="text-align: center;">
            <h1 style="font-size: 3.5em; margin: 0 0 20px 0;">👤</h1>
            <h1 style="margin: 0 0 20px 0;">Un Día en la Vida de María</h1>
            <p style="font-size: 1.3em; opacity: 0.9; line-height: 1.8;">
                Esta no es una presentación técnica.<br>
                Es una historia sobre <strong>entender lo que realmente importa</strong>.<br><br>
                Te voy a mostrar cómo diseñar procesos desde la humanidad, no desde la tecnología.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Comenzar la Historia", use_container_width=True):
            avanzar()
            st.rerun()

# PASO 1: CONOCE A MARÍA
elif st.session_state.step == 1:
    st.markdown("""
    <div class="story-section">
        <h2 style="color: #667eea;">📍 Capítulo 1: Conoce a María</h2>
        
        <div class="character">
            <div class="character-avatar">👩‍💼</div>
            <div class="character-info">
                <h3>María Rodríguez</h3>
                <p><strong>32 años</strong> • Diseñadora gráfica • Bogotá, Colombia</p>
                <p style="margin-top: 10px;">
                    Hace 2 años contrató un seguro de auto a través de su banco.<br>
                    Lo hizo rápido, en 10 minutos, desde su celular.
                </p>
            </div>
        </div>
        
        <div class="quote dark-text">
            "Fue súper fácil contratar el seguro. Tres clicks y listo. 
            Me sentí moderna, en control."
        </div>
        
        <div class="insight">
            <strong>💡 Insight:</strong> María no compró un seguro. Compró <strong>tranquilidad sin fricción</strong>.
            La experiencia inicial marcó sus expectativas.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("➡️ ¿Qué pasó después?", use_container_width=True):
            avanzar()
            st.rerun()

# PASO 2: EL CAMBIO
elif st.session_state.step == 2:
    st.markdown("""
    <div class="story-section">
        <h2 style="color: #667eea;">🍼 Capítulo 2: Todo Cambió</h2>
        
        <p style="font-size: 1.3em; line-height: 1.8;">
            Tres meses atrás, María tuvo a <strong>Sofía</strong>, su primera hija.
        </p>
        
        <div style="text-align: center; margin: 40px 0;">
            <div style="font-size: 5em;">👶</div>
            <p style="font-size: 1.2em; color: #667eea; margin-top: 20px;">
                Su mundo cambió. Sus prioridades cambiaron.<br>
                Su seguro... <strong>necesitaba cambiar también</strong>.
            </p>
        </div>
        
        <div class="quote dark-text">
            "Ahora no solo me preocupo por mí. Si algo me pasa en el auto, 
            ¿qué pasa con Sofía? Necesito más cobertura."
        </div>
        
        <div class="insight">
            <strong>💡 Insight:</strong> Los clientes no modifican seguros por aburrimiento. 
            Lo hacen porque <strong>la vida cambió</strong>. Es un momento emocional, no transaccional.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("➡️ ¿Qué hizo María?", use_container_width=True):
            avanzar()
            st.rerun()

# PASO 3: EL PROCESO ACTUAL (PROBLEMA)
elif st.session_state.step == 3:
    st.markdown("""
    <div class="story-section problem">
        <h2>😤 Capítulo 3: El Laberinto</h2>
        
        <p style="font-size: 1.2em; line-height: 1.8; margin-bottom: 40px;">
            María llamó al banco para agregar cobertura de accidentes personales familiar.
            <strong>Esto es lo que vivió:</strong>
        </p>
        
        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-icon">📞</div>
                <div class="timeline-content">
                    <h4>Llamada 1: El banco</h4>
                    <p>"Su seguro lo maneja otra área. Le transfiero."</p>
                    <p style="font-size: 0.9em; opacity: 0.8; margin-top: 10px;">⏱️ 12 minutos en espera</p>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-icon">🔄</div>
                <div class="timeline-content">
                    <h4>Llamada 2: Centro de seguros</h4>
                    <p>"Necesito su número de póliza, fecha de nacimiento, y tres documentos por email."</p>
                    <p style="font-size: 0.9em; opacity: 0.8; margin-top: 10px;">⏱️ 8 minutos explicando lo mismo</p>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-icon">⏰</div>
                <div class="timeline-content">
                    <h4>Días 2-5: El silencio</h4>
                    <p>Nadie la contactó. Tuvo que llamar 2 veces más para preguntar "¿qué pasó?"</p>
                    <p style="font-size: 0.9em; opacity: 0.8; margin-top: 10px;">⏱️ 5 días sin noticias</p>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-icon">💰</div>
                <div class="timeline-content">
                    <h4>Día 6: La sorpresa</h4>
                    <p>"Su nueva prima es $X." — No le explicaron por qué, ni le mostraron opciones.</p>
                    <p style="font-size: 0.9em; opacity: 0.8; margin-top: 10px;">😤 Frustración máxima</p>
                </div>
            </div>
        </div>
        
        <div style="text-align: center; margin: 40px 0;">
            <h3 style="margin: 0 0 20px 0;">Su viaje emocional</h3>
            <div class="emotion-meter">
                <div class="emotion-point">
                    <span class="emoji">😊</span>
                    <span class="label">Inicio</span>
                </div>
                <div class="emotion-point">
                    <span class="emoji">😕</span>
                    <span class="label">Día 1</span>
                </div>
                <div class="emotion-point">
                    <span class="emoji">😤</span>
                    <span class="label">Día 3</span>
                </div>
                <div class="emotion-point">
                    <span class="emoji">😡</span>
                    <span class="label">Día 5</span>
                </div>
                <div class="emotion-point">
                    <span class="emoji">😞</span>
                    <span class="label">Día 6</span>
                </div>
            </div>
        </div>
        
        <div class="quote">
            "Contratar el seguro fue más fácil que modificarlo. 
            ¿Por qué cuidar a mi hija tiene que ser tan difícil?"
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💡 Ver mi propuesta", use_container_width=True):
            avanzar()
            st.rerun()

# PASO 4: MI ENFOQUE
elif st.session_state.step == 4:
    st.markdown("""
    <div class="story-section solution">
        <h2>🎯 Mi Enfoque: Diseño desde la Empatía Radical</h2>
        
        <p style="font-size: 1.3em; line-height: 1.8; margin-bottom: 30px;">
            El problema no es técnico. Es <strong>humano</strong>.<br>
            María no necesitaba un "proceso de modificaciones".<br>
            Necesitaba que alguien entendiera que <strong>estaba protegiendo a su hija</strong>.
        </p>
        
        <div class="quote">
            "No diseño procesos. Diseño momentos que respetan 
            la urgencia emocional del cliente."
        </div>
        
        <h3 style="margin: 50px 0 30px 0; font-size: 1.8em;">🧭 Mis 4 Principios</h3>
        
        <div class="principles-grid">
            <div class="principle-card">
                <div class="icon">🔍</div>
                <h4>Empatía Radical</h4>
                <p>Entender el "por qué" antes del "cómo"</p>
            </div>
            
            <div class="principle-card">
                <div class="icon">⚡</div>
                <h4>Velocidad Emocional</h4>
                <p>No cuánto tarda, sino cuán rápido SE SIENTE</p>
            </div>
            
            <div class="principle-card">
                <div class="icon">💎</div>
                <h4>Transparencia Total</h4>
                <p>Mostrar el "por qué" del precio antes de confirmar</p>
            </div>
            
            <div class="principle-card">
                <div class="icon">🤝</div>
                <h4>Opcionalidad Real</h4>
                <p>El cliente elige cómo, cuándo y dónde</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("➡️ ¿Cómo lo haría diferente?", use_container_width=True):
            avanzar()
            st.rerun()

# PASO 5: LA SOLUCIÓN (PROCESO REDISEÑADO)
elif st.session_state.step == 5:
    st.markdown("""
    <div class="story-section">
        <h2 style="color: #667eea;">✨ Capítulo 4: El Proceso que María Merece</h2>
        
        <p style="font-size: 1.2em; line-height: 1.8; margin-bottom: 40px;">
            Imagina que María abre la app del banco y ve esto:
        </p>
        
        <div style="background: #f8f9fa; padding: 30px; border-radius: 15px; margin: 30px 0;">
            <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <h3 style="color: #667eea; margin: 0 0 15px 0;">👶 ¿Tu familia creció?</h3>
                <p style="color: #666; margin: 0 0 20px 0;">
                    Protege a los que más amas. Agrega cobertura familiar en 2 minutos.
                </p>
                <button style="background: #667eea; color: white; border: none; padding: 12px 30px; border-radius: 8px; font-weight: 600; cursor: pointer;">
                    Ver opciones
                </button>
            </div>
        </div>
        
        <h3 style="color: #667eea; margin: 50px 0 30px 0;">🔄 El Nuevo Flujo (3 minutos)</h3>
        
        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-icon">🎯</div>
                <div class="timeline-content">
                    <h4>Paso 1: Contexto (30 seg)</h4>
                    <p><strong>"¿Qué cambió en tu vida?"</strong></p>
                    <p>Opciones: Nuevo bebé • Nueva casa • Nuevo trabajo</p>
                    <p style="background: #e0f2fe; padding: 10px; border-radius: 8px; margin-top: 10px;">
                        💡 <strong>Por qué funciona:</strong> Le demostramos que entendemos su contexto emocional
                    </p>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-icon">💰</div>
                <div class="timeline-content">
                    <h4>Paso 2: Simulación Visual (1 min)</h4>
                    <p><strong>Comparativa lado a lado:</strong></p>
                    <p>• Tu plan actual: $150/mes → Cubre solo a ti<br>
                       • Con cobertura familiar: $210/mes → Cubre a ti + 3 personas</p>
                    <p style="background: #e0f2fe; padding: 10px; border-radius: 8px; margin-top: 10px;">
                        💡 <strong>Por qué funciona:</strong> Transparencia total. Ve el valor ANTES de decidir
                    </p>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-icon">✅</div>
                <div class="timeline-content">
                    <h4>Paso 3: Confirmación Emocional (30 seg)</h4>
                    <p><strong>"Tu familia estará protegida desde HOY."</strong></p>
                    <p>Email + SMS + Póliza en PDF + Botón "Compartir con mi familia"</p>
                    <p style="background: #e0f2fe; padding: 10px; border-radius: 8px; margin-top: 10px;">
                        💡 <strong>Por qué funciona:</strong> No es una transacción. Es un momento de alivio
                    </p>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-icon">📊</div>
                <div class="timeline-content">
                    <h4>Paso 4: Micro-Feedback (48 horas después)</h4>
                    <p><strong>"¿Qué tan fácil fue?"</strong> 😊 😐 😕</p>
                    <p>Un solo click. Sin encuestas largas.</p>
                    <p style="background: #e0f2fe; padding: 10px; border-radius: 8px; margin-top: 10px;">
                        💡 <strong>Por qué funciona:</strong> Medimos cuando la emoción aún está fresca
                    </p>
                </div>
            </div>
        </div>
        
        <div style="text-align: center; margin: 50px 0;">
            <h3 style="margin: 0 0 20px 0;">Nuevo viaje emocional</h3>
            <div class="emotion-meter">
                <div class="emotion-point">
                    <span class="emoji">🤔</span>
                    <span class="label">Necesidad</span>
                </div>
                <div class="emotion-point">
                    <span class="emoji">😊</span>
                    <span class="label">Descubrimiento</span>
                </div>
                <div class="emotion-point">
                    <span class="emoji">💡</span>
                    <span class="label">Comparación</span>
                </div>
                <div class="emotion-point">
                    <span class="emoji">✅</span>
                    <span class="label">Decisión</span>
                </div>
                <div class="emotion-point">
                    <span class="emoji">❤️</span>
                    <span class="label">Alivio</span>
                </div>
            </div>
        </div>
        
        <div class="insight">
            <strong>📊 Impacto Esperado:</strong><br>
            • Tiempo de proceso: 6 días → <strong>3 minutos</strong><br>
            • Tasa de abandono: 35% → <strong>< 5%</strong><br>
            • Satisfacción: 2.8/5 → <strong>> 4.5/5</strong><br>
            • Llamadas de soporte: -78%
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("➡️ ¿Cómo lo mediría?", use_container_width=True):
            avanzar()
            st.rerun()

# PASO 6: MÉTRICAS HUMANAS
elif st.session_state.step == 6:
    st.markdown("""
    <div class="story-section action">
        <h2 style="color: #1a1a1a;">📊 Midiendo lo que Realmente Importa</h2>
        
        <div class="quote dark-text">
            "Los NPS no capturan lágrimas de alivio.<br>
            Necesitamos métricas que midan momentos, no números."
        </div>
        
        <h3 style="color: #1a1a1a; margin: 40px 0 25px 0;">Mis KPIs Disruptivos:</h3>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 20px;">
            <h4 style="color: #667eea; margin: 0 0 15px 0;">🎤 Effortless Score</h4>
            <p style="margin: 0 0 10px 0;"><strong>Pregunta:</strong> "¿Qué tan fácil fue?" (1-5)</p>
            <p style="margin: 0; color: #666; font-size: 0.95em;">
                <strong>Por qué:</strong> Mide carga cognitiva y emocional, no solo satisfacción
            </p>
        </div>
        
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 20px;">
            <h4 style="color: #667eea; margin: 0 0 15px 0;">📱 Micro-interacciones</h4>
            <p style="margin: 0 0 10px 0;"><strong>Métrica:</strong> ¿Cuántas veces simula antes de decidir?</p>
            <p style="margin: 0; color: #666; font-size: 0.95em;">
                <strong>Por qué:</strong> Si simula 5+ veces, algo no es claro
            </p>
        </div>
        
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            <h4 style="color: #667eea; margin: 0 0 15px 0;">⏱️ Time to Relief</h4>
            <p style="margin: 0 0 10px 0;"><strong>Métrica:</strong> Desde "tengo el problema" hasta "siento alivio"</p>
            <p style="margin: 0; color: #666; font-size: 0.95em;">
                <strong>Por qué:</strong> Mide velocidad emocional, no técnica
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 20px;">
            <h4 style="color: #667eea; margin: 0 0 15px 0;">💬 Sentiment Analysis</h4>
            <p style="margin: 0 0 10px 0;"><strong>Métrica:</strong> Análisis de texto en chats/emails post-proceso</p>
            <p style="margin: 0; color: #666; font-size: 0.95em;">
                <strong>Por qué:</strong> Captura emociones que las escalas no pueden
            </p>
        </div>
        
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 20px;">
            <h4 style="color: #667eea; margin: 0 0 15px 0;">🔄 Repeat Confidence</h4>
            <p style="margin: 0 0 10px 0;"><strong>Métrica:</strong> % que vuelve a modificar en 6 meses</p>
            <p style="margin: 0; color: #666; font-size: 0.95em;">
                <strong>Por qué:</strong> Si confían, vuelven sin miedo
            </p>
        </div>
        
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            <h4 style="color: #667eea; margin: 0 0 15px 0;">📞 Support Deflection</h4>
            <p style="margin: 0 0 10px 0;"><strong>Métrica:</strong> % que NO necesita llamar después</p>
            <p style="margin: 0; color: #666; font-size: 0.95em;">
                <strong>Por qué:</strong> Si el proceso es claro, no hay dudas
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="insight">
            <strong>🎯 Filosofía de Medición:</strong><br>
            No mido si el cliente está "satisfecho". Mido si:<br>
            • Sintió que lo <strong>entendieron</strong><br>
            • Sintió <strong>control</strong> sobre su decisión<br>
            • Sintió <strong>alivio</strong> al terminar<br>
            • Volvería a <strong>confiar</strong> en nosotros
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("➡️ ¿Por qué yo?", use_container_width=True):
            avanzar()
            st.rerun()

# PASO 7: CIERRE PERSONAL
elif st.session_state.step == 7:
    st.markdown("""
    <div class="story-section dark">
        <h2 style="text-align: center; margin-bottom: 40px;">💫 Por Qué Yo para Este Rol</h2>
        
        <div class="quote">
            "No soy un técnico que intenta entender a las personas.<br>
            Soy alguien que entiende a las personas primero, 
            y luego busca la tecnología que las sirve."
        </div>
        
        <div style="margin: 50px 0;">
            <h3 style="text-align: center; margin-bottom: 30px;">🎯 Lo que aporto:</h3>
            
            <div class="principles-grid">
                <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
                    <div style="font-size: 3em; text-align: center; margin-bottom: 15px;">🧠</div>
                    <h4 style="text-align: center; margin: 0 0 10px 0;">Pensamiento Holístico</h4>
                    <p style="margin: 0; opacity: 0.9; text-align: center;">
                        Veo sistemas, no pasos aislados
                    </p>
                </div>
                
                <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
                    <div style="font-size: 3em; text-align: center; margin-bottom: 15px;">❤️</div>
                    <h4 style="text-align: center; margin: 0 0 10px 0;">Empatía Radical</h4>
                    <p style="margin: 0; opacity: 0.9; text-align: center;">
                        Diseño desde el miedo, la urgencia y la esperanza del cliente
                    </p>
                </div>
                
                <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
                    <div style="font-size: 3em; text-align: center; margin-bottom: 15px;">⚡</div>
                    <h4 style="text-align: center; margin: 0 0 10px 0;">Ejecución Ágil</h4>
                    <p style="margin: 0; opacity: 0.9; text-align: center;">
                        Prototipo rápido, mido más rápido, aprendo aún más rápido
                    </p>
                </div>
                
                <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
                    <div style="font-size: 3em; text-align: center; margin-bottom: 15px;">🌎</div>
                    <h4 style="text-align: center; margin: 0 0 10px 0;">Visión Regional</h4>
                    <p style="margin: 0; opacity: 0.9; text-align: center;">
                        Entiendo LATAM: sus diferencias y sus puentes
                    </p>
                </div>
            </div>
        </div>
        
        <div style="text-align: center; margin: 50px 0 30px 0;">
            <p style="font-size: 1.5em; margin: 0 0 30px 0; line-height: 1.6;">
                <strong>No solo diseño procesos.<br>
                Diseño momentos que transforman la relación cliente-marca.</strong>
            </p>
            
            <p style="font-size: 1.2em; opacity: 0.9; margin-bottom: 40px;">
                ¿Listo para co-crear el futuro de seguros digitales en LATAM?
            </p>
            
            <div style="background: white; color: #667eea; padding: 30px; border-radius: 15px; display: inline-block;">
                <p style="font-size: 1.3em; margin: 0 0 15px 0;"><strong>Julian Course</strong></p>
                <p style="margin: 0; font-size: 1.1em;">📧 ebetancurc@sura.com</p>
                <p style="margin: 10px 0 0 0; font-size: 0.9em; opacity: 0.7;">
                    Candidato a Responsable de Experiencia y Procesos | SuraTech
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("🔄 Volver al inicio", use_container_width=True):
            resetear()
            st.rerun()
    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <a href="mailto:ebetancurc@sura.com" style="text-decoration: none;">
                <button style="background: white; color: #667eea; border: none; padding: 12px 30px; border-radius: 8px; font-weight: 600; cursor: pointer; width: 100%;">
                    📧 Contactar
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        if st.button("⬅️ Paso anterior", use_container_width=True):
            st.session_state.step -= 1
            st.rerun()

# ============================================
# SIDEBAR CON PROGRESO
# ============================================

with st.sidebar:
    st.image("https://www.sura.com/Style%20Library/Sura/Assets/images/header-sura-logo.png", width=160)
    
    st.markdown("### 📖 Progreso de la Historia")
    
    steps = [
        "🏠 Inicio",
        "👤 Conoce a María",
        "🍼 El Cambio",
        "😤 El Problema",
        "💡 Mi Enfoque",
        "✨ La Solución",
        "📊 Las Métricas",
        "💫 El Cierre"
    ]
    
    for i, step in enumerate(steps):
        if i < st.session_state.step:
            st.success(f"✅ {step}")
        elif i == st.session_state.step:
            st.info(f"📍 {step}")
        else:
            st.text(f"⚪ {step}")
    
    st.markdown("---")
    st.markdown("**Desarrollado con** ❤️  \n*Enfoque: Narrativa sobre Técnica*")
