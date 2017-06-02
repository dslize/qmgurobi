# -*- coding: utf-8 -*-
"""
Created on Tue May 24 00:56:12 2016

@author: luebbecke
"""

# use Gurobi's Python library
from gurobipy import *

# a very compact way to represent all data
food, calories, fat, cost = multidict({
    "apple" : [50, 0.4, 0.31],
    "peanutbutter" : [627, 49.9, 0.82],
    "milk" : [42, 0.3, 0.07],
    "bread" : [188, 1.0, 0.29]
})

# give the model a name
model = Model("diet")

# define variables, one for each food item
buy = {}
for f in food:
    # "obj" is the objective function coefficient
    buy[f] = model.addVar(obj=cost[f], name=f)

# variables are "made known to the model"
model.update()

# define the constraints
model.addConstr(quicksum(calories[f] * buy[f] for f in food) >= 2000)
model.addConstr(quicksum(fat[f] * buy[f] for f in food) <= 20)
model.addConstr(1/3. * quicksum(buy[f] for f in food) <= buy["apple"])

# now solve the model
model.optimize()

# for debugging and information purposes, write out LP 
model.write("diet.lp")

# let's have a look at the solution
for f in food:
    print "eat " + str(buy[f].x) + " units of " + str(f)
print "Total cost: " + str(model.Objval)




