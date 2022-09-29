# collecte un nombre
nombre = input (" donne moi un nombre : ")
valeur = 100
print(type(nombre))
nombre = float(nombre)
print(type(nombre))

# affiche le nombre "Sequential"
print(nombre)

# conditionne le nombre  "Conditionnal"

if nombre > valeur :
    print( "nombre superieur a 100" )
if nombre < valeur :
    print( "nombre inferieur a 100")

print("all good!")

age = input ("Quelle Age as tu ? ")
age = float(age)
int = 18
if age >= int :
    print("vous etes majeur")
    print("ca sent bon !!")
    print("vous avez quelle langage ?")
    langage = input ("-")
    if langage == "python":
        print("vous pouvez entrer")
        print("Mais attention aux abus")
        print("signez la charte!! mdr")
    else :
        print("Accée refusé!!")
        print("faut parler python !! idiot !! ")

elif age < int :
    print("vous etes mineur")
    print("les mineurs ne peuvent pas entrer car c'est la loi :D  ")

print("script over")