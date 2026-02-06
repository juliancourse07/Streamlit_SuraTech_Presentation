import streamlit as st

@st.cache_data
def load_css():
    """CSS optimizado y cacheado"""
    return """
    <style>
        * { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
        .main { background: linear-gradient(135deg, #fff 0%, #E8F4F8 100%); }
        .hero {
            background: linear-gradient(135deg, #0072CE, #00C9DB);
            padding: 50px 30px;
            border-radius: 15px;
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }
        .hero h1 { font-size: clamp(1.8em, 5vw, 3em); margin: 0 0 15px 0; }
        .card {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            border-left: 4px solid #00C9DB;
            margin: 15px 0;
        }
        .section-title {
            color: #003366;
            font-size: clamp(1.3em, 3.5vw, 2em);
            font-weight: 700;
            margin: 40px 0 20px 0;
            border-bottom: 3px solid #00C9DB;
            padding-bottom: 10px;
        }
        .timeline { padding-left: 30px; border-left: 3px solid #00C9DB; margin: 10px 0; }
        .metric-box {
            background: linear-gradient(135deg, #0072CE, #00C9DB);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
        }
        [data-testid="stSidebar"] { background: linear-gradient(180deg, #003366, #0072CE); }
        [data-testid="stSidebar"] * { color: white !important; }
    </style>
    """
