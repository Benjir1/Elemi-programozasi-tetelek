print("Egyszerű cserés rendezés tétele\n")
sve = input("Szóközzel szeretnéd elválasztani a tagjaidat, vagy egyesével szeretnéd beírni? (S = Space, E = Egyesével): ").lower()
nvc = input("Növekvő vagy csökkenő sorrendbe szeretnéd rendezni a tömb tagjait? (N = Növekvő, C = Csökkenő): ").lower()

def novekvorendezes(tomb, hatvany):
    doit = True
    hatvany += 1
    hatar = 10 ** hatvany
    if hatvany == 0:
        doit = False
    end = False
    megoldas = []
    i = 0
    while end == False:
        if i == hatar:
            end = True
            break
        if i in tomb:
            megoldas.append(i)
            i += 1
        if i not in tomb:
            i += 1
    if doit == True:
        return f"A pozitív számok növekvő sorrendben: {megoldas}"
    elif doit == False:
        return "Sajnos nem helyes hatványt adtál meg. Kérlek próbáld újra!"

def csokkenorendezes(tomb, hatvany):
    doit = True
    hatvany += 1
    hatar = 10 ** hatvany
    if hatvany == 0:
        doit = False
    end = False
    megoldas = []
    i = 0
    while end == False:
        if i == hatar:
            end = True
            break
        if i in tomb:
            megoldas.append(i)
            i += 1
        if i not in tomb:
            i += 1
    if doit == True:
        return f"A pozitív számok növekvő sorrendben: {megoldas[::-1]}"
    elif doit == False:
        return "Sajnos nem helyes hatványt adtál meg. Kérlek próbáld újra!"

if sve == "s":
    if nvc == "n":
        hatvany = int(input("A legnagyobb szám a tíz melyik hatványához van legközelebb?: "))
        tomb = input("Add meg az elemeket!: ").split()
        for i in range(0, len(tomb)):
            tomb[i] = int(tomb[i])
        print(novekvorendezes(tomb, hatvany))
    if nvc == "c":
        hatvany = int(input("A legnagyobb szám a tíz melyik hatványához van legközelebb?: "))
        tomb = input("Add meg az elemeket!: ").split()
        for i in range(0, len(tomb)):
            tomb[i] = int(tomb[i])
        print(csokkenorendezes(tomb, hatvany))

if sve == "e":
    if nvc == "n":
        hatvany = int(input("A legnagyobb szám a tíz hányadik hatványához van legközelebb?: "))
        tomb = []
        tagok = int(input("Hány tagja lesz a listádnak?: "))
        for i in range(0, tagok):
            elem = int(input("Add meg az elemedet!: "))    
            tomb.append(elem)
        print(novekvorendezes(tomb, hatvany))
    if nvc == "c":
        hatvany = int(input("A legnagyobb szám a tíz hányadik hatványához van legközelebb?: "))
        tomb = []
        tagok = int(input("Hány tagja lesz a listádnak?: "))
        for i in range(0, tagok):
            elem = int(input("Add meg az elemedet!: "))    
            tomb.append(elem)
        print(csokkenorendezes(tomb, hatvany))
        