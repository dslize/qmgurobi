# Dies ist eine Instanzdatei mit konkreten Daten, Sie muessen diese Datei nicht aendern!

from gurobipy import *

G = [
  (1,1,2), (1,2,5), (1,5,3), (1,7,9), (1,9,1),
  (2,2,1), (2,6,4),
  (3,1,4), (3,3,7), (3,7,2), (3,9,8),
  (4,3,5), (4,4,2),
  (5,5,9), (5,6,8), (5,7,1),
  (6,2,4), (6,6,3),
  (7,4,3), (7,5,6), (7,8,7), (7,9,2),
  (8,2,7), (8,9,3),
  (9,1,9), (9,3,3), (9,7,6), (9,9,4)
]

import sudokumodel

model = sudokumodel.solve(G)

if not isinstance(model, Model):
  print("solve-Funktion gibt kein Gurobi-Modell zurueck!")

