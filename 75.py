def bubble_sort(saraksts):
    for j in range(len(saraksts)):
        for i in range(len(saraksts) - 1):
            if saraksts[i] > saraksts[i + 1]:
                saraksts[i], saraksts[i + 1] = saraksts[i + 1], saraksts[i]
    return saraksts

dati = list(range(3000, 0, -1))

dati_bubble = dati.copy()
dati_sorted = dati.copy()

sakartots_bubble = bubble_sort(dati_bubble)
sakartots_sorted = sorted(dati_sorted)

print("Bubble sort:", sakartots_bubble[:10])
print("Sorted:", sakartots_sorted[:10])

import time

sakums = time.time()
bubble_sort(dati_bubble)
beigas = time.time()

laiks_bubble = beigas - sakums

sakums = time.time()
sorted(dati_sorted)
beigas = time.time()

laiks_sorted = beigas - sakums

print(f"Bubble sort laiks: {laiks_bubble:.4f} sekundes")
print(f"sorted() laiks: {laiks_sorted:.4f} sekundes")

print(f"sorted() ir aptuveni {laiks_bubble / laiks_sorted:.1f} reizes ātrāks")

dati_saraksts = list(range(200000))
dati_kopa = set(dati_saraksts)

mekletais = 199999

sakums = time.time()
atrasts_saraksta = mekletais in dati_saraksts
laiks_saraksts = time.time() - sakums

sakums = time.time()
atrasts_kopa = mekletais in dati_kopa
laiks_kopa = time.time() - sakums

print(f"Sarakstā: {atrasts_saraksta} ({laiks_saraksts:.6f} s)")
print(f"Kopā: {atrasts_kopa} ({laiks_kopa:.6f} s)")

print(f"Kopa ir aptuveni {laiks_saraksts / laiks_kopa:.0f} reizes ātrāka")

speletaji = {"Anna", "Roberts", "Anna", "Laura"}

print(speletaji)

speletaji = set()

speletaji.add("Anna")
speletaji.add("Roberts")
speletaji.add("Laura")

print(speletaji)

vardnica = {i: i for i in range(200000)}

sakums = time.time()
atrasts_vardnica = 199999 in vardnica
laiks_vardnica = time.time() - sakums

print(f"Vārdnīcā: {atrasts_vardnica} ({laiks_vardnica:.6f} s)")