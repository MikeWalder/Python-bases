import requests
import csv
from sumfunction import simpleFunction
from sumfunction import add

# créer un nouveau fichier, y écrire du text, et le refermer
fichier = open("text.txt", "w")
fichier.write("Un peu de texte")
fichier.close()

with open ("donnees.csv") as file_csv:
    reader = csv.reader(file_csv, delimiter=';')
    header = next(reader)
    print(header)
    for line in reader:
        print(line)
# Fermer le fichier
fichier.close()

# Importer (= include) un autre script
print(simpleFunction())
print(str(add(48, 57.5)))

# Autre manière d'importer : 
# import sumfunction
# print(sumfunction.simpleFunction())