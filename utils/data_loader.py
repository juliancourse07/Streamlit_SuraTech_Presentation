import streamlit as st

@st.cache_data
def get_colors():
    return {
        'blue': '#0072CE',
        'cyan': '#00C9DB',
        'navy': '#003366'
    }
