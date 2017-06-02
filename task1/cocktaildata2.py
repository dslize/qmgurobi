from gurobipy import *

# Die ist eine Instanzdatei mit konkreten Daten, Sie muessen diese Datei nicht aendern!

zutaten, preis, alkohol, zucker, kalorien = multidict({
    "Rum": [1.57, 0.45, 0, 247],
    "Blue_Curacao": [1.41, 0.3, 17, 243],
    "Orangensaft": [0.99, 0, 8.8, 47],
    "Amaretto": [1.73, 0.28, 30.4, 284],
    })

# zutaten: Liste der Zutaten als Strings (str).
# preis: Dictionary, das jede Zutat Ihrem Preis zuordnet, also z.B. preis['Rum']
# alkohol: Dictionary, das jede Zutat Ihrem Alkoholanteil zuordnet.
# zucker: Dictionary, das jede Zutat Ihrer Zuckermenge in g/100 ml zuordnet, also z.B. preis['Rum']
# kalorien: Dictionary, das jede Zutat Ihrer Kalorienmenge je 100 ml zuordnet, also z.B. preis['Rum']

maxAlkohol = 0.25 # 25%
minAlkohol = 0.15 # 15%
minZucker = 50 # in g
maxKalorien = 800
minVolumen = 2.5 # in 100 ml

import cocktailmodel

model = cocktailmodel.solve(zutaten, preis, alkohol, zucker, kalorien, minAlkohol, maxAlkohol, minZucker, maxKalorien, minVolumen)

if not isinstance(model, Model):
  print("solve-Funktion gibt kein Gurobi-Modell zurueck!")

