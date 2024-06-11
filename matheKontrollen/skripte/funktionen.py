import random
import time

import numpy as np
from sympy import *
from pylatex import Document, Package


# Timer Funktion
def timer(func):
    """
    Timer-Dekorator zur Messung der Ausführungszeit einer Funktion.
    """
    def wrapper(*args, **kwargs):  # Erklärung eines Dekorators -> https://t1p.de/lqn4d
        start_time = time.perf_counter()  # Zeit vorm ausfuhren nehmen
        result = func(*args, **kwargs)  # Aufruf der eigentlichen Funktion mit ihren Argumenten
        end_time = time.perf_counter()  # Zeit nachm ausführen
        execution_time = end_time - start_time  # Vergangene Zeit berechnen

        print(f'\033[38;2;0;220;120m\033[1m"{func.__name__}" wurde in {round(execution_time, 3)} Sekunden ausgeführt\033[0m')
        return result
    return wrapper


def packages(doc: Document):
    """
    Fügt unsere benutzten Pakete an jeweiliges Dokument an.
    """
    packages_lst = ['amsfonts', 'bm']

    for package in packages_lst:
        doc.packages.append(Package(package))


# Funktionen zur Darstellung von Zahlen
def zzahl(p, q):
    return random.choice([-1, 1]) * random.randint(p, q)

def nzahl(p, q):
    return random.randint(p, q)

def vorz(k):
    if k < 0:
        return '-'
    else:
        return '+'

def vorz_aussen(k, Null=False):
    if k < 0:
        return '-'
    else:
        return ''

# Vorzeichen und Faktoren in Gleichungen oder Vektoren
def vorz_fakt(k):
    if k < 0:
        return -1
    else:
        return 1

def vorz_str(k, null=False):
    if k == 0:
        return '+0' if null else ''  # Falls auch Nullen angezeigt werden sollen
    if k%1 == 0:
        k = int(k)
    if k < 0:
        return latex(k)
    else:
        return f'+{latex(k)}'


# Darstellung der Faktoren bzw. Vorzeichen neu

def vorz_v_innen(k,v, null=False):
    if k == 0:
        return '0' if null else ''  # Falls auch Nullen angezeigt werden sollen
    if k == -1:
        return '-' + v
    if k == 1:
        return '+' + v
    if k%1 == 0:
        k = int(k)
    if k < 0:
        return latex(k) + v
    else:
        return f'+{latex(k)}' + v

def vorz_v_aussen(k,v, null=False):
    if k == 0:
        return '0' if null else ''  # Falls auch Nullen angezeigt werden sollen
    if k == -1:
        return '-' + v
    if k == 1:
        return v
    if k%1 == 0:
        k = int(k)
    return latex(k) + v

def gzahl(k):
    if k % 1 == 0:
        return latex(int(k))
    else:
        return latex(k)

def gzahl_klammer(k):
    if k%1 == 0:
        k = int(k)
    if k < 0:
        if k % 1 == 0:
            return f'({latex(k)})'
        else:
            return r'\Big(' + latex(k) + r'\Big)'
    else:
        return latex(k)

# Funktionen zur Optimierung von Ergebnissen mit True and False als Ausgabe

def vektor_rational(vec,p,q=1000):
    vec_p = [element*p for element in vec]
    print(vec_p)
    k = 0
    i = 0
    for element in vec_p:
        if element % 1 == 0:
            k += 1
        if int(k/q) == 0:
            i += 1
    if k == 3 and i == 3:
        return True
    else:
        return False

# Funktionen zur linearen Algebra

def punkt_vektor(p):
    return np.array([zzahl(1,p), zzahl(1,p), zzahl(1,p)])

def faktorliste(n, p=1,q=10):
    return [zzahl(p, q) for _ in range(n)]  # mit dem _ kann man die Variable weglassen

def vektor_runden(vec,p):
    return [N(elements,p) for elements in vec]
# Berechnung für die Aufgaben
def vektor_ganzzahl(vec):
    return np.array([int(element) if element % 1 == 0 else element for element in vec])

def vektor_kuerzen(vec, p = 50):
    faktor = [x + 1 for x in range(p)]
    list = np.array(vec)
    i = 0
    for element in vec:
        k = 0
        if list[i] % 1 == 0:
            i += 1
        else:
            while (list[i] * faktor[k]) % 1 != 0 and k+1 < p:
                k += 1
            list = list * faktor[k]
            i += 1
    # print('erweitert: ' + str(list))
    teiler = [x + 1 for x in range(int(max(list)/2),-1,-1)]
    for zahl in teiler:
        treffer = [1 for x in list if x % zahl == 0]
        if sum(treffer) == len(vec):
            list = list / zahl
    # print('gekürzt: ' + str(list))
    list = np.array([int(element) if element % 1 == 0 else element for element in list])
    return np.array(list)

def vektor_kollinear(vec1, vec2):
    i = 0
    lsg = []
    for element in vec1:
        lsg.append(element / vec2[i])
        i += 1
    # print(lsg)
    for element in lsg:
        # print(element / lsg[0])
        if element / lsg[0] != 1:
            return False
    return True

def vektor_max(vec, p):
    vec_p = [element / p for element in vec]
    k = 0
    for element in vec_p:
        if element % 1 == 0:
            k += 1
    if k == 3:
        return True
    else:
        return False

def vektor_vergleich(vec1, vec2):
    if len(vec1) != len(vec2):
        return print('Vektoren verschieden lang.')
    i = 0
    for element in vec1:
        if vec1[i] == vec2[i]:
            i += 1
        else:
            return False
    return True

# Wahrscheinlichkeitsrechnung

def darstellung_mengen(lsg_menge):
    # korrekte Darstellung der Lösungsmenge
    lsg = '{ '
    m = 1
    for tubel in lsg_menge:
        n = 1
        lsg = lsg + '( '
        for element in tubel:
            lsg = lsg + str(element)
            if n < len(tubel):
                lsg = lsg + ', '
            n += 1
        lsg = lsg + ')'
        if m < len(lsg_menge):
            lsg = lsg + '; '
        m += 1
    lsg = lsg + ' }'
    return lsg

def ergebnisraum_zmZ(anzahl_ziehen, farbe1='weiß', farbe2='schwarz'):
    omega = [[farbe1 for element in range(anzahl_ziehen)]]
    for anzahl in omega:
        i = 0
        for stelle in anzahl:
            tubel = anzahl.copy()
            tubel[i] = farbe2
            for element in omega:
                if tubel not in omega:
                    omega.append(tubel)
            i += 1
    return omega

# Funktionen zur Analysis

def faktorliste(p, q, n):
    return [zzahl(p, q) for _ in range(n)]  # mit dem _ kann man die Variable weglassen

def exponenten(n):
    menge = set()  # ich habe hier eine Menge verwendet, weil diese keine gleichen Elemente enthält
    while len(menge) < n:
        menge.add(nzahl(2, 6 + n))
    return menge

def funktion(p):  # erzeugt eine Funktion und deren Ableitungen mit p Summanden und maximal p-Grades
    fkt = random.choice([zzahl(1, 10), 0])
    koeffizienten = faktorliste(1, 15, p)
    potenzen = exponenten(p)

    for koeffizient in koeffizienten:
        fkt = koeffizient * (x ** potenzen.pop()) + fkt
        fkt = collect(fkt, x)
    fkt_abl_1 = collect(expand(diff(fkt, x)), x)
    fkt_abl_2 = collect(expand(diff(fkt, x, 2)), x)

    return fkt, fkt_abl_1, fkt_abl_2

# noch zu programmieren
def ergebnisraum_zoZ(az, anz_1, anz_2, farbe1='weiß', farbe2='schwarz'):
    anz_ges = anz_1 + anz_2
    if az > anz_ges:
        az = anz_ges
    omega1 = [[farbe1 for element in range(az)]]
    if az > anz_1:
        omega = []
    else:
        omega = [[farbe1 for element in range(az)]]
    for anzahl in omega1:
        i = 0
        for stelle in anzahl:
            tubel = anzahl.copy()
            tubel[i] = farbe2
            for element in omega1:
                if tubel not in omega1:
                    omega1.append(tubel)
                    if tubel.count(farbe2) <= anz_2 and tubel.count(farbe1) <= anz_1:
                        omega.append(tubel)
            i += 1
    return omega
