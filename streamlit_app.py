import streamlit as st

st.title("🌙 Mars Mission - Sleep Tracker")

sleep_hours = st.slider("Combien d'heures as-tu dormies ?", 0.0, 12.0, 7.0, 0.5)

if sleep_hours >= 7.0 and sleep_hours <= 9.0:
    st.success("✅ Sommeil optimal validé !")
    # Déclenche une animation visuelle de bulles/ballons à l'écran
    st.balloons()

