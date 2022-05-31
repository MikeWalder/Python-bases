def checkNumberInput(variable):
    number = input(f"Entrez un entier {variable} :")
    try:
        # Convert into an integer
        numberIntegered = int(number)
        print("Vous avez entré l'entier",numberIntegered)
        # print(type(number))
        # print(type(numberIntegered))
        return numberIntegered
    except ValueError:
        try:
            # Convert into a float
            numberFloated = float(number)
            print("Le nombre est un flottant et vaut",numberFloated)
            return checkNumberInput(variable)
        except ValueError:
            print("Le nombre est autre chose")
            return checkNumberInput(variable)

def selectNumbers(entry):
    try:
        number = int(input(f"Choisir {entry} : "))
        print(number)
        return number
    except ValueError:
        print("Entrée invalide !")


print("------ CALCULATRICE V.2 ------")
print("Choix de l'opération : ")
print("1 : Addition \n2 : Soustraction \n3 : Multiplication \n4 : Division \n5 : Puissance")
choice = input("Choix : ")

if choice == "1":
    print("Choix : Addition")
    a = checkNumberInput("a")
    b = checkNumberInput("b")
    res = a + b 
    print(f"Résultat de l'addition de {a} par {b} : {res}")
elif choice == "2":
    print("Choix : Soustraction")
    a = checkNumberInput("a")
    b = checkNumberInput("b")
    res = a - b
    print(f"Résultat de la soustraction de {a} par {b} : {res}")
elif choice == "3":
    print("Choix : Multiplication")
    a = checkNumberInput("a")
    b = checkNumberInput("b")
    res = a * b
    print(f"Résultat de la multiplication de {a} par {b} : {res}")
elif choice == "4":
    print("Choix : Division")
    a = checkNumberInput("a")
    b = checkNumberInput("b")
    res = a / b
    print(f"Résultat de la division de {a} par {b} : {res}")
elif choice == "5":
    print("Choix : Puissance (a^b)")
    a = checkNumberInput("a")
    b = checkNumberInput("b")
    res = a ** b
    print(f"Résultat de {a} puissance {b} : {res}")
else:
    print("Mauvais choix")



