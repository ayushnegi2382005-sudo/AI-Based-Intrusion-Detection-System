import pandas as pd
from sklearn.ensemble import IsolationForest
from joblib import dump
import os

df = pd.read_csv('data/live_captured_data.csv')

X = df[['packet_length', 'protocol', 'src_port', 'dst_port']]

model = IsolationForest(contamination=0.01, random_state=42)
model.fit(X)

os.makedirs("models", exist_ok=True)
dump(model, 'models/anomaly_model.pkl')

print("✅ Anomaly model trained")
