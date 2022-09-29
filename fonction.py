# premiere fonction contruite

x = 10
print ( " hello world ")
print (" voici une petite musique ")
def Affiche_chanson():
    print (" j'aime la musique et elle 'm'aime pas ")
    print (" pourquoi la vie et si dure et faut travailler ")
    print (" gagner gagner gagner de l'argent ")

print (" ma musique est fini ")
Affiche_chanson()
print(" non !! non !! non , elle est encore la :D ")


#faire un fonction plus collaborative

def salut(lang) :
    if lang == 'es' :
        print('Hola !')
    elif lang == 'it' :
        print(" salute !")
    elif lang == 'us' :
        print("Hi ! ")
    elif lang == 'uk' :
        print("hello ! ")
    else :
        print(" bonjour !! ")


lang = input (" quelles langues ? es | it | us | uk ")
salut(lang)
