class Voiture:
    count_Voiture = 0

    def __init__(self, marque, modele, couleur, annee, prix):
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.annee = annee
        self.prix = prix
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
        self.prix *= (1 + (pourcent / 100))
        print(f"Prix après promotion : {self.prix}€")
    
    def afficheInfosVoiture(self):
        print(f"Marque : {self.marque}\nModèle : {self.modele}\nCouleur : {self.couleur}\nAnnée de constructon : {self.annee}")
        if self.count_Voiture <= 1:
            print(f"{self.count_Voiture} voiture")
        else:
            print(f"{self.count_Voiture} voitures")
        print(f"Prix TTC : {self.prix}€")


print(f"{Voiture.count_Voiture} voitures")

# instances de classe
voiture1 = Voiture("Peugeot", "206", "Gris métal", 2002, 1500)
voiture1.afficheInfosVoiture()

voiture2 = Voiture("Renault", "Kangoo", "Vert pâle", 2001, 1700)
voiture2.afficheInfosVoiture()

voiture3 = Voiture("Fiat", "Punto", "Noire", 2003, 1650)
voiture3.afficheInfosVoiture()
voiture3.promotion(5)