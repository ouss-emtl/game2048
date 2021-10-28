from game2048.textual_2048 import *


def create_grid(n): #crée une grille vide composée que de 0
    game_grid = []
    for i in range(0,n):
        game_grid.append([0 for i in range(n)])
    return game_grid

def grid_add_new_tile_at_position(grid,absc,ordo):
    grid[absc][ordo]=2
    return grid


from numpy import random as rd

def get_value_new_tile():#90% d'avoir une nouvelle tuile égale à 2 et 10% égale à 4
    proba=rd.random()
    if proba<=0.9:
        return 2
    else:
        return 4

def get_all_tiles(grid):#transforme notre liste en grille
    list_of_tiles=[]
    n= len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j]==' ' or grid[i][j]==0:#associe à ' ' la valeur 0 dans la liste
                list_of_tiles.append(0)
            else:
                list_of_tiles.append(grid[i][j])
    return list_of_tiles

def get_empty_tiles_positions(grid):#donne la position des tuiles vides
    n=len(grid)
    list_of_index_empty_tiles=[]
    for i in range(n):
        for j in range(n):
            if grid[i][j]==0 or grid[i][j]==" ":
                list_of_index_empty_tiles.append((i,j))
    return list_of_index_empty_tiles


def grid_get_value(grid,x,y):
    return grid[x][y]

def get_new_position(grid):
    list_of_empty_tiles_index=get_empty_tiles_positions(grid)#liste des positions de toutes les tuiles vides
    n=len(list_of_empty_tiles_index)
    if n==1:
        return list_of_empty_tiles_index[0][0],list_of_empty_tiles_index[0][1]
    else:
        m=rd.randint(0,n-1)#choisi la position d'une tuile vide au hasard
        return list_of_empty_tiles_index[m][0],list_of_empty_tiles_index[m][1]

def grid_add_new_tile(grid):
    x,y=get_new_position(grid)
    grid[x][y]=get_value_new_tile()
    return grid


def init_game(n=4):
    grid=create_grid(n)
    grid=grid_add_new_tile(grid_add_new_tile(grid))
    return grid

def somme(l):
    S=""
    for x in l:
        S+=x
    return S


def grid_to_stringbis(grid,n):
    l1=[" ===" for k in range(n)]
    L1="\n"+somme(l1)
    res=""
    for j in range(n):
        l2=""
        for i in range(n):
            if grid[j][i] in [2,4]:
                l2+="| "+str(grid[j][i])+" "
                if i==n-1:
                    l2="\n"+l2+"|"
                    res+=L1+l2
            else:
                l2+="| "+" "+" "
                if i==n-1:
                    l2="\n"+l2+"|"
                    res+=L1+l2
    res+=L1
    return res

def long_value(grid):
    res=1
    for x in grid:
        for y in x:
            if y!=" ":
                if len(str(y))>res:
                    res = len(str(y))
    return res

def grid_to_string_with_size(grid,n):
    longueur_max_tiles=long_value(grid)
    tile_size=longueur_max_tiles+2
    a=[" " for i in range(tile_size)]
    Sapce_of_empty_tile=somme(a)#Nb d'espaces dans une case vide
    b=["=" for i in range(tile_size)]
    B=" "+somme(b)
    l1=[B for k in range(n)]
    delimiter_tiles="\n"+somme(l1)#délimiteur entre les lignes
    res=""
    for j in range(n):
        l2=""
        for i in range(n):
            if grid[j][i]!=" ":
                if len(str(grid[j][i]))<longueur_max_tiles:
                    k=(tile_size-len(str(grid[j][i])))
                    if k%2==0:#si la différence est paire, on ajoute le même espace à l'avant et à l'arrière du str
                        c=[" " for i in range(k//2)]
                        C=somme(c)
                        l2+="|"+C+str(grid[j][i])+C
                    elif k%2==1:#si la différence est impaire, l'espace devant le str aura une longeur de plus que celui à l'arrière
                        c=[" " for i in range(k//2)]
                        C=somme(c)
                        l2+="| "+C+str(grid[j][i])+C
                    if i==n-1:
                        l2="\n"+l2+"|"
                        res+=delimiter_tiles+l2
                else:
                    l2+="| "+str(grid[j][i])+" "
                    if i==n-1:
                        l2="\n"+l2+"|"
                        res+=delimiter_tiles+l2
            else:
                l2+="|"+Sapce_of_empty_tile
                if i==n-1:
                    l2="\n"+l2+"|"
                    res+=delimiter_tiles+l2
    res+=delimiter_tiles
    return res


THEMES = {"0": {"name": "Default", 0: " ", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: " ", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: " ", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

def transfer_grid_themedefault_to_other(grid, theme):#fonction qui transforme une grille de theme par defaut avec une grille d'un autre theme
    grid_copy=grid.copy()
    n=len(grid_copy)
    res=[[] for k in range(n)]
    if theme["name"]=="Chemistry":
        for i in range(n):
            for j in range(n):
                res[i].append(THEMES["1"][grid_copy[i][j]])
        return res
    if theme["name"]=="Alphabet":
        for i in range(n):
            for j in range(n):
                res[i].append(THEMES["2"][grid_copy[i][j]])
        return res
    else:
        return grid_copy


def long_value_with_theme(grid,theme):
    grid_theme = transfer_grid_themedefault_to_other(grid,theme)
    return long_value(grid_theme)

def grid_to_string_with_size_and_theme(grid,theme,n):
    grid_theme = transfer_grid_themedefault_to_other(grid,theme)
    return grid_to_string_with_size(grid_theme,n)



def fusion_full_liste_left(liste):#fais la fusion des élements non nuls égaux consécutifs
    listebis=[]
    i=0
    if len(liste)==1:
        return liste
    else:
        while i<len(liste)-1:
            if liste[i]==liste[i+1]:#si on a 2 éléments consécutifs égaux, on les fusionne
                listebis.append(2*liste[i])
                i+=2
            else:
                listebis.append(liste[i])
                i+=1
            if i==len(liste)-1:
                listebis.append(liste[i])
    return listebis



def move_row_left(l1):
    l=np.array(l1).tolist()#cette précaution m'a été nécessaire au vu de move_grid qui transforme la liste en array
    n=len(l)
    liste=[]
    if l==[0 for i in range(n)]:#On distingue directement le cas le plus évidents
        return(l)
    else:
        for i in range(n):         #On regroupe dans une même liste tous les éléments non nuls et on les fusionne si c'est possible
            if l[i]!=0:
                liste.append(l[i])
        listebis=fusion_full_liste_left(liste)
        if len(listebis)==n:#cas où pas de fusion possible et pas d'éléments nuls
            return l
        else:
            return listebis+[0 for i in range(n-len(listebis))]


def reverse_list(l):#crée une liste dont les éléments sont inversés
    res=[]
    n=len(l)
    for k in range(n):
        res.append(l[n-1-k])
    return res

def move_row_right(l):
    return reverse_list(move_row_left(reverse_list(l)))

import numpy as np

def move_grid(grid, d):
    gridbis=grid.copy()#on fait une copie pour ne pas modifier la grille de départ
    n=len(gridbis)     #Cela nous aidera pour la suite pour faire des comparaisons
    if d=="left":
        for k in range(n):
            gridbis[k]=move_row_left(gridbis[k])
    if d=="right":
        for k in range(n):
            gridbis[k]=move_row_right(gridbis[k])
    if d=="up":                       #Pour déplacer vers le haut, on transpose et on déplace vers la gauche
        gridbis=np.asarray(gridbis)   #puis on retranspose
        gridbis=np.transpose(gridbis)
        for k in range(n):
            gridbis[k]=move_row_left(gridbis[k])
        gridbis=np.transpose(gridbis)
        gridbis=gridbis.tolist()
    if d=="down":#Pour déplacer vers le bas, on transpose et on déplace vers la droite
        gridbis=np.asarray(gridbis) #puis on retranspose
        gridbis=np.transpose(gridbis)
        for k in range(n):
            gridbis[k]=move_row_right(gridbis[k])
        gridbis=np.transpose(gridbis)
        gridbis=gridbis.tolist()
    return gridbis


def is_grid_full(grid):
    grid_copy=grid.copy()#servira de comparaison avec la grille qui sera déplacée, cette étape n'est pas
    m=True               #nécessaire d'après la copie faite dans move_grid
    for d in ["left","right","up","down"]:
        if grid_copy != move_grid(grid,d):
            m=False
            break
    return m

def move_possible(grid):
    res = [True for k in range(4)]
    move=["left","right","up","down"]
    for k in range(4):
        if grid == move_grid(grid,move[k]):#pas besoin de faire de copies d'après la copie de move_grid()
            res[k]=False
    return res

def is_game_over(grid):
    if move_possible(grid)==[False for k in range(4)]:
        return True
    else:
        return False

def get_grid_tile_max(grid):
    maximum=0
    for x in grid:
        for y in x:
            if y>maximum:
                maximum=y
    return maximum

def is_game_win(grid):
    for x in grid:
        for y in x:
            if y>=2048:
                return True
    return False

THEMES = {"0": {"name": "Default", 0: "0", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "0", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "0", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


def random_play(k,n=4, theme=THEMES["0"]):#j'ai ajouté un argument k pour choisir le nombre de parties jouées
    grid= init_game(n)
    print(grid_to_string_with_size_and_theme(grid,theme,n))
    dictionnary_of_position={0:"left",1:"right",2:"up",3:"down"} #on crée un dictionnaire pour pouvoir choisir un
    for i in range(k):                                           #move au hasard dans la boucle
        if is_game_over(grid):
            print("Game Over")
            break
        else:
            move=rd.randint(0,3)
            grid = move_grid(grid,dictionnary_of_position[move])
            grid = grid_add_new_tile(grid)
            print(grid_to_string_with_size_and_theme(grid,theme,n))
    return is_game_win(grid)


def game_play():
    theme= THEMES[read_theme_grid()] #Le joueur choisi son thème
    n= int(read_size_grid())         #Le joueur choisi la taille de la grille
    grid = init_game(n)
    print(grid_to_string_with_size_and_theme(grid,theme,n))
    dictionnary_of_move={"g":"left","d":"right","h":"up","b":"down"} #On crée un dictionnaire pour pour traduire le choix
    while is_game_over(grid) == False:                               #du joueur avec une entrée valable pour move_grid()
        move = read_player_command()
        grid=move_grid(grid,dictionnary_of_move[move])
        grid=grid_add_new_tile(grid)
        print(grid_to_string_with_size_and_theme(grid,theme,n))
        if is_game_win(grid):
            print("Vous avez gagnez le jeu")
        m=input("Si vous voulez arrêter le jeu, tapez e, sinon tapez n'importe quoi :")
        if m=="e":
            break
    print("Game Over")

