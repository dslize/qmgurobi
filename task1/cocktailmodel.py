# coding=utf-8

from gurobipy import *

def solve(zutaten, preis, alkohol, zucker, kalorien, minAlkohol, maxAlkohol, minZucker, maxKalorien, minVolumen):
  # Modell erzeugen:
  model = Model("Cocktailmischung")
  
  #Minimierungsproblem
  model.modelSense = GRB.MINIMIZE

  # Variablen erzeugen: Zunaechst leeres Dictionary.
  x = {} 

  # Alle Variablen der Liste durchlaufen.
  for zutat in zutaten:
    # Fuer jede Zutat wird die Variable "x_ZUTAT" angelegt. Implizit lower bound = 0.0.
    x[zutat] = model.addVar(name = ("x_" + zutat), obj = preis[zutat]) 

  # Variablen dem Modell bekannt machen.
  model.update()

  # Erste Nebenbedingung:
  # Bedeutung: Volumen muss mindestens <minVolumen> sein.
  # Ungleichung: "Summe aller Variablen >= minVolumen"
  model.addConstr(quicksum(x[zutat] for zutat in zutaten) >= minVolumen)

  # Zweite Nebenbedingung:
  # Bedeutung: Alkoholgehalt muss mindestens <minAlkohol> sein.
  # Ungleichung: "Summe der Alkoholgehalte multipliziert mit der Anzahl der Zutat, geteilt durch Summe aller Variablen >= minAlkohol"
  #              "Obere Bedingung nicht linear, also auf beiden Seiten mit Nenner multiplizieren, legitim da Variablen nichtnegativ"
  model.addConstr(quicksum(alkohol[zutat] * x[zutat] for zutat in zutaten) >= minAlkohol * quicksum(x[zutat] for zutat in zutaten))

  # Dritte Nebenbedingung:
  # Bedeutung: Alkoholgehalt muss höchstens <maxAlkohol> sein.
  # Ungleichung: "Summe der Alkoholgehalte multipliziert mit der Anzahl der Zutat, geteilt durch Summe aller Variablen <= minAlkohol"
  #              "Obere Bedingung nicht linear, also auf beiden Seiten mit Nenner multiplizieren, legitim da Variablen nichtnegativ"
  model.addConstr(quicksum(alkohol[zutat] * x[zutat] for zutat in zutaten) <= maxAlkohol * quicksum(x[zutat] for zutat in zutaten))

  # Vierte Nebenbedingung:
  # Bedeutung: Zuckermenge muss mindestens <minZucker> sein.
  # Ungleichung: "Summe aller Zuckermengen, jeweils multipliziert mit der Anzahl der Zutat >= minZucker"
  model.addConstr(quicksum(zucker[zutat] * x[zutat] for zutat in zutaten) >= minZucker)

  # Fuenfte Nebenbedingung:
  # Bedeutung: Kalorienanzahl muss höchstens <maxKalorien> sein.
  # Ungleichung: "Summe aller Kalorienanzahlen, jeweils multipliziert mit der Anzahl der Zutat <= maxKalorien"
  model.addConstr(quicksum(kalorien[zutat] * x[zutat] for zutat in zutaten) <= maxKalorien)

  # Nebenbedingungen hinzugefuegt? LP loesen lassen!
  model.optimize()

  # Cocktailpreis und einzelne Mengen ausgeben.
  if model.status == GRB.OPTIMAL:
    print('\nPreis des Cocktails: %g' % model.ObjVal)
    for zutat in zutaten:
      print('Menge von %s im Cocktail: %g' % (zutat, x[zutat].x))
  else:
    print('Keine Optimalloesung gefunden. Status: %i' % (model.status))

  # Modell zurueckgeben.
  return model
