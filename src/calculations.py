import numpy as np
import pandas as pd


def calculate_power_curve(leistung, zeitaufloesung=1):
    """
    Berechnet die Power Curve aus Leistungsdaten.

    Parameter:
        leistung       : Leistungswerte (pd.Series oder np.ndarray)
        zeitaufloesung : Sekunden pro Datenpunkt (Standard: 1)

    Rückgabe:
        pd.DataFrame mit Spalten 'zeit_sek' und 'leistung_w'
    """
    leistung = pd.Series(leistung)
    total_seconds = len(leistung)
    
    durations = np.unique(
    np.logspace(0, np.log10(total_seconds), num=100).astype(int)
)
  
    zeit_sek = []
    beste_leistung = []

    for fenster in durations:
        bester_wert = leistung.rolling(window=fenster).mean().max()
        zeit_sek.append(fenster * zeitaufloesung)
        beste_leistung.append(bester_wert)

    return pd.DataFrame({
        "zeit_sek": zeit_sek,
        "leistung_w": beste_leistung
    })




