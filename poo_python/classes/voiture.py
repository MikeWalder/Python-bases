class Voiture:
    count_Voiture = 0
    count_voiture_achetee = 0

    def __init__(self, marque, modele, couleur, annee, prix):
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.annee = annee
        self.prix = prix
        self.acheteur = None
        Voiture.count_Voiture += 1

    def get_marque(self): # assesseur / getter
        return self.marque
    
    def get_modele(self):
        return self.modele
    
    def get_couleur(self):
        return self.couleur
    
    def get_annee(self):
        return self.annee
    
    def get_prix(self):
        return self.prix

    def promotion(self, pourcent): # mutateur / setter
        self.prix *= (1 - (pourcent / 100))
        print(f"Prix après promotion de {pourcent}% de la {self.marque} {self.modele} : {self.prix}€")
    
    def afficheInfosVoiture(self):
        print(f"Marque : {self.marque}\nModèle : {self.modele}\nCouleur : {self.couleur}\nAnnée de constructon : {self.annee}")
        if self.count_Voiture <= 1:
            print(f"{self.count_Voiture} voiture")
        else:
            print(f"{self.count_Voiture} voitures")
        print(f"Prix TTC (hors promotion) : {self.prix}€\n")
    
    # Méthode pour ajouter un acheteur à une voiture
    def set_acheteur(self, acheteur):
        self.acheteur = acheteur
        Voiture.count_voiture_achetee += 1


    # Méthode pour vérifier si la voiture a un ou des acheteurs
    def has_acheteur(self):
        if self.acheteur == None:
            print(f"Aucun acheteur pour la {self.marque} {self.modele}")
        else:
            print(f"Il y a au moins 1 acheteur et c'est {self.acheteur.nom}")

    # Méthode pour afficher le nombre total de voitures achetéees
    def totalVoituresAchetees(self):
        print(f"Notre magasin enregistre {Voiture.count_voiture_achetee} ventes au total de la {self.marque} {self.modele}")



