import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt

st.set_page_config(page_title="ML Monitoring Dashboard", layout="wide")

st.title("🏭 Monitoring - Maintenance Prédictive")

# -----------------------------
# Charger les logs
# -----------------------------
logs = []

try:
    with open("logs.json", "r") as f:
        for line in f:
            logs.append(json.loads(line))
except:
    st.warning("Pas encore de logs disponibles")

if len(logs) > 0:
    df = pd.DataFrame(logs)

    # -----------------------------
    # KPIs
    # -----------------------------
    col1, col2, col3 = st.columns(3)

    col1.metric("Nombre de prédictions", len(df))

    anomalies = df[df["anomaly"] == -1]
    col2.metric("Anomalies détectées", len(anomalies))

    col3.metric("RUL moyen", round(df["prediction"].mean(), 2))

    # -----------------------------
    # Graph RUL
    # -----------------------------
    st.subheader("📉 Évolution du RUL")

    fig, ax = plt.subplots()
    ax.plot(df["prediction"])
    ax.set_ylabel("RUL")
    ax.set_xlabel("Temps")
    st.pyplot(fig)

    # -----------------------------
    # Graph anomalies
    # -----------------------------
    st.subheader("⚠️ Anomalies")

    fig2, ax2 = plt.subplots()
    ax2.plot(df["anomaly"])
    ax2.set_ylabel("Anomaly (-1 = anomalie)")
    st.pyplot(fig2)

    # -----------------------------
    # Drift
    # -----------------------------
    if "drift_score" in df.columns:
        st.subheader("📊 Drift")

        fig3, ax3 = plt.subplots()
        ax3.plot(df["drift_score"])
        ax3.set_ylabel("Drift score")
        st.pyplot(fig3)

    # -----------------------------
    # Tableau
    # -----------------------------
    st.subheader("📋 Logs")
    st.dataframe(df.tail(50))

else:
    st.info("Lance d'abord ton API pour générer des logs.")