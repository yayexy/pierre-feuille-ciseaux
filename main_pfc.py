import random


choices_long=["pierre","feuille","ciseaux"]
choices_short=["p","f","c"]

play_again=""
play_again_response=""

tour=0

def round_game():
    global tour
    tour=input("Vous voulez faire combien de tours gagnés ? ")

    while tour.isdigit()!=True or int(tour)>10:
        tour=input("Vous voulez faire combien de tours gagnés ? ")
    
    
def game_start():
    global ia, user
    
    user=input("pierre, feuille ou ciseaux ? (p, f ou c) ")
    ia=random.choice(choices_long)

    while user not in choices_short:
        print()
        print("Veuillez choisir une vraie valeur !")
        user=input("pierre, feuille ou ciseaux ? (p, f ou c) ")
        

def main_game():
    points_gagnés_user=0
    points_gagnés_ia=0

    while points_gagnés_user < int(tour) and points_gagnés_ia < int(tour):
        game_start() 
        if ((user=="p" and ia=="ciseaux") or (user=="f" and ia=="pierre") or (user=="c" and ia=="feuille")):
            points_gagnés_user+=1
            print(f"L'adversaire a fait {ia}")
            print("Vous avez gagné !")
            print(f"Mon score: {points_gagnés_user}")
            print(f"Adversaire: {points_gagnés_ia}")
            print()
        elif ((user=="p" and ia=="feuille") or (user=="f" and ia=="ciseaux") or (user=="c" and ia=="pierre")):
            points_gagnés_ia+=1
            print(f"L'adversaire a fait {ia}")
            print("Vous avez perdu !")
            print(f"Mon score: {points_gagnés_user}")
            print(f"Adversaire: {points_gagnés_ia}")
            print()
        elif ((user=="p" and ia=="pierre") or (user=="f" and ia=="feuille") or (user=="c" and ia=="ciseaux")):
            print(f"L'adversaire a fait {ia}")
            print("Il y a égalité !")
            print(f"Mon score: {points_gagnés_user}")
            print(f"Adversaire: {points_gagnés_ia}")
            print()
        else:
            print("Il y a un problème !")
    
    print("Merci d'avoir joué")     
            

def play_one_more_time():
    
    play_again=input("Voulez vous recommencer ? (oui ou non) ")
    play_again_response=["oui","non"]

    while play_again not in play_again_response:
        play_again=input("Voulez vous recommencer ? (oui ou non) ")

    if play_again=="oui":
        return play_again
    else:
        print("A bientôt !")

while True:
    round_game()
    main_game()
    play_one_more_time()