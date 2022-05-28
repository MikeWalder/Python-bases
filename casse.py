word1 = input("Entrez un mot quelconque : ")
word1_maj = word1.upper() # Appel de méthode
print(word1_maj)

word2 = input("Entrez un mot en majuscules : ")
word2_min = word2.lower() # Méthode pour les comparaisons (recherche de mots)
print(word2_min)

# ----------
# Remplacer des chaînes de caractères
bonjour = "Bonjour"
bonsoir = bonjour.replace("jour", "soir").lower()
print(bonjour + " et " + bonsoir)

# ---------
# Séparer une chaîne de caractères
c1 = "1, oui, 34, nom, 0.6, adresse"
c1_split = c1.split(", ")
print(c1)
print(c1_split)

# Joindre en une chaîne de caractères
c1_new = " - ".join(c1_split)
print(c1_new)

# Remplir de zéros une chaîne de caractères (ex. pour séquences d'images)
c2 = "8"
c2_zfill = c2.zfill(6) # 6 zéros
print(c2 + " et " + c2_zfill)
for i in range(20):
    print(str(i).zfill(4))

digit1 = "50".isdigit() # true

# Renvoyer le nombre d'éléments dans une liste ou une chaîne de caractères
count1 = "Bonjour ici le jour fatidique"
count1_c = count1.count("jour") # retourne 2 donc faux
print(count1_c)
count1_d = count1.count(" jour") # retourne 1 donc bon
print(count1_d)

