# coding=utf-8

from gurobipy import *

def solve(staedte, gueter, fahrzeiten, kosten, kapazitaeten, verfuegbarkeiten, bedarfe):
  model = Model("transport")

  # Ziel (Minimieren)
  model.modelSense = GRB.MINIMIZE
  
  # Variablen erzeugen.
  x = {}
  for k in gueter:
    for s1 in staedte:
      for s2 in staedte:
        x[k, s1, s2] = model.addVar(name = "x_" + k + "_" + s1 + "_" + s2, obj = kosten[k]*fahrzeiten[s1,s2])

  # Variablen dem Modell bekannt machen.
  model.update()

  # Erste Nebenbedingung:
  # Bedeutung: Von einer Stadt i können zu einer Stadt j höchstens <kapazitaeten[i,j]> Chargen geliefert werden
  # Ungleichung: Summe aller Chargen von Gütern, die von i nach j geschickt werden <= kapazitaeten[i,j]
  for i in staedte:
    for j in staedte:
        model.addConstr(quicksum(x[k, i, j] for k in gueter) <= kapazitaeten[i,j])

  # Zweite Nebenbedingung:
  # Bedeutung: Von einer Stadt i können höchstens <verfuegbarkeiten[i,k]> Chargen von Gut k geliefert werden
  # Ungleichung: Summe der Chargen von Gut k, welche von i aus in Städte j verschickt werden <= verfuegbarkeiten[i,k]
  for i in staedte:
    for k in gueter:
      model.addConstr(quicksum(x[k, i, j] for j in staedte) <= verfuegbarkeiten[i,k])

  # Dritte Nebenbedingung:
  # Bedeutung: Zu einer Stadt j müssen mindestens <bedarfe[j,k]> Chargen von Gut k geschickt werden
  # Ungleichung: Summe der Chargen von Gut k, welche zu Stadt j geliefert werden >= bedarfe[j,k]
  for j in staedte:
    for k in gueter:
        model.addConstr(quicksum(x[k, i, j] for i in staedte) >= bedarfe[j,k])

  # Nebenbedingungen hinzugefuegt? LP loesen lassen!
  model.optimize()


  # Transportmengen ausgeben.
  if model.status == GRB.OPTIMAL:
    print('\nOptimalloesung hat Kosten von %g.\n' % (model.ObjVal))
    for k in gueter:
      for s1 in staedte:
        for s2 in staedte:
          if x[k, s1, s2].x > 0.0001:
            print('Von %s nach %s werden %g Chargen von %s transportiert.' % (s1, s2, x[k, s1, s2].x, k))
  else:
    print('Keine Optimalloesung gefunden. Status: %i' % (model.status))

  return model

