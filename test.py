import requests

print("Hello my name is Mike")

prixEuros = 56 * 6.55957

print(prixEuros)

# Variables :

name='Henry'
city = 'Selestat'
country = 'France'
cp = '67600'
print('Hello my name is ' + name + ', I live in ' + country + ' near ' + city + ' (' + cp +')')


# Les listes (équivalent à un tableau) :
langages_prog = ['HTML', 'CSS', 'PHP', 'SQL', 'JavaScript', 'Java', 'Python']
print(langages_prog[2] + ' est un langage côté back-end')
print(langages_prog[0] + ' est un langage côté front-end')
print(len(langages_prog))


# Tuple (liste immuable) :
reseau_social = ('Facebook', 'Instagram', 'Twitter', 'Linkedin')
print(reseau_social[0] + ' et ' + reseau_social[3] + ' sont des réseaux sociaux à usage orienté professionnellement')


# Dictionnaire (équivalent sur PHP à un tableau associatif) :
infos_perso = {
    "nom" : "Mike",
    "age" : "32",
    "situation" : "en couple",
    "anniversaire" : "19/09/1988",
}
del infos_perso["situation"]
print(infos_perso["nom"] + ' a ' + infos_perso["age"] + ' ans et est né le ' + infos_perso["anniversaire"])

# -------------------------
# LES CONDITIONS :
# -------------------------
# IF ... ELSE
soleil = True
chaud = False
pluie = False
if soleil and chaud :
    print("Aujourd'hui il fait assez beau et chaud")
elif soleil and not chaud:
    print("Il y a du soleil mais il ne fait pas chaud")
elif chaud and pluie :
    print("Aujour'hui il pleut, même s'il fait chaud")
else :
    print("Autre")

# -------------------------
# LES BOUCLES
# -------------------------
# BOUCLE FOR

liste_villes = ["Nancy", "Lyon", "Grenoble", "Nice", "Bordeaux", "Brest", "Dreux"]
for ville in liste_villes:
    print("Cette ville s'appelle " + ville)
for y in range(4):
    print("Ceci est la ligne numéro " + str(y))

# -------------------------
# BOUCLE WHILE
# -------------------------
ligne_min = 3
ligne_max = 10
while ligne_min <= ligne_max:
    print("Nous avons la ligne au stade numéro " + str(ligne_min))
    ligne_min += 1

# --------------------------
# LES FONCTIONS
# --------------------------
def addition_nombres(a, b, c):
    return a + b + c

def francs_to_euros(a):
    return round(a / 6.55957, 2)

res = addition_nombres(5, 8, 47.5)
print("Le résultat de l'addition est : " + str(res))

prix_francs = 250
converted = francs_to_euros(prix_francs)
print(str(prix_francs) + "F valent : " + str(converted) + "€")

# LES PACKAGES
# pip = gestionnaire de packages
# pip freeze : voir les packages déjà installés
# pip install <nom-du-package> 
