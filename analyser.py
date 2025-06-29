import streamlit as st
from datetime import datetime
import requests

# === CONFIGURATION ===
# (Dans un vrai projet, utilisez st.secrets pour ces valeurs)
CONFIG = {
    "APP_NAME": "BET ANALYST PRO",
    "VERSION": "2.0",
    "API_KEYS": {
        "FOOTBALL_DATA": "e466a37640c044bfbeaceaef804ff773",
        "RAPIDAPI": "0053fc492dmsh0aa885662e3df2cp1fbaa2jsnde9ef0e4e8a2"
    },
    "PRIMARY_COLOR": "#2563EB",
    "SECONDARY_COLOR": "#1E40AF"
}

# === STREAMLIT CONFIG ===
st.set_page_config(
    page_title=f"{CONFIG['APP_NAME']} - L'analyse intelligente des paris sportifs",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded"
)

# === CSS PERSONNALISÉ ===
def load_css():
    st.markdown(f"""
    <style>
        .main {{
            background-color: #f8fafc;
        }}
        .header {{
            padding: 2rem 0;
            text-align: center;
        }}
        .logo {{
            font-size: 3rem;
            margin-bottom: 0.5rem;
        }}
        .title {{
            color: {CONFIG['PRIMARY_COLOR']};
            font-weight: 800;
            margin-bottom: 0;
        }}
        .subtitle {{
            color: #64748B;
            margin-top: 0;
        }}
        .feature-card {{
            border-radius: 0.5rem;
            padding: 1.5rem;
            margin-bottom: 1rem;
            background: white;
            box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
        }}
        .primary-button {{
            background-color: {CONFIG['PRIMARY_COLOR']} !important;
            border: none !important;
        }}
        .primary-button:hover {{
            background-color: {CONFIG['SECONDARY_COLOR']} !important;
            transform: scale(1.02);
        }}
    </style>
    """, unsafe_allow_html=True)

load_css()

# === HEADER ===
st.markdown("""
<div class="header">
    <div class="logo">📊</div>
    <h1 class="title">BET ANALYST PRO</h1>
    <p class="subtitle">L'analyse intelligente des paris sportifs</p>
</div>
""", unsafe_allow_html=True)

# === PRÉSENTATION DES FONCTIONNALITÉS ===
with st.expander("🌟 Découvrez BET ANALYST PRO", expanded=True):
    st.markdown("""
    **BET ANALYST PRO** révolutionne votre approche des paris sportifs grâce à :
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🔍 Analyse Avancée</h3>
            <ul>
                <li>Statistiques en temps réel</li>
                <li>Historique des performances</li>
                <li>Comparaison des équipes</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>📈 Outils Prédictifs</h3>
            <ul>
                <li>Modèles algorithmiques</li>
                <li>Probabilités calculées</li>
                <li>Détection des value bets</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>💰 Gestion Bankroll</h3>
            <ul>
                <li>Méthode de Kelly</li>
                <li>Suivi des performances</li>
                <li>Analyse risque/récompense</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>⚡ Live Trading</h3>
            <ul>
                <li>Matchs en cours analysés</li>
                <li>Alertes opportunités</li>
                <li>Recommandations temps réel</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# === BOUTON D'ACCÈS ===
st.markdown("""
<div style="margin: 2rem 0;">
    <h3 style="text-align: center; color: #334155;">Prêt à transformer votre approche des paris ?</h3>
</div>
""", unsafe_allow_html=True)

if st.button("🚀 Accéder à l'analyse complète", key="main_cta", use_container_width=True, type="primary"):
    try:
        st.switch_page("pages/analyser.py")
    except:
        try:
            st.switch_page("analyser.py")
        except Exception as e:
            st.error("Module d'analyse non trouvé")
            st.info("""
            Le module principal d'analyse n'est pas disponible.
            Vérifiez que le fichier `analyser.py` est présent dans votre dossier.
            """)

# === FOOTER ===
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #64748B; font-size: 0.8rem;">
    <p>Version {CONFIG['VERSION']} | © {datetime.now().year} {CONFIG['APP_NAME']}</p>
    <p><small>Les paris sportifs comportent des risques. À utiliser avec modération.</small></p>
</div>
""", unsafe_allow_html=True)
