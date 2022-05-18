# Racine carrée
import math

print("Racine carrée d'un nombre")
a = int(input("Veuillez saisir un nombre positif : "))
try:
    racine_a = round(math.sqrt(a), 3)
    print("La racine de " + str(a) + " est d'environ " + str(racine_a))
except: 
    print("Le nombre entré est incorrect !")

# Factorielle
print("Factorielle d'un nombre")
b = int(input("Entrez un nombre entier positif : "))
try:
    facto_b = math.factorial(b)
    print("La factorielle de " + str(b) + " est égale à " + str(facto_b))
except:
    print("Entrée incorrecte !")