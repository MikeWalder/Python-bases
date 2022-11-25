import datetime
destination = 'projets/recette/output_txt/datas.txt'

choice1 = 'Quiche au saumon'
choice2 = 'Moules frites'
choice3 = 'Petits pois carottes'
choice4 = 'Pizza marguarita'

print('Recette de cuisine')
print("")
print('------------')
print('Veuillez choisir une recette')
print('------------')
print('1. Quiche au saumon')
print('2. Moules frites')
print('3. Petits pois carottes')
print('4. Pizza marguarita')
print('------------')

choiceNbre = input('Votre choix : ')

match choiceNbre:
    case "1":
        res = "Votre choix est : " + choice1
    case "2": 
        res = "Votre choix est : " + choice2
    case "3":
        res = "Votre plat est : " + choice3
    case "4":
        res = "Votre choix : " + choice4
    case _:
        res = "Aucun choix entré n'existe ici."

print(res)

x = datetime.datetime.now()

order = res
order += '\nCommande faite le : ' + str(x) + '\n------------\n\n'

# Save the result of the order into a specific file
file_saved = open(destination, "a")
file_saved.write(order)
file_saved.close()