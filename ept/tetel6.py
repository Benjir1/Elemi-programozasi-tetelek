print("A maximumkiválasztás tétele\n")

sve = input("Szóközzel szeretnéd elválasztani a tagjaidat, vagy egyesével szeretnéd beírni? (S = Space, E = egyesével): ").lower()

def kivalasztas(tomb,hatvany):
  index = 0
  i = 0
  legnagyobb = 0
  hatvany += 1
  hatar = 10 ** hatvany
  while i != hatar:
    if i in tomb:
      if i > legnagyobb:
        legnagyobb = i
        index = tomb.index(legnagyobb)
      else:
        i += 1
    if i not in tomb:
      i += 1
  if legnagyobb == 0:
    return "A tömbödben nincsen pozitív szám"
  if legnagyobb > 0:
    return f"A legnagyobb szám a tömbödben: {legnagyobb}, sorszáma: {index + 1}"

if sve == "s":
  hatvany = int(input("A legnagyobb szám a tíz melyik hatványához van legközelebb?: "))
  tomb = input("Add meg az elemeidet!: ").split()
  for i in range(0, len(tomb)):
    tomb[i] = int(tomb[i])
  print(kivalasztas(tomb, hatvany))

if sve == "e":
  tomb = []
  hatvany = int(input("A legnagyobb szám a tíz melyik hatványához van legközelebb?: "))
  tagok = int(input("Hány tagja lesz a tömbödnek?: "))
  for i in range(0, tagok):
    elem = int(input("Add meg az elemedet!: "))
    tomb.append(elem)
  print(kivalasztas(tomb, hatvany))