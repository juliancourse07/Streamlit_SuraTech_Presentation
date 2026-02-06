import streamlit as st
from datetime import datetime

def render():
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; padding: 25px; background: #F8F9FA; border-radius: 12px;">
        <p style="font-size: 1.1em; margin: 0 0 15px 0;">
            <strong>¿Listo para co-crear el futuro de seguros digitales?</strong>
        </p>
        <p style="font-size: 0.95em; color: #666;">
            📧 ebetancurc@sura.com | 🚀 Julian Course | {datetime.now().year}
        </p>
    </div>
    """, unsafe_allow_html=True)
