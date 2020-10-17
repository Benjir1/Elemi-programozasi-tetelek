print("A kiválasztás és lineáris keresés tétele\n")
sve = input("Szóközzel szeretnéd elválasztani a tagjaidat, vagy egyesével szeretnéd beírni? (S = Space, E = egyesével): ").lower()

def hasonlitas(tomb,tizedesjegy):
    hatar = 10 ** tizedesjegy
    eps = 1
    found = False
    while found == False:
        if eps in tomb:
            sorszam = tomb.index(eps)
            return f"A legkisebb pozitív szám a listában:{eps}, sorszáma: {sorszam + 1}"
            found = True
        
        if eps > hatar:
            return "Nem található pozitív szám a listádban!"

        else:
            eps += 1


if sve == "s":
    tizedesjegy = int(input("A legnagyobb számod a tíz hányadik hatványához van közelebb?: "))
    tomb = input("Add meg az elemeket!: ").strip().split()
    tagok = len(tomb)
    for i in range(0, tagok):
        tomb[i] = int(tomb[i])
    egyesevel = False
    print(hasonlitas(tomb, tizedesjegy))

if sve == "e":
    tizedesjegy = int(input("A legnagyobb számod a tíz hányadik hatványához van legközelebb?: "))
    tomb = []
    tagok = int(input("Hány tagot szeretnél megadni?: "))
    for i in range(0, tagok):
        elem = int(input("Add meg az elemedet!: "))
        tomb.append(elem)
    egyesevel = True
    print(hasonlitas(tomb, tizedesjegy))