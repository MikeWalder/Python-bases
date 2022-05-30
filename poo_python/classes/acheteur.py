class Acheteur:
    count_acheteur = 0

    def __init__(self, nom, prenom, pays, budget):
        self.nom = nom
        self.prenom = prenom
        self.pays = pays
        self.budget = budget
        Acheteur.count_acheteur += 1

    def get_nom(self):
        return self.nom
    
    def get_prenom(self):
        return self.prenom
    
    def get_pays(self):
        return self.pays

    def get_budget(self):
        return self.budget    

    def afficherNombreAcheteurs(self): # affichage du nombre d'acheteurs
        if(self.count_acheteur <= 1):
            print(f"{self.count_acheteur} acheteur")
        else:
            print(f"{self.count_acheteur} acheteurs")