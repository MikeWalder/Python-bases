# Notion d'objets en Python

class Etudiant:

    def __init__(self, nom, age, city = "Lyon"):
        self.nom = nom
        self.age = age
        self.city = city

    def presentationIdentite(self):
        print("Nom : " + self.nom +"\nAge : " + str(self.age) + "\nVille : " + self.city)

    @classmethod
    def implementation(cls):
        return "This is a class method"

        

mike = Etudiant("Mike", 23, "Chalençon")
mike.presentationIdentite()

# Modifier un attribut de la classe : 
mike.age = 32
mike.city = "Strasbourg"
print(mike.nom + " a maintenant " + str(mike.age) + " ans\nIl vit à " + mike.city)

# Verify the type of a variable
position = 1, 4, -5
print("The type of position is : ",type(position))
coord = {
    "age" : 23, 
    "job" : "student",
    "birthday" : "12/05/2002"
    }
print("The type of coord is :",type(coord))

ret = Etudiant.implementation()
print(ret)