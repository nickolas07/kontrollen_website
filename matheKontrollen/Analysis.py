import importlib
import sys

from skripte.erstellen import *
from funktionen import get_aufgaben

# Angaben für den Test im pdf-Dokument
probe = sys.argv[-2]
schule = 'Torhorst - Gesamtschule'
schulart = 'mit gymnasialer Oberstufe'
Kurs = 'Leistungskurs'
Fach = 'Mathematik'
Klasse = '12'
Lehrer = 'Herr Herrys'
Art = 'Probe' if probe else 'Test'
identifier = os.path.basename(__file__).removesuffix('.py')
Titel = identifier
datum_delta = 0  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 1  # wie viele verschiedenen Tests sollen erzeugt werden

alle_aufgaben = get_aufgaben(identifier)
alphabet = string.ascii_lowercase
brauch_aufg = []
brauch_teilaufg = []
temp = sys.argv[-1][1:-1].replace(r"'", '').split(', ')
for i in temp:
    if '.' in i:
        brauch_teilaufg.append(i)
    else:
        brauch_aufg.append(i)

# print(brauch_aufg, brauch_teilaufg)
# print(alle_aufgaben)
selected = []
for aufgabe in alle_aufgaben:
    temp_selected = []
    if aufgabe[0] in brauch_aufg:
        temp_selected.append([aufgabe[0], aufgabe[1]])
        temp_teilaufg = []
        for teilaufgabe in aufgabe[3]:
            if teilaufgabe[0] in brauch_teilaufg:
                temp_teilaufg.append(alphabet[int(teilaufgabe[0][-1])-1])
            else:
                continue
        temp_selected.append(temp_teilaufg)
    else:
        continue
    selected.append(temp_selected)


liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']

aufgaben_seite1 = []
module = importlib.import_module(f'Aufgaben.Aufgaben_{identifier}')

for i, aufgabe in enumerate(selected, start=1):
    func = getattr(module, aufgabe[0][1])
    if len(aufgabe[1]) != 0:
        aufgaben_seite1.append(func(i, aufgabe[1]))
    else:
        aufgaben_seite1.append(func(i))

for element in aufgaben_seite1:
    liste_bez.extend(element[5])
    liste_punkte.extend(element[4])

aufgaben_seite2 = []
for element in aufgaben_seite2:
    liste_bez.extend(element[5])
    liste_punkte.extend(element[4])

liste_seiten = [seite(aufgaben_seite1)] # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

angaben = [schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel, datum_delta, liste_bez, liste_punkte, identifier,
           sys.argv[1]]

args = sys.argv[2:-2]
for arg in args:
    key, value = arg.split(':')
    angaben[int(key)] = value if value != '' else angaben[int(key)]

test_erzeugen(liste_seiten, angaben, probe=probe)
