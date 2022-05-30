def selectNumbers(entry):
    try:
        number = int(input(f"Choisir {entry} : "))
        print(number)
        return number
    except ValueError:
        print("Entrée invalide !")

print("------ CALCULATRICE V.2 ------")
print("Choix de l'opération : ")
print("1 : Addition \n2 : Soustraction \n3 : Multiplication \n4 : Division")
choice = input("Choix : ")

if choice == "1":
    print("Addition")
    a = selectNumbers("a")
    b = selectNumbers("b")
    res = a + b 
    print(f"Résultat : {res}")
elif choice == "2":
    print("Soustraction")
    a = selectNumbers("a")
    b = selectNumbers("b")
    res = a - b
    print(f"Résultat : {res}")
elif choice == "3":
    print("Multiplication")
    a = selectNumbers("a")
    b = selectNumbers("b")
    res = a * b
    print(f"Résultat : {res}")
elif choice == "4":
    print("Division")
    a = selectNumbers("a")
    b = selectNumbers("b")
    res = a / b
    print(f"Résultat : {res}")
else:
    print("Mauvais choix")

