from gtts import gTTS # Google text-to-speech package
import os
import vlc
import math 

# Définition des paramètres 
a = input("Entrer la vitesse de rotation du moteur :")
print("La vitesse de rotation est de",a,"tours par minute")
b = round(int(a) * 2 * math.pi / 60, 2)

# Texte de sortie 
text = "Calcul de la vitesse de rotation radiale"
text += "Pour " + str(a) + " tours par minute on obtient " + str(b) + " radians par seconde"

# Paramétrage de la librairie pour la dictée orale en français
language = "fr" 
speech = gTTS(text=text, lang=language, slow=False)

# On convertit le texte en fichier .mp3
speech.save("tourtorad.mp3")

# Lancement d'une application pour lire le fichier mp3
# Ici VLC sans l'interface graphique
os.system("tourtorad.mp3")