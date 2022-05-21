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