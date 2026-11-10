rezultati = [90, 45]

print("Pirms maiņas:", rezultati)

rezultati[0], rezultati[1] = rezultati[1], rezultati[0]

print("Pēc maiņas:", rezultati)

rezultati[0], rezultati[1] = rezultati[1], rezultati[0]

a = 90
b = 45

print("Pirms maiņas:", a, b)

a, b = b, a

print("Pēc maiņas:", a, b)

rezultati = [45, 12, 89, 23, 67, 5]

for i in range(len(rezultati) - 1):
    print(rezultati[i], rezultati[i + 1])

for i in range(len(rezultati) - 1):
    print(rezultati[i], rezultati[i + 1])

if rezultati[i] > rezultati[i + 1]:
    rezultati[i], rezultati[i + 1] = rezultati[i + 1], rezultati[i]

print("Pēc pirmā gājiena:", rezultati)

rezultati = [45, 12, 89, 23, 67, 5]

for i in range(len(rezultati) - 1):
    if rezultati[i] > rezultati[i + 1]:
        rezultati[i], rezultati[i + 1] = rezultati[i + 1], rezultati[i]

print("Pēc pirmā gājiena:", rezultati)

rezultati = [45, 12, 89, 23, 67, 5]

for i in range(len(rezultati) - 1):
    if rezultati[i] > rezultati[i + 1]:
        rezultati[i], rezultati[i + 1] = rezultati[i + 1], rezultati[i]

print("Pēc pirmā gājiena:", rezultati)

rezultati = [45, 12, 89, 23, 67, 5]

for j in range(len(rezultati)):
    for i in range(len(rezultati) - 1):
        if rezultati[i] > rezultati[i + 1]:
            rezultati[i], rezultati[i + 1] = rezultati[i + 1], rezultati[i]

    print("Pēc gājiena:", rezultati)

print("Sakārtots saraksts:", rezultati)