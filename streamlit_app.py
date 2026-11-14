import streamlit as st
import pandas as pd

# Configuration de la page (Design dashboard spatial)
st.set_page_config(
    page_title="Mars Mission - Sleep Module",
    page_icon="🌙",
    layout="centered"
)

# En-tête principal
st.title("🌙 Mars Mission Copilot")
st.subheader("Module de Suivi du Sommeil & Rythme Circadien")
st.markdown("---")

# Section de saisie pour l'astronaute
st.markdown("### 📥 Enregistrement du Sommeil Quotidien")
sleep_hours = st.slider("Combien d'heures as-tu dormies cette nuit ?", 0.0, 12.0, 7.0, 0.5)
co2_level = st.slider("Niveau de CO2 dans les quartiers (mmHg)", 1.0, 6.0, 2.5, 0.1)

# Analyse selon les seuils scientifiques (NASA / HERA)
st.markdown("### 📊 Analyse & Alertes en Temps Réel")

if sleep_hours <= 5.0:
    st.error(f"🚨 **ALERTE ROUGE (Critique) :** {sleep_hours}h de sommeil. En dessous du seuil HERA ($\le 5\text{h}$). **Verrouillage des tâches de précision (Bras robotique / EVA).**")
elif sleep_hours < 7.0:
    st.warning(f"⚠️ **Attention :** {sleep_hours}h de sommeil. Sommeil insuffisant, fatigue modérée détectée.")
else:
    st.success(f"✅ **Nominal :** {sleep_hours}h de sommeil. Performances optimales.")

# Vérification du CO2 dans la cabine
if co2_level > 3.0:
    st.warning(f"⚠️ **Qualité de l'air :** Niveau de $CO_2$ élevé ({co2_level} mmHg). Risque de perturbation du sommeil. Ventilation ajustée.")
else:
    st.info(f"💨 **Environnement de sommeil :** $CO_2$ nominal ({co2_level} mmHg).")

# Section Check-list d'hygiène et de relaxation
st.markdown("---")
st.markdown("### 🧘 Protocoles de Contre-Mesure (NASA)")
st.checkbox("Éclairage SSLA réglé en mode chaud / tamisé (2h avant le coucher)")
st.checkbox("Check-list Sleep CBT (Gestion du stress pré-sommeil) validée")
st.checkbox("Bloc de relaxation et self-care quotidien complété")
