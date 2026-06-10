import os
import pandas as pd
import numpy as np


def read_leistung_data():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "..", "data", "activity.csv")
    df = pd.read_csv(csv_path)
    leistung = df["PowerOriginal"]
    leistung = leistung.replace(0, np.nan)  # Nullwerte zu NaN
    leistung = leistung.dropna()            # alle NaN raus
    return leistung

leistung = read_leistung_data()  