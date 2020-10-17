import os

while True:

    konzol = input(">>> ")

    if konzol == "ept":
        tetel = int(input("Hányadik tételt szeretnéd megnézni?: "))

        if tetel == 1:
            os.system('python ept/tetel1.py')

        if tetel == 2:
            os.system('python ept/tetel2.py')

        if tetel == 3 or tetel == 4:
            os.system('python ept/tetel3.py')

        if tetel == 5:
            os.system('python ept/tetel5.py')
            
        if tetel == 6:
            os.system('python ept/tetel6.py')

        if tetel == 7:
            os.system('python ept/tetel7.py')

    if konzol == "help":
        print("Az ept parancs segítségével nézheted meg az elemi programozási tételeket.")