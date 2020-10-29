#Galgje
#Opdracht: Maak een programma om galgje te spelen, laat speler 1 een woord invoeren, laat daarna speler 2 een letter raden
#als het letter in het word zit moet de letter op de goede plaats komen, speler 2 mag maar 9 x raden
poging = 9
letters = 0
woord = input("Kies een woord:  ")
woord = woord.lower()

text = woord
woordarray = []
goedgeraden = []
foutgeraden = []
streepwoord = []    
for char in range(len(woord)):
    streepwoord.append("_")

for char in woord:
    woordarray.append(char)
    letters += 1
print("\n \n \n \n \n \n \n \n")
print("tot nu toe geraden: " + "".join(streepwoord))
print("het woord is " + str(letters) + " lang ")
if poging == 0:
    print("je hebt geen pogingen meer")
while poging > 0:
    print("\n \n")
    if woord == "".join(streepwoord):
        print(" \n \n je hebt het goed geraden \n het woord was:  " + woord)
        poging = 0
        break
    print(str(poging) + " pogingen resterend")
    print("".join(streepwoord))
    print("fout geraden: " + "".join(foutgeraden))
    inp = input("voer je keuze in: ").lower()
    if len(inp) > 1:
        print(" \n \n \n dat is meer dan 1 letter")
    else:
        poging = poging - 1
        if inp in woord:
            goedgeraden.append(inp)
            for i in range(0, len(woordarray)):
                if woordarray[i] == inp:
                    streepwoord[i] = inp
        else:
            foutgeraden.append(inp)
if poging == 0:
    print("\n\n\nje hebt geen pogingen meer\n\n")