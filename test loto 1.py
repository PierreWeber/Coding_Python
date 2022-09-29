import random  #importe le module statistique simple dit aleatoire
loto_number = [int]  # créer une list de list pour recuperere les numbre aleatoire créer
for i in range (0,4): # creer une boucle de calcul
    number = random.randint(1,49) # ouvre les nombre au module stat
while number in loto_number:
    number = random.randint(1,49)  # verifie que le nombre n'est pas deja pris
    loto_number.append(number) # pioche un nombre
    loto_number.sort() #tri la list de nombre de maniére logique

    print("resultat test loto :")  #affiche le resultat
    print(loto_number)

file_opening = open("D:\Application\Python\Programmation training\Proba Loto Fichier\loto.csv", "r") # ouverture du fichier d'exctraction information

print(file_opening.readable())

file_opening.close()