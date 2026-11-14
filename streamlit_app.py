
import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Fonction pour charger une animation Lottie depuis le web
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.title("🌙 Mars Mission - Circadian Module")

# Exemple d'animation (ici un cercle de chargement / pulsation futuriste)
# Tu peux remplacer l'URL par n'importe quelle animation Lottie gratuite (fleur, nature, techno)
lottie_flower = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_jcikwtux.json")

if lottie_flower:
    st_lottie(lottie_flower, speed=1, height=200, key="flower")

sleep_hours = st.slider("Temps de sommeil (heures) :", 0.0, 12.0, 7.0, 0.5)

if sleep_hours <= 5.0:
    st.error("🚨 Alerte Critique (Seuil HERA <= 5h)")
else:
    st.success("✅ Statut Nominal")
