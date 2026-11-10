apaksa = 1
augsa = 100

minejums = (apaksa + augsa) // 2

print(f"Datora pirmais minējums: {minejums}")

apaksa = 1
augsa = 100
minejumi = 0

while True:
    if apaksa > augsa:
        print("Tas nesakrīt, esi kļūdijies.")
        break

    minejums = (apaksa + augsa) // 2
    minejumi += 1

    print(f"Vai tavs skaitlis ir {minejums}?")
    atbilde = input("Ieraksti: lielaks, mazaks vai pareizi: ")

    if atbilde == "lielaks":
        apaksa = minejums + 1

    elif atbilde == "mazaks":
        augsa = minejums - 1

    elif atbilde == "pareizi":
        print(f"Pareizi uzminēju. Vajadzēja tikai {minejumi} mēģinājumus.")
        break

    else:
        print("Nesapratu tavu atbildi, mēģini vēlreiz.")