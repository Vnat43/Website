import streamlit as st

st.set_page_config(layout="wide", page_title="Mon Site Personnel")

# --- NAVIGATION ---
# Définition des pages
accueil = st.Page("pages/1_accueil.py", title="Accueil & Présentation", icon="🏠")
cv = st.Page("pages/2_cv.py", title="Mon CV", icon="📄")
portfolio = st.Page("pages/3_portfolio.py", title="Projets Informatiques", icon="💻")
rando = st.Page("pages/4_randonnees.py", title="Mes Randonnées", icon="🥾")

# Création du menu latéral
pg = st.navigation(
    {
        "Présentation": [accueil, cv],
        "Mes Passions": [portfolio, rando],
    }
)

# Lancement de la navigation
pg.run()