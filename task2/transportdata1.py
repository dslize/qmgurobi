# Dies ist eine Instanzdatei mit konkreten Daten, Sie muessen diese Datei nicht aendern!

from gurobipy import *

# Staedte: Liste der Staedte (als str)
# Gueter: Liste der Gueter (als str)
staedte = ['Aachen', 'Juelich', 'Geilenkirchen', 'Dueren', 'Eschweiler','Heerlen']
gueter = ['Atommuell', 'Babynahrung', 'Regenschirme', 'Schokoladenosterhasen']

# kosten: Dictionary der Transportkosten einer Charge pro Stunde: z.B.: kosten["Atommuell"]=2
gueter, kosten = multidict({
 'Atommuell': 2,
 'Babynahrung': 0.5,
 'Regenschirme': 0.2,
 'Schokoladenosterhasen': 0.35
})

# fahrzeiten: Dictionary der Fahrzeiten (in Stunden) zwischen Paaren von Staedten z.B.: fahrzeiten['Aachen', 'Juelich'] = 28
# kapazitaeten: Dictionary der Kapazitaeten (in Anzahl an Chargen) zwischen Paaren von Staedten z.B.: kapazitaeten['Aachen', 'Juelich'] = 70
fahrzeiten = { (i , j) : 0 for i in staedte for j in staedte}
kapazitaeten = { (i , j) : 0 for i in staedte for j in staedte}

# verfuegbarkeiten: Dictionary der Verfuegbarkeiten (in Anzahl an Chargen) von Guetern in Staedten z.B.: verfuegbarkeiten[('Aachen','Regenschirme')] = 45
# bedarfe: Dictionary der Bedarfe (in Anzahl an Chargen) von Guetern in Staedten z.B.: bedarfe[('Aachen','Atommuell')] = 20
verfuegbarkeiten = { (i , k) : 0 for i in staedte for k in gueter}
bedarfe = { (i , k) : 0 for i in staedte for k in gueter}

fahrzeiten[('Aachen','Juelich')] = 28
fahrzeiten[('Aachen','Geilenkirchen')] = 31
fahrzeiten[('Aachen','Dueren')] = 32
fahrzeiten[('Aachen','Eschweiler')] = 16
fahrzeiten[('Aachen','Heerlen')] = 22
fahrzeiten[('Juelich','Aachen')] = 28
fahrzeiten[('Juelich','Geilenkirchen')] = 25
fahrzeiten[('Juelich','Dueren')] = 18
fahrzeiten[('Juelich','Eschweiler')] = 19
fahrzeiten[('Juelich','Heerlen')] = 42
fahrzeiten[('Geilenkirchen','Aachen')] = 31
fahrzeiten[('Geilenkirchen','Juelich')] = 25
fahrzeiten[('Geilenkirchen','Dueren')] = 41
fahrzeiten[('Geilenkirchen','Eschweiler')] = 30
fahrzeiten[('Geilenkirchen','Heerlen')] = 15
fahrzeiten[('Dueren','Aachen')] = 32
fahrzeiten[('Dueren','Juelich')] = 18
fahrzeiten[('Dueren','Geilenkirchen')] = 41
fahrzeiten[('Dueren','Eschweiler')] = 19
fahrzeiten[('Dueren','Heerlen')] = 48
fahrzeiten[('Eschweiler','Aachen')] = 16
fahrzeiten[('Eschweiler','Juelich')] = 19
fahrzeiten[('Eschweiler','Geilenkirchen')] = 30
fahrzeiten[('Eschweiler','Dueren')] = 19
fahrzeiten[('Eschweiler','Heerlen')] = 32
fahrzeiten[('Heerlen','Aachen')] = 22
fahrzeiten[('Heerlen','Juelich')] = 42
fahrzeiten[('Heerlen','Geilenkirchen')] = 15
fahrzeiten[('Heerlen','Dueren')] = 48
fahrzeiten[('Heerlen','Eschweiler')] = 32
kapazitaeten[('Aachen','Juelich')] = 70
kapazitaeten[('Aachen','Geilenkirchen')] = 70
kapazitaeten[('Aachen','Dueren')] = 60
kapazitaeten[('Aachen','Eschweiler')] = 60
kapazitaeten[('Aachen','Heerlen')] = 50
kapazitaeten[('Juelich','Aachen')] = 70
kapazitaeten[('Juelich','Geilenkirchen')] = 60
kapazitaeten[('Juelich','Dueren')] = 60
kapazitaeten[('Juelich','Eschweiler')] = 60
kapazitaeten[('Juelich','Heerlen')] = 50
kapazitaeten[('Geilenkirchen','Aachen')] = 70
kapazitaeten[('Geilenkirchen','Juelich')] = 60
kapazitaeten[('Geilenkirchen','Dueren')] = 60
kapazitaeten[('Geilenkirchen','Eschweiler')] = 60
kapazitaeten[('Geilenkirchen','Heerlen')] = 50
kapazitaeten[('Dueren','Aachen')] = 60
kapazitaeten[('Dueren','Juelich')] = 60
kapazitaeten[('Dueren','Geilenkirchen')] = 60
kapazitaeten[('Dueren','Eschweiler')] = 60
kapazitaeten[('Dueren','Heerlen')] = 50
kapazitaeten[('Eschweiler','Aachen')] = 60
kapazitaeten[('Eschweiler','Juelich')] = 60
kapazitaeten[('Eschweiler','Geilenkirchen')] = 60
kapazitaeten[('Eschweiler','Dueren')] = 60
kapazitaeten[('Eschweiler','Heerlen')] = 50
kapazitaeten[('Heerlen','Aachen')] = 50
kapazitaeten[('Heerlen','Juelich')] = 50
kapazitaeten[('Heerlen','Geilenkirchen')] = 50
kapazitaeten[('Heerlen','Dueren')] = 50
kapazitaeten[('Heerlen','Eschweiler')] = 50 

verfuegbarkeiten[('Aachen','Regenschirme')] = 45
verfuegbarkeiten[('Aachen','Schokoladenosterhasen')] = 40
verfuegbarkeiten[('Juelich','Atommuell')] = 30
verfuegbarkeiten[('Juelich','Schokoladenosterhasen')] = 10
verfuegbarkeiten[('Geilenkirchen','Babynahrung')] = 35
verfuegbarkeiten[('Dueren','Regenschirme')] = 25
verfuegbarkeiten[('Dueren','Schokoladenosterhasen')] = 10
verfuegbarkeiten[('Eschweiler','Babynahrung')] = 35
verfuegbarkeiten[('Heerlen','Atommuell')] = 20

bedarfe[('Aachen','Atommuell')] = 20
bedarfe[('Aachen','Babynahrung')] = 20
bedarfe[('Juelich','Babynahrung')] = 20
bedarfe[('Juelich','Regenschirme')] = 20
bedarfe[('Geilenkirchen','Atommuell')] = 10
bedarfe[('Geilenkirchen','Regenschirme')] = 10
bedarfe[('Geilenkirchen','Schokoladenosterhasen')] = 20
bedarfe[('Dueren','Atommuell')] = 10
bedarfe[('Dueren','Babynahrung')] = 20
bedarfe[('Eschweiler','Atommuell')] = 10
bedarfe[('Eschweiler','Regenschirme')] = 20
bedarfe[('Eschweiler','Schokoladenosterhasen')] = 20
bedarfe[('Heerlen','Babynahrung')] = 10
bedarfe[('Heerlen','Regenschirme')] = 20
bedarfe[('Heerlen','Schokoladenosterhasen')] = 20

import transportmodel

model = transportmodel.solve(staedte, gueter, fahrzeiten, kosten, kapazitaeten, verfuegbarkeiten, bedarfe)

if not isinstance(model, Model):
  print("solve-Funktion gibt kein Gurobi-Modell zurueck!")

