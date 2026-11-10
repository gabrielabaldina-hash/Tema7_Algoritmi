import time

def iegut_pirmo(dati):
    return dati[0]

dati_10 = list(range(10))
dati_1000000 = list(range(1000000))

sakums = time.time()
iegut_pirmo(dati_10)
beigas = time.time()

print("10 elementu saraksta laiks:", beigas - sakums)

sakums = time.time()
iegut_pirmo(dati_1000000)
beigas = time.time()

print("1 000 000 elementu saraksta laiks:", beigas - sakums)

def viens_cikls(dati):
    kopa = 0
    for x in dati:
        kopa += x
    return kopa

def divi_cikli(dati):
    skaits = 0
    for x in dati:
        for y in dati:
            skaits += 1
    return skaits

for n in (100, 1000):
    dati = list(range(n))

    sakums = time.time()
    viens_cikls(dati)
    beigas = time.time()
    print("Viens cikls, n =", n, "laiks:", beigas - sakums)

    sakums = time.time()
    divi_cikli(dati)
    beigas = time.time()
    print("Divi cikli, n =", n, "laiks:", beigas - sakums)

def pirmais_elements(saraksts):
    return saraksts[0]

def visi_elementi(saraksts):
    for elements in saraksts:
        print(elements)

def elementu_pari(saraksts):
    for x in saraksts:
        for y in saraksts:
            print(x, y)

def pirmais_elements(saraksts):
    soli = 1
    return soli


def visi_elementi(saraksts):
    soli = 0
    for elements in saraksts:
        soli += 1
    return soli


def elementu_pari(saraksts):
    soli = 0
    for x in saraksts:
        for y in saraksts:
            soli += 1
    return soli

for n in (10, 100):
    dati = list(range(n))

    print("Elementu skaits:", n)
    print("O(1):", pirmais_elements(dati))
    print("O(n):", visi_elementi(dati))
    print("O(n²):", elementu_pari(dati))