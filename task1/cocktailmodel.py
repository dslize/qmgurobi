# coding=utf-8

from gurobipy import *

def solve(zutaten, preis, alkohol, zucker, kalorien, minAlkohol, maxAlkohol, minZucker, maxKalorien, minVolumen):
  # Modell erzeugen:
  model = Model("Cocktailmischung")

  # Variablen erzeugen: Zunaechst leeres Dictionary.
  x = {} 

  # Alle Variablen der Liste durchlaufen.
  for zutat in zutaten:
    # Fuer jede Zutat wird die Variable "x_ZUTAT" angelegt.
    x[zutat] = model.addVar(name = ("x_" + zutat), obj = preis[zutat]) 

  # Variablen dem Modell bekannt machen.
  model.update()

  # Erste Nebenbedingung:
  # Bedeutung: Volumen muss mindestens <minVolumen> sein.
  # Ungleichung: "Summe aller Variablen >= minVolumen"

  model.addConstr( "HIER FEHLT DIE UNGLEICHUNG!" )

  # Zweite Nebenbedingung:
  # Bedeutung: ...
  # Ungleichung: ...


  # Dritte Nebenbedingung:
  # Bedeutung: ...
  # Ungleichung: ...


  # Vierte Nebenbedingung:
  # Bedeutung: ...
  # Ungleichung: ...


  # Fuenfte Nebenbedingung:
  # Bedeutung: ...
  # Ungleichung: ...


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
