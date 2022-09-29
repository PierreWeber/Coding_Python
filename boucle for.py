
for letter in "Welcome to the paradise of Python!!!":
    print (letter)

for index in range(5):
    if index == 0:
        print("first")
    else:
        print("not first")

######################################list

maliste = ["bananes", "fraises", "mangues","pommes", "poires" ]
print(maliste)

if "banane" in maliste:   # verifie si la banane est dans la liste
    print("oui")
else:
    print("non")

for x in maliste:
    print(x)

print(len(maliste))  #calcule le nombre d'element dans la liste et l affiche

maliste.append("citron")  # rajoute un  element dans ma liste
print(maliste)

maliste1 = ["oranges", "clementines", "pasteques", "durian", "cerise"]

ma_nouvelle_liste = maliste + maliste1
print(ma_nouvelle_liste)

maliste.sort()  # tri la liste selon un ordre
print(ma_nouvelle_liste)

malistedenombre = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fibo = [a*a for a in malistedenombre]

print(malistedenombre)
print(fibo)
############################################################translate voyelle
def trans(phrase):
    trans = ""
    for lettre in phrase:
        if lettre in "AEIOUYaeiouy":
            trans = trans + "01"
        else:
            trans = trans + lettre
    return trans

print(trans(input(" ecrit des mots pour trans : ")))
#######################################################While loop condition boolean
i = 0
while i <= 10:
    print(i)
    i += 1
print("done with I")