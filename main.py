from src.read_csv import leistung
from src.calculations import calculate_power_curve
from src.make_plot import plot_power_curve

power_curve = calculate_power_curve(leistung)
#print(len(leistung), "Sekunden")
#print(len(leistung) / 60, "Minuten")

  

plot_power_curve(power_curve)
