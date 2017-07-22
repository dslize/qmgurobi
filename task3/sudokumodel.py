# coding=utf-8

from gurobipy import *

def solve(G):
  model = Model("sudoku")

  # Ziel (Minimieren oder Maximieren?)

  # Variablen erzeugen.
  x = {}
  for i in range(1,10):
    for j in range(1,10):
      for k in range(1,10):
        x[i,j,k] = model.addVar(name = "x_"+str(i)+"_"+str(j)+"_"+str(k), vtype=GRB.INTEGER, lb=0, ub=1)

  # Variablen dem Modell bekannt machen.
  model.update()

  # Erste Nebenbedingung:
  # Bedeutung: In jedem Feld steht genau eine Zahl aus range(1,10)
  # (Un)gleichung: ...
  for i in range(1,10):
    for j in range(1,10):
      model.addConstr(quicksum(x[i,j,k] for k in range(1,10)) == 1)

  # Zweite Nebenbedingung:
  # Bedeutung: Jede Zahl taucht in einer Zeile genau einmal auf.
  # (Un)gleichung: ...
  for i in range(1,10):
    for k in range(1,10):
      model.addConstr(quicksum(x[i,j,k] for j in range(1,10)) == 1)
      
  # Dritte Nebenbedingung:
  # Bedeutung: Jede Zahl taucht in einer Spalte genau einmal auf.
  # (Un)gleichung: ...
  for j in range(1,10):
    for k in range(1,10):
      model.addConstr(quicksum(x[i,j,k] for i in range(1,10)) == 1)

  # Vierte Nebenbedingung:
  # Bedeutung: Jede Zahl taucht in einem Teilquadrat genau einmal auf.
  # (Un)gleichung: ...
  for m in range(0,3):        # Iteriere über Teilquadrate einer Zeile (0-indiziert)
    for n in range(0,3):      # Iteriere über Teilquadrate einer Spalte (0-indiziert)
      for k in range(1,10):
        model.addConstr(quicksum(x[i+(m*3), j+(n*3), k] for i in range(1,4) for j in range(1,4)) == 1)

  # Fuenfte Nebenbedingung:
  # Bedeutung: Die gegebenen Felder setzen.
  # (Un)gleichung: ...
  for (i,j,k) in G:
    model.addConstr(x[i,j,k] == 1)

  # Nebenbedingungen hinzugefuegt? IP loesen lassen!
  model.optimize()

  # Sudoku ausgeben.
  if model.status == GRB.OPTIMAL:
    print '\nGeloestes Sudoku:'
    for i in range(1,10):
      zeile = ''
      for j in range(1,10):
        zahl = '-'
        for k in range(1,10):
          if x[i,j,k].x > 0.5:
            zahl = k
        zeile += ' ' + str(zahl)
      print zeile
  else:
    print('\nEs gibt keine korrekte Belegung.')

  return model

