print("Az eldöntés tétele\n")
sve = input("Szóközzel szeretnéd elválasztani a tagjaidat, vagy egyesével szeretnéd beírni? (S = Space, E = egyesével): ").lower()

def vizsgalat(tomb):
    van = False
    for i in range(0, len(tomb)):
        tomb[i] = int(tomb[i])
    for i in range(0, len(tomb)):
        elem = tomb[i]
        if elem > 0:
            van = True
        else:
            van = False
    if van == True:
        return "A megadott tömbben van pozitív szám!"
    if van == False:
        return "A megadott tömbben nincs pozitív szám!"
if sve == "s":
    tomb = input("Add meg a tömbödet szóközzel elválasztva!: ").split()
    print(vizsgalat(tomb))
if sve == "e":
    tomb = []
    elemszam = int(input("Hány eleme lesz a listádnak?:"))
    for i in range(0, elemszam):
        elem = int(input("Add meg az elemedet!: "))
        tomb.append(elem)
    print(vizsgalat(tomb))