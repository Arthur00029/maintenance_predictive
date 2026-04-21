import numpy as np
import json
from datetime import datetime

class Monitoring:

    def __init__(self, reference_data):
        self.reference_mean = np.mean(reference_data, axis=0)
        self.logs = []

    def log_prediction(self, input_data, prediction, anomaly):
        log_entry = {
            "timestamp": str(datetime.now()),
            "input": input_data.tolist(),
            "prediction": float(prediction),
            "anomaly": int(anomaly)
        }
        self.logs.append(log_entry)

        # sauvegarde fichier
        with open("logs.json", "a") as f:
            f.write(json.dumps(log_entry) + "\n")

    def detect_drift(self, input_data):
        current_mean = np.mean(input_data, axis=0)
        drift = np.abs(current_mean - self.reference_mean)

        drift_score = drift.mean()

        if drift_score > 0.1:
            return True, drift_score
        return False, drift_score

    def check_input_anomaly(self, input_data):
        if np.any(input_data > 1000) or np.any(input_data < -1000):
            return True
        return False