import streamlit as st
import datetime
import sys
import os
from pathlib import Path

# === CONFIGURATION ===
CONFIG = {
    "APP_NAME": "BET ANALYST PRO",
    "VERSION": "2.1",
    "PRIMARY_COLOR": "#2563EB",
    "SECONDARY_COLOR": "#1E40AF",
    "ANALYSIS_PAGE": "analyser.py"  # Nom du fichier d'analyse
}

# === VÉRIFICATION DES FICHIERS ===
def check_analysis_file():
    """Vérifie la présence du fichier d'analyse"""
    # Essayer dans le dossier pages/
    pages_path = Path("pages") / CONFIG["ANALYSIS_PAGE"]
    if pages_path.exists():
        return str(pages_path)
    
    # Essayer dans le dossier courant
    current_path = Path(CONFIG["ANALYSIS_PAGE"])
    if current_path.exists():
        return str(current_path)
    
    return None

# === INITIALISATION STREAMLIT ===
st.set_page_config(
    page_title=f"{CONFIG['APP_NAME']} - Analyse Sportive",
    page_icon="📊",
    layout="centered"
)

# === CSS PERSONNALISÉ ===
st.markdown(f"""
<style>
    .header {{
        text-align: center;
        padding: 1rem 0;
    }}
    .title {{
        color: {CONFIG['PRIMARY_COLOR']};
        font-size: 2.5rem;
        font-weight: 800;
    }}
    .cta-button {{
        background: {CONFIG['PRIMARY_COLOR']} !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 0.5rem 1rem !important;
        border-radius: 0.5rem !important;
        margin-top: 1.5rem !important;
    }}
    .feature-card {{
        border-left: 4px solid {CONFIG['PRIMARY_COLOR']};
        padding: 1rem;
        margin: 1rem 0;
        background: #f8fafc;
    }}
</style>
""", unsafe_allow_html=True)

# === HEADER ===
st.markdown("""
<div class="header">
    <h1 class="title">BET ANALYST PRO</h1>
    <p>L'outil professionnel d'analyse des paris sportifs</p>
</div>
""", unsafe_allow_html=True)

# === CONTENU PRINCIPAL ===
with st.expander("✨ Fonctionnalités", expanded=True):
    st.markdown("""
    <div class="feature-card">
        <h3>📊 Analyse Complète</h3>
        <p>Statistiques détaillées et prédictions précises</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>⚡ Live Betting</h3>
        <p>Analyse en temps réel des matchs en cours</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>💰 Gestion Bankroll</h3>
        <p>Recommandations de mise optimisées</p>
    </div>
    """, unsafe_allow_html=True)

# === SOLUTION ROBUSTE POUR LA NAVIGATION ===
analysis_file = check_analysis_file()

if analysis_file:
    if st.button("🔍 Accéder à l'analyse complète", key="main_cta", use_container_width=True):
        try:
            # Deux méthodes pour gérer la navigation :
            
            # Méthode 1: Switch page (Streamlit >= 1.25)
            if hasattr(st, 'switch_page'):
                st.switch_page(analysis_file)
            
            # Méthode 2: Exécution directe (compatibilité)
            else:
                with open(analysis_file, encoding='utf-8') as f:
                    exec(f.read(), globals())
        
        except Exception as e:
            st.error(f"Erreur lors du chargement: {str(e)}")
else:
    st.error("Module d'analyse non trouvé")
    st.markdown("""
    ### Pour résoudre ce problème :
    
    1. Créez un fichier nommé `analyser.py`
    2. Placez-le soit :
       - À la racine de votre projet
       - Dans un dossier `pages/`
    3. Vérifiez que le fichier contient le code d'analyse
    """)

    if st.button("🔄 Réessayer la détection", help="Cliquez pour vérifier à nouveau"):
        st.experimental_rerun()

# === FOOTER ===
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #64748B; font-size: 0.8rem;">
    <p>{CONFIG['APP_NAME']} v{CONFIG['VERSION']} • © {datetime.datetime.now().year}</p>
    <p><small>Jouez responsablement • Les paris sportifs comportent des risques</small></p>
</div>
""", unsafe_allow_html=True)