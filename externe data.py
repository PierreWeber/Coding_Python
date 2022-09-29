

open("file.xxx", "r") # r pour lecture w pour ecriture , a pour append "rajouter un truc dedans" , r+ for Read and write

file_opening = open("file.xwz", "r") # moyen plus technique pour ouvrir un fichier et travaille dedans
print(file_opening.readable())   # permet de savoir si python peut lire le fichier
print(file_opening.read()) # permet de lire l'ensemble du fichier
print(file_opening.readlines()) # permet de lire toute les lignes une par une  dans un zone de lecture
print(file_opening.readline()[15])  # permet de lire une ligne du fichier  ex: 15
file_opening.close()

nouveau_fichier = open("index.html", "w")  # permet de créer un nouveau fichier
nouveau_fichier.write("<p> This is HTML </p> ") # ecrit seulement cela dans le fichier

nouveau_fichier.close()

import random  #permet de recuperer des fonction et variable d'un module python dediée pour une tache -> voir  https://docs.python.org/3.9/

