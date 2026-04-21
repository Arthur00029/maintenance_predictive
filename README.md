# Predictive Maintenance System (ML + Monitoring + API + Dashboard)

##  Description

Ce projet est un système complet de **maintenance prédictive industrielle** basé sur des données capteurs.

Il permet de :
- prédire le **Remaining Useful Life (RUL)** des machines
- détecter les **anomalies de fonctionnement**
- surveiller la **dérive des données (data drift)**
- fournir une API de prédiction déployable
- visualiser les résultats via un dashboard de monitoring

---

##  Objectifs du projet

- Anticiper les pannes machines grâce au machine learning
- Simuler un pipeline industriel end-to-end
- Mettre en production un modèle ML
- Surveiller la performance du modèle dans le temps

---

##  Architecture du projet

dataset → preprocessing → ML model → API FastAPI → Docker → Monitoring → Dashboard


---

##  Modèles utilisés

- **XGBoost** : prédiction du RUL
- **Isolation Forest** : détection d’anomalies

---

## 📊 Monitoring

Un module de monitoring a été ajouté pour :

- logging des prédictions
- détection de data drift
- détection d’entrées anormales
- suivi des performances en production

---

## 🚀 API (FastAPI)

### Endpoint principal

`POST /predict`

### Input

json
{
  "data": [feature_1, feature_2, ..., feature_27]
}

### Output

{
  "RUL": 189.0,
  "anomaly": 1,
  "drift_detected": true,
  "drift_score": 1.93,
  "input_warning": true
}
