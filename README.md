# Leistungskurve_II

In diesem Repo wird eine Power-Curve aus Leistungsdaten in Watt berechnet.
Die Daten werden aus einer CSV-Datei eingelesen, und in einem DataFrame berechnet Danach wird ein Plot aus diesen Daten dargestellt.

## Projektstruktur
- `src` enthält die Funktionen zur Berechnung und zum Plotten der Power-Curve. 
- `main.py` liest die Daten ein und führt die Berechnung sowie den Plot aus.

## Voraussetzungen

Für das Projekt werden Python sowie die Bibliotheken `pandas`, `numpy` und `plotly` benötigt. 
Dafür starten wir im Terminal mit dem Befehl: ```pdm install```

## Ausführen

Das Projekt wird über `main.py` gestartet

## Ausgabe

Das Programm erstellt:
- eine berechnete Power-Curve als DataFrame mit Zeit in Sekunden und Leistung in Watt
- einen Plot der Power-Curve,
- sowie einen Screenshot `screenshot.png` für die Dokumentation in diesem Repository.

![Screenshot](screenshot.png)
