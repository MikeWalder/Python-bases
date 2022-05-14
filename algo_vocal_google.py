from gtts import gTTS
import os
import vlc

# Définition des valeurs de la recette
nbre_personnes = 4
prix_plat = 12
total = nbre_personnes * prix_plat

# Texte de sortie 
text = "Voici les frais du repas de ce soir."
text += "Pour " + str(nbre_personnes) + " personnes à " + str(prix_plat) + " euros le plat, "
text += "cela fait un coût total de " + str(total) + " euros."

# Paramétrage de la librairie pour la dictée orale en français
language = "fr"
speech = gTTS(text=text, lang=language, slow=True)

# On convertit le texte en fichier .mp3
speech.save("recette.mp3")

# Lancement d'une application pour lire le fichier mp3
# Ici VLC sans l'interface graphique
os.system("recette.mp3")
# media = vlc.MediaPlayer("recette.mp3")
# media.play()