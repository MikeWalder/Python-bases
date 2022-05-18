# Méthodes des objets liste
a = [3, 4.6, "Bonjour"]

# Ajouter un élément à la fin de la liste
a.append("Un peu de texte")
print(a)

# Retirer le dernier élément de la liste
a.pop(0)
print(a)

# Longueur de la liste
l = len(a)
print("La liste a une longueur de",l)

# Chercher le dernier élément
print(a[-1])

# Transformer une chaîne de caractères en liste
chaine = "Une:simple:chaine:de:caracteres"
chaine_tab = chaine.split(":")
print(chaine_tab)

# Agrandir une liste par une liste
x = [3, 5.3, 18]
y = [23, 5.98, -5.7]
x.extend(y)
print(x)

# Afficher les 3 premiers éléments d'une liste
print(x[:3])