# Tables de hachage = dictionnaires (en Python)
# Dictionnaire = associer une valeur à une clé (de type entier, string, fonction, élément d'une classe)

dic = {
    'chat': "cat",
    'chien': "dog",
    'vache': "cow",
    'tigre': "tiger",
    'poule': "chicken",
    'cheval': "horse"
}
print(dic)
# print(dic.get('chat'))

dic["souris"] = "mouse"
print(dic)

def ajouterMot(cle_mot, dictionnaire):
    if not cle_mot in dictionnaire:
        mot_en = input("Veuillez entrer le mot " + cle_mot + " en anglais : ")
        dictionnaire[cle_mot] = mot_en
        print(dictionnaire)
    else:
        print(cle_mot + " -> " + dictionnaire[cle_mot])


mot_fr = input("Veuillez entrer un mot français : ")
# mot_en = input("Veuillez entrer sa traduction en anglais : ")
ajouterMot(mot_fr, dic)

