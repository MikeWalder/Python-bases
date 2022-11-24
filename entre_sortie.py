# Demander le message à afficher
message = input("Veuillez entrer le message à afficher :")

# Affichage du message
print("")
print("--- " + message + " ---")
print("")

# Second affichage
element1 = input("Nom du premier ingrédient :")
element2 = input("Nom du secon ingrédient :")
nbre_convives = input("Nombre de convives :")
print("")
print("Nous avons " + str(nbre_convives) + " invités et les ingrédients suivants seront : " + element1 + ", " + element2)
print("")