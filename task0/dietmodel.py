# -*- coding: utf-8 -*-

from gurobipy import *

def solve(speisen, kalorien, fett, kosten, minKalorien, maxFett, obst):

  # Gurobi-Modell erzeugen.
  model = Model("Diätenplanung")

  # Problem ist ein Minimierungsproblem.
  model.modelSense = GRB.MINIMIZE

  # Variablen-Dictionary fuer den Kauf anlegen.
  xKaufen = {}
  # Variablen in Gurobi erzeugen und hinzufuegen.
  for speise in speisen:
    xKaufen[speise] = model.addVar(obj = kosten[speise], name = ('x_' + speise))

  # Variablen bekannt machen.
  model.update()

  # Constraint: Mindestmenge an Kalorien.
  model.addConstr(quicksum(kalorien[speise] * xKaufen[speise] for speise in speisen) >= minKalorien)
  
  # Constraint: Maximalmenge an Fett.
  # Wurde vergessen.

  # Constraint: Ein Drittel der Gesamtmenge muss Obst sein.
  model.addConstr(1.0/3.0 * quicksum(xKaufen[speise] for speise in speisen) <= quicksum(xKaufen[speise] for speise in obst))

  # Problem loesen lassen.
  model.optimize()

  # Ausgabe der Loesung.
  if model.status == GRB.OPTIMAL:
    print('\nOptimaler Zielfunktionswert: %g\n' % model.ObjVal)
    for speise in speisen:
      print('Es werden %g Mengeneinheiten von %s gekauft.' % (xKaufen[speise].x, speise))
  else:
    print('Keine Optimalloesung gefunden. Status: %i' % (model.status))

  return model
