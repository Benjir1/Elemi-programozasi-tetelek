adattipus = input("Milyen adattípusra szeretnél rákeresni? (S = String, I = Int): ").lower()
sve = input("Szóközzel szeretnéd elválasztani a tagjaidat, vagy egyesével szeretnéd beírni? (S = Space, E = Egyesével): ").lower()

if sve == "s":
    tomb = input("Add meg tömbödet!: ").split()
    if adattipus == "s":
        talalat = False
        keresendo_string = input("Mit szeretnél megkeresni?: ")
        for i in range(0, len(tomb)):
            if tomb[i] == keresendo_string:
                talalat = True
                elemt = tomb[i]
                elemszam = tomb.index(elemt)
                print(f"Az elem száma: {elemszam + 1}")
            else:
                pass
        if talalat == False:
            print("A keresett string nincs a tömbben. Kérem ellenőrizze, hogy helyesen írta-e le.")
    if adattipus == "i":
        talalat = False
        keresendo_int = int(input("Mit szeretnél megkeresni?: "))
        for i in range(0, len(tomb)):
            tomb[i] = int(tomb[i])
        for i in range(0, len(tomb)):
            if tomb[i] == keresendo_int:
                talalat = True
                elemt = tomb[i]
                elemszam = tomb.index(elemt)
                print(f"A keresett szám megtalálva, sorszáma {elemszam + 1}")
            else:
                pass
        if talalat == False:
            print("A keresett int nincs a tömbben. Kérem ellenőrizze, hogy helyesen írta-e le.")
if sve == "e":
    tagok_szama = int(input("Add meg tagjaid számát!: "))
    tomb = []
    for i in range(0, tagok_szama):
        elem = input("Add meg az elemedet!: ")
        tomb.append(elem)

    if adattipus == "s":
        talalat = False
        keresendo_string = input("Mit szeretnél megkeresni?: ")
        for i in range(0, len(tomb)):
            if tomb[i] == keresendo_string:
                talalat = True
                elemt = tomb[i]
                elemszam = tomb.index(elemt)
                print(f"Az elem száma: {elemszam + 1}")
            else:
                pass
        if talalat == False:
            print("A keresett string nincs a tömbben. Kérem ellenőrizze, hogy helyesen írta-e le.")
    if adattipus == "i":
        talalat = False
        keresendo_int = int(input("Mit szeretnél megkeresni?: "))
        for i in range(0, len(tomb)):
            tomb[i] = int(tomb[i])
        for i in range(0, len(tomb)):
            if tomb[i] == keresendo_int:
                talalat = True
                elemt = tomb[i]
                elemszam = tomb.index(elemt)
                print(f"A keresett szám megtalálva, sorszáma {elemszam + 1}")
        if talalat == False:
            print("A keresett int nincs a tömbben. Kérem ellenőrizze, hogy helyesen írta-e le.")
    

