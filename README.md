# Galējais 2. tēmas darbs



## Algoritms un kā tas strādā
Dators katru reizi min skaitli intervāala vidū. Spēlētājs pasaka, vai viņa skaitlis ir lielāks, mazāks vai pareizs. Pēc katras atbildes dators sadala intervālu uz pusi, līdz beidzot uzmin pareizo skaitli.

Programma arī skaita mēģinājumus un pamana, ja spēlētājs sniedz nepareizas atbildes.


## Algoritma efektivitāte
Binārās meklēšanas laika sarežģītība ir O(log n), jo katrā solī meklēšanas intervāls tiek samazināts gandrīz uz pusi.

- 100 skaitļu intervālā nepieciešami ne vairāk kā 7 minējumi.
- 1000 skaitļu intervālā nepieciešami ne vairāk kā 10 minējumi.

Salīdzinājumam, lineārās meklēšanas sarežģītība ir O(n), un 100 skaitļu intervālā sliktākajā gadījumā būtu nepieciešami 100 minējumi.


## Testu piemēri
Es spēli pārbaudīju ar šādiem skaitļiem:

73 - nepieciešami 6 minējumi
15 - nepieciešami 5 minējumi
100 - nepieciešami 7 minējumi

Beigās pārbaudīju vai viņš saprastu, ja es turpinu dot neīstas atbildes un jā viņš saprata.


## Kā palaiž?
Atver PowerShell projekta mapē un ievadi komandu:
    python 76.py



