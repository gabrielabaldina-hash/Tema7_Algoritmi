ienaidnieku_hp = [45, 120, 80, 30, 95, 150, 60, 110, 25, 70]

vajakais = min(ienaidnieku_hp)
stiprakais = max(ienaidnieku_hp)

print(f"Vājākais ienaidnieks: {vajakais}")
print(f"Stiprākais ienaidnieks: {stiprakais}")

mazakais_savs = ienaidnieku_hp[0]

for hp in ienaidnieku_hp:
    if hp < mazakais_savs:
        mazakais_savs = hp

print("Mazākais ar manu ciklu:", mazakais_savs)

dati = list(range(1000000))

def mana_summa(dati):
    kopa = 0
    for skaitlis in dati:
        kopa += skaitlis
    return kopa

def iebuveta_summa(dati):
    return sum(dati)

print("Mana summa:", mana_summa(dati))
print("Iebūvētā summa:", iebuveta_summa(dati))

import time

sakums = time.time()
mana_summa(dati)
beigas = time.time()

laiks_savs = beigas - sakums

sakums = time.time()
iebuveta_summa(dati)
beigas = time.time()

laiks_iebuvets = beigas - sakums

print(f"Pašrakstītā funkcija: {laiks_savs:.4f} sekundes")
print(f"Iebūvētā funkcija: {laiks_iebuvets:.4f} sekundes")

print(f"sum() ir aptuveni {laiks_savs / laiks_iebuvets:.1f} reizes ātrāka")