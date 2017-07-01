# Dies ist eine Instanzdatei mit konkreten Daten, Sie muessen diese Datei nicht aendern!

from gurobipy import *

# Staedte: Liste der Staedte (als str)
# Gueter: Liste der Gueter (als str)
staedte = ['Aachen', 'Muenchen', 'Berlin', 'Koeln', 'Hamburg','Frankfurt']
gueter = ['Printen', 'Lennet Bier', 'RWTH Tassen']

# kosten: Dictionary der Transportkosten einer Charge pro Stunde: z.B.: kosten["Printen"] = 2
gueter, kosten = multidict({
 'Printen': 2,
 'Lennet Bier': 0.5,
 'RWTH Tassen': 0.2
 })

# fahrzeiten: Dictionary der Fahrzeiten (in Stunden) zwischen Paaren von Staedten z.B.: fahrzeiten['Aachen', 'Berlin'] = 28
# kapazitaeten: Dictionary der Kapazitaeten (in Anzahl an Chargen) zwischen Paaren von Staedten z.B.: kapazitaeten['Aachen', 'Juelich'] = 70
fahrzeiten ={ (i , j) : 0 for i in staedte for j in staedte}
kapazitaeten = { (i , j) : 0 for i in staedte for j in staedte}

# verfuegbarkeiten: Dictionary der Verfuegbarkeiten (in Anzahl an Chargen) von Guetern in Staedten z.B.: verfuegbarkeiten[('Aachen','RWTH Tassen')] = 45
# bedarfe: Dictionary der Bedarfe (in Anzahl an Chargen) von Guetern in Staedten z.B.: bedarfe[('Aachen','Printen')] = 20
verfuegbarkeiten = { (i , k) : 0 for i in staedte for k in gueter}
bedarfe = { (i , k) : 0 for i in staedte for k in gueter}

fahrzeiten[('Aachen','Muenchen')] = 28
fahrzeiten[('Aachen','Berlin')] = 31
fahrzeiten[('Aachen','Koeln')] = 32
fahrzeiten[('Aachen','Hamburg')] = 16
fahrzeiten[('Aachen','Frankfurt')] = 22
fahrzeiten[('Muenchen','Aachen')] = 28
fahrzeiten[('Muenchen','Berlin')] = 25
fahrzeiten[('Muenchen','Koeln')] = 18
fahrzeiten[('Muenchen','Hamburg')] = 19
fahrzeiten[('Muenchen','Frankfurt')] = 42
fahrzeiten[('Berlin','Aachen')] = 31
fahrzeiten[('Berlin','Muenchen')] = 25
fahrzeiten[('Berlin','Koeln')] = 41
fahrzeiten[('Berlin','Hamburg')] = 30
fahrzeiten[('Berlin','Frankfurt')] = 15
fahrzeiten[('Koeln','Aachen')] = 32
fahrzeiten[('Koeln','Muenchen')] = 18
fahrzeiten[('Koeln','Berlin')] = 41
fahrzeiten[('Koeln','Hamburg')] = 19
fahrzeiten[('Koeln','Frankfurt')] = 48
fahrzeiten[('Hamburg','Aachen')] = 16
fahrzeiten[('Hamburg','Muenchen')] = 19
fahrzeiten[('Hamburg','Berlin')] = 30
fahrzeiten[('Hamburg','Koeln')] = 19
fahrzeiten[('Hamburg','Frankfurt')] = 32
fahrzeiten[('Frankfurt','Aachen')] = 22
fahrzeiten[('Frankfurt','Muenchen')] = 42
fahrzeiten[('Frankfurt','Berlin')] = 15
fahrzeiten[('Frankfurt','Koeln')] = 48
fahrzeiten[('Frankfurt','Hamburg')] = 32
kapazitaeten[('Aachen','Muenchen')] = 70
kapazitaeten[('Aachen','Berlin')] = 70
kapazitaeten[('Aachen','Koeln')] = 60
kapazitaeten[('Aachen','Hamburg')] = 60
kapazitaeten[('Aachen','Frankfurt')] = 50
kapazitaeten[('Muenchen','Aachen')] = 70
kapazitaeten[('Muenchen','Berlin')] = 60
kapazitaeten[('Muenchen','Koeln')] = 60
kapazitaeten[('Muenchen','Hamburg')] = 60
kapazitaeten[('Muenchen','Frankfurt')] = 50
kapazitaeten[('Berlin','Aachen')] = 70
kapazitaeten[('Berlin','Muenchen')] = 60
kapazitaeten[('Berlin','Koeln')] = 60
kapazitaeten[('Berlin','Hamburg')] = 60
kapazitaeten[('Berlin','Frankfurt')] = 50
kapazitaeten[('Koeln','Aachen')] = 60
kapazitaeten[('Koeln','Muenchen')] = 60
kapazitaeten[('Koeln','Berlin')] = 60
kapazitaeten[('Koeln','Hamburg')] = 60
kapazitaeten[('Koeln','Frankfurt')] = 50
kapazitaeten[('Hamburg','Aachen')] = 60
kapazitaeten[('Hamburg','Muenchen')] = 60
kapazitaeten[('Hamburg','Berlin')] = 60
kapazitaeten[('Hamburg','Koeln')] = 60
kapazitaeten[('Hamburg','Frankfurt')] = 50
kapazitaeten[('Frankfurt','Aachen')] = 50
kapazitaeten[('Frankfurt','Muenchen')] = 50
kapazitaeten[('Frankfurt','Berlin')] = 50
kapazitaeten[('Frankfurt','Koeln')] = 50
kapazitaeten[('Frankfurt','Hamburg')] = 50 

verfuegbarkeiten[('Aachen','RWTH Tassen')] = 45
verfuegbarkeiten[('Muenchen','Printen')] = 30
verfuegbarkeiten[('Berlin','Lennet Bier')] = 35
verfuegbarkeiten[('Koeln','RWTH Tassen')] = 25
verfuegbarkeiten[('Hamburg','Lennet Bier')] = 35
verfuegbarkeiten[('Frankfurt','Printen')] = 20

bedarfe[('Aachen','Printen')] = 20
bedarfe[('Aachen','Lennet Bier')] = 20
bedarfe[('Muenchen','Lennet Bier')] = 20
bedarfe[('Muenchen','RWTH Tassen')] = 20
bedarfe[('Berlin','Printen')] = 10
bedarfe[('Berlin','RWTH Tassen')] = 10
bedarfe[('Koeln','Printen')] = 10
bedarfe[('Koeln','Lennet Bier')] = 20
bedarfe[('Hamburg','Printen')] = 10
bedarfe[('Hamburg','RWTH Tassen')] = 20
bedarfe[('Frankfurt','Lennet Bier')] = 10
bedarfe[('Frankfurt','RWTH Tassen')] = 20

import transportmodel

model = transportmodel.solve(staedte, gueter, fahrzeiten, kosten, kapazitaeten, verfuegbarkeiten, bedarfe)

if not isinstance(model, Model):
  print("solve-Funktion gibt kein Gurobi-Modell zurueck!")

