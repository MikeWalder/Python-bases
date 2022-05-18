# Recherche du plus petit élément d'un tableau quelconque

def plus_petit_element(tab):
    valeur_courante = tab[0]
    index_plus_petit_element = 0

    for i in range(1, len(tab)):
        if(tab[i] < valeur_courante):
            valeur_courante = tab[i]
            index_plus_petit_element = i
        
    return index_plus_petit_element


# Définition des valeurs dans un tableau
tab1 = [8, 5, 45, 12, 0.5, 14, -4, 120, 420, -3.48]
print("Valeurs du tableau : " + str(tab1))

# Appel de la fonction de tri du tableau
index_plus_petit_element = plus_petit_element(tab1)

# Affichage des résultats
print("L'index du plus petit élément de notre tableau est : " + str(index_plus_petit_element))
print("La valeur du plus petit élément du tableau est : " + str(tab1[index_plus_petit_element]))


# ----------------------------------------
# Trier une liste quelconque avec sorted
tab1_tri = sorted(tab1)
print(tab1_tri)

# Algo de recherche dichotomique à partir d'une lsite triée
def recherche_dichotomique(tab, elem):
    a = 0
    b = len(tab1_tri) - 1
    milieu = (a + b) // 2 # Division entière : //

    while a < b:
        if tab[milieu] == elem:
            return milieu # Récupération au final de l'indice
        elif tab[milieu] > elem:
            b = milieu - 1
        else:
            a = milieu + 1

        milieu = (a + b) // 2
    
    return a # Récursivité de la fonction tant que tab[milieu] != elem

# Test de la fonction :
nombre = input("Entrez le nombre à chercher dans le tableau : ")
indice_nombre = recherche_dichotomique(tab1_tri, int(nombre))
print("Le nombre " + str(nombre) + " est présent dans le tableau à l'indice " + str(indice_nombre))






