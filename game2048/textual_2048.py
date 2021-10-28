
def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    while move not in ["g","d","h","b"]:
        move = input( "Votre saisie est invalide. Réessayez.")
    return move

def read_size_grid():
    size = input("avec combien de tuiles souhaitez-vous jouer (entrez un nombre supérieur à 2):")
    while int(size)<2:
        size = input( "Votre saisie est invalide. Réessayez.")
    return size

def read_theme_grid():
    theme = input("Quelle thème voulez-vous ? (0 (défault),1 (Chemistery), 2 (Alphabet):)")
    while theme not in ["0","1","2"]:
        theme = input( "Votre saisie est invalide. Réessayez.")
    return theme
