from Aufgaben.Aufgaben_Analysis import *
from Aufgaben.Aufgaben_Algebra import *
from Aufgaben.Aufgaben_Wahrscheinlichkeitsrechnung import *
from skripte.erstellen import *

# Angaben für den Test im pdf-Dokument
schule = 'Torhorst - Gesamtschule'
schulart = 'mit gymnasialer Oberstufe'
Kurs = 'Leistungskurs'
Fach = 'Mathematik'
Klasse = '12'
Lehrer = 'Herr Herrys'
Art = 'Test 3 (2. Sem.)'
Titel = 'Kurvendiskusssion einer Parameterfunktion'
datum_delta = 0  # in Tagen (0 ist Heute und 1 ist Morgen, 2 Übermorgen, usw.)
anzahl = 1 # wie viele verschiedenen Tests sollen erzeugt werden
probe = True    # True: Probe 01, 02 usw. oder Gr. A, Gr. B usw

liste_punkte = ['Punkte']
liste_bez = ['Aufgabe']

for i in range(anzahl):
    aufgaben_seite1 = [kurvendiskussion_exponentialfkt_01(1, ['a', 'b', 'c', 'd', 'e', 'f', 'h'])]
    for element in aufgaben_seite1:
        liste_bez.extend(element[5])
        liste_punkte.extend(element[4])

    aufgaben_seite2 = []
    for element in aufgaben_seite2:
        liste_bez.extend(element[5])
        liste_punkte.extend(element[4])

    liste_seiten = [seite(aufgaben_seite1)] # z.b. liste_seiten = [seite(aufgaben_seite1), seite(aufgaben_seite2)]

    angaben = [schule, schulart, Kurs, Fach, Klasse, Lehrer, Art, Titel, datum_delta, liste_bez, liste_punkte]

    import sys
    probe = True if sys.argv[-1] == 'True' else False
    identifier = os.path.basename(__file__).removesuffix('.py')
    angaben.append(True) if len(sys.argv) == 3 else angaben.append(False)
    angaben.append(identifier)
    angaben.append(sys.argv[1])
    if len(sys.argv) > 3:
        args = sys.argv[2:-1]
        for arg in args:
            key, value = arg.split(':')
            angaben[int(key)] = value if value != '' else angaben[int(key)]

    test_erzeugen(liste_seiten, angaben, i, probe)

