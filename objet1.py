# Notion d'objets en Python

class Etudiant:
    nom = "Mike"
    age = 32
    city = "Lyon"

    def presentationIdentite(self):
        text = print("Nom : " + self.nom +"\n Age : " + self.age + "\nVille : " + self.city)
        return text

Etudiant.presentationIdentite()