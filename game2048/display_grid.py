from game2048.grid_2048 import *

from tkinter import*

def _2048_graphical_grid_init():
    root = Tk()
    root.title("2048")
    toplevel = Toplevel(root)
    root.mainloop()

n = 4



TILES_BG_COLOR = {0: "#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f1b078", \
                  16: "#eb8c52", 32: "#f67c5f", 64: "#f65e3b", \
                  128: "#edcf72", 256: "#edcc61", 512: "#edc850", \
                  1024: "#edc53f", 2048: "#edc22e", 4096: "#5eda92", \
                  8192: "#24ba63"}

TILES_FG_COLOR = {0: "#776e65", 2: "#776e65", 4: "#776e65", 8: "#f9f6f2", \
                  16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", \
                  256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", \
                  2048: "#f9f6f2", 4096: "#f9f6f2", 8192: "#f9f6f2"}

TILES_FONT = {"Verdana", 40, "bold"}


def grille_vide():
    root = Tk()
    root.title(2048)
    Toplevel(root)
    for i in range(n):
        for j in range(n):
            tile = Frame(root, bg=TILES_BG_COLOR[0],height=100, width=100,borderwidth=2, relief=RIDGE)
            tile.grid(row =i, column = j )
    root.mainloop()


def graphical(grid_game):
    root = Tk()
    root.title("2048")
    n = len(grid_game)
    for i in range(n):
        for j in range(n):
            if grid_game[i][j]!=0:
                tile = Frame(root, bg=TILES_BG_COLOR[grid_game[i][j]],height=150, width=150,borderwidth=2, relief=RIDGE)
                label_fiel = Label(root, text=str(grid_game[i][j]),bg=TILES_BG_COLOR[grid_game[i][j]],relief=FLAT)
                tile.grid(row =i,column = j)
                label_fiel.grid(row =i,column = j)
            else:
                tile = Frame(root, bg=TILES_BG_COLOR[0],height=150, width=150,borderwidth=2, relief=RIDGE)
                tile.grid(row =i, column = j )
    return root

grid_game = [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2], [0, 0, 0, 0]]
"""""
display_grid(grid_game)
"""




""""
graphical_grid(grid_game).mainloop()
"""

def game_2048():
    grid_game = init_game()
    graphical_game = graphical(grid_game)
    Toplevel(graphical_game)

    def Key_event_left(i):
        global grid_game
        global graphical_game
        if move_possible(grid_game)[0]:
            grid_game = move_grid(grid_game, "left")
            grid_game = grid_add_new_tile(grid_game)
            graphical_game = graphical(grid_game)
            graphical_game.update()

    def Key_event_right(i):
        global grid_game
        global graphical_game
        if move_possible(grid_game)[1]:
            grid_game = move_grid(grid_game, "right")
            grid_game = grid_add_new_tile(grid_game)
            graphical_game = graphical(grid_game)
            graphical_game.update()

    def Key_event_down(i):
        global grid_game
        global graphical_game
        if move_possible(grid_game)[3]:
            grid_game = move_grid(grid_game, "down")
            grid_game = grid_add_new_tile(grid_game)
            graphical_game = graphical(grid_game)
            graphical_game.update()

    def Key_event_up(i):
        global grid_game
        global graphical_game
        if move_possible(grid_game)[2]:
            grid_game = move_grid(grid_game, "up")
            grid_game = grid_add_new_tile(grid_game)
            graphical_game = graphical(grid_game)
            graphical_game.update()

    graphical_game.bind('<KeyPress-q>',Key_event_left)
    graphical_game.bind('<KeyPress-d>',Key_event_right)
    graphical_game.bind('<KeyPress-s>',Key_event_down)
    graphical_game.bind('<KeyPress-z>',Key_event_up)
    graphical_game.mainloop()

game_2048()


