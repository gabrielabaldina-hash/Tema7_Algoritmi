import random

id_saraksts = []

for i in range(20):
    id_saraksts.append(random.randint(1, 100))

print(id_saraksts)

def linear_search(saraksts, mekletais):
    for i, elements in enumerate(saraksts):
        if elements == mekletais:
            return i
    return -1

    # Pārbaudām ar esošu ID
mekletais = id_saraksts[0]
print("Meklētais ID:", mekletais)
print("Rezultāts:", linear_search(id_saraksts, mekletais))

# Pārbaudām ar neesošu ID
print("Neesošs ID:", linear_search(id_saraksts, 101))

id_saraksts.sort()
print("Sakārtots saraksts:", id_saraksts)

def binary_search(saraksts, mekletais):
    apaksa = 0
    augsa = len(saraksts) - 1

    while apaksa <= augsa:
        vidus = (apaksa + augsa) // 2

        if saraksts[vidus] == mekletais:
            return vidus
        elif saraksts[vidus] < mekletais:
            apaksa = vidus + 1
        else:
            augsa = vidus - 1

    return -1

def linear_search(saraksts, mekletais):
    soli = 0
    for i, elements in enumerate(saraksts):
        soli += 1
        if elements == mekletais:
            return i, soli
    return -1, soli

def binary_search(saraksts, mekletais):
    apaksa = 0
    augsa = len(saraksts) - 1
    soli = 0

    while apaksa <= augsa:
        soli += 1
        vidus = (apaksa + augsa) // 2

        if saraksts[vidus] == mekletais:
            return vidus, soli
        elif saraksts[vidus] < mekletais:
            apaksa = vidus + 1
        else:
            augsa = vidus - 1

    return -1, soli

mekletais = id_saraksts[-1]

print("Lineārā meklēšana:", linear_search(id_saraksts, mekletais))
print("Binārā meklēšana:", binary_search(id_saraksts, mekletais))

for i in range(20):
    id_saraksts.append(random.randint(1, 100))

for i in range(1000):
    id_saraksts.append(random.randint(1, 10000))

id_saraksts.sort()