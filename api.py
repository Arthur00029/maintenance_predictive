from fastapi import FastAPI
import numpy as np
import pickle
from monitoring import Monitoring
from pydantic import BaseModel
import traceback


class InputData(BaseModel):
    data: list

app = FastAPI()


# exemple : utilise X_train pour référence
reference_data = np.load("reference.npy")

monitor = Monitoring(reference_data)

# charger modèle (à sauvegarder avant avec pickle)
model = pickle.load(open("model.pkl", "rb"))
model_anomaly = pickle.load(open("anomaly.pkl", "rb"))



@app.post("/predict")
def predict(input: InputData):

    try:
        X = np.array(input.data).reshape(1, -1)

        rul = model.predict(X)[0]
        anomaly = model_anomaly.predict(X)[0]

        monitor.log_prediction(X, rul, anomaly)

        drift_flag, drift_score = monitor.detect_drift(X)
        input_issue = monitor.check_input_anomaly(X)

        return {
            "RUL": float(rul),
            "anomaly": int(anomaly),
            "drift_detected": drift_flag,
            "drift_score": float(drift_score),
            "input_warning": input_issue
        }

    except Exception as e:
        print(traceback.format_exc())
        return {"error": str(e)}