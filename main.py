#Amir Bozorgpour
#402
#10-17-23
#TP2




import random   #Imports the 'random' library into pycharm

def jouer_jeu():
 borne_minimale = 0 #sets minimum value
 borne_maximale = 1000 #sets maximum value
 nombre_choisi = random.randint(borne_minimale, borne_maximale) #generates a number between borne_minimale and borne_maxmimale
 nb_essais = 0 # number of tries

 print("Point de départ :")
 print(f"J'ai choisi un nombre au hasard entre {borne_minimale} et {borne_maximale}.")
 print("À vous de le deviner...")

 while True: #loop to give the option of repeating the game
  essai = int(input("Entrez votre essai : ")) #inputs attempt
  nb_essais += 1 #logs the attempt

  if essai < nombre_choisi:
   print(f"Mauvais choix, le nombre est plus grand que {essai}")
  elif essai > nombre_choisi:
   print(f"Mauvais choix, le nombre est plus petit que {essai}")
  else:
   print("Bravo! Bonne réponse.")
   print(f"Vous avez réussi en : {nb_essais} essai(s).")
   replay = input("Voulez-vous faire une autre partie (y/n)? ")
   nb_essais = 0 #resets nb of attempts to 0 after finishing
   nombre_choisi = random.randint(borne_minimale, borne_maximale) #generates a new number
   if replay.lower() != 'y':
    print("Merci et au revoir...")
    break


jouer_jeu()