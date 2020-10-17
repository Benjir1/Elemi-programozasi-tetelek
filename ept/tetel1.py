print("Az összegzés tétele\n")
sve = input("Szóközzel szeretnéd elválasztani a tagjaidat, vagy egyesével szeretnéd beírni? (S = Space, E = egyesével): ").lower()

def osszeadas(tomb, elemekmennyisege):
    eredmeny = 0
    for i in range(0, elemekmennyisege):
        eredmeny += tomb[i]
    
    return f"Az eredmény: {eredmeny}"

if sve == "s":
    mt = input("Add meg a tömböd elemeit!: ")
    tomb = mt.split()
    tagok = len(tomb)
    for i in range(0, tagok):
        tomb[i] = int(tomb[i])
    print(osszeadas(tomb, tagok))
if sve == "e":
    tomb = []
    tagok = int(input("Hány eleme lesz a listádnak?: "))
    for i in range(0, tagok):
        elem = input("Add meg az elemedet!: ")
        tomb.append(elem)
    for i in range(0, tagok):
        tomb[i] = int(tomb[i])   
    print(osszeadas(tomb, tagok))
