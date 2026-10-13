import streamlit as st

st.title("📄 Curriculum Vitae")

st.header("Expérience")
st.markdown("""
* **Poste actuel** - *Entreprise* (Année) : Description...
* **Poste précédent** - *Entreprise* (Année) : Description...
""")

st.header("Compétences")
st.progress(80, text="Python")
st.progress(70, text="Streamlit")

st.header("Formation")
st.markdown("...")