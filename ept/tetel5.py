doit = True
print("A megszámolás tétele\n")
sve = input("Szóközzel szeretnéd elválasztani a tagjaidat, vagy egyesével szeretnéd beírni? (S = Space, E = egyesével): ").lower()

def megszamolas(tomb, hatvany):
  talalat = 0
  i = 0
  hatar = 10 ** hatvany
  while i != hatar:
    if i in tomb:
      talalat += 1
      i += 1
    else:
      i += 1
      pass
  if talalat == 0:
    return "Nincs pozitív szám a tömbödben!"
  if talalat > 0:
    return f"A pozitív számok mennyisége a tömbödben: {talalat}"

if sve == "s":
  hatvany = int(input("A tíz hányadik hatványához van legközelebb a legnagyobb számod?: "))
  hatvany += 1
  if hatvany == 0:
    doit = False
  tomb = input("Add meg a tömbödet!: ").split()
  for i in range(0, len(tomb)):
    tomb[i] = int(tomb[i])
if sve == "e":
  hatvany = int(input("A tíz hányadik hatványához van legközelebb a legnagyobb számod?: "))
  hatvany += 1
  if hatvany == 0:
    doit = False
  tomb = []
  tagok = int(input("Hány tagja lesz a listádnak?: "))
  for i in range(0, tagok):
    elem = int(input("Add meg az elemedet"))
    tomb.append(elem)

if doit == True:
  print(megszamolas(tomb, hatvany))
if doit == False:
  print("Sajnos nem helyes hatványt adtál meg. Kérlek próbáld újra!")





