# importation de la classe Voiture
from classes.voiture import Voiture
from classes.acheteur import Acheteur

acheteur1 = Acheteur("Jim", "Bolowitz", "France", 28000)
acheteur2 = Acheteur("Michael", "Dunkritz", "USA", 12500)
acheteur3 = Acheteur("Pamela", "Bornetti", "Italy", 20800)

print(f"{Voiture.count_Voiture} voitures")

# instances de classe
voiture1 = Voiture("Peugeot", "206", "Gris métal", 2002, 1500)
voiture1.afficheInfosVoiture()
voiture1.set_acheteur(acheteur2)
voiture1.set_acheteur(acheteur3)
voiture1.has_acheteur()

voiture2 = Voiture("Renault", "Kangoo", "Vert pâle", 2001, 1700)
voiture2.afficheInfosVoiture()
voiture2.has_acheteur()

voiture3 = Voiture("Fiat", "Punto", "Noire", 2003, 1650)
voiture3.afficheInfosVoiture()
voiture3.promotion(5)

print(f"{Acheteur.count_acheteur} acheteurs")

voiture1.totalVoituresAchetees()