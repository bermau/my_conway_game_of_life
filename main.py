# Jeu de la vie
# D'après livre de Lafourcade

VIVANTE = "#"
MORTE = "-"


class LifeGame():
    def __init__(self):

        self.grille = []
        self.load()
        self.line_nb = len(self.grille)
        self.col_nb = len(self.grille[0])

    def load(self):
        with open("initiale.txt", 'r') as f:
            self.grille = f.read().splitlines()

    def afficher(self):
        for i in range(self.line_nb):
            print(self.grille[i])

    def compter_voisins(self, m, n):
        voisins = 0
        for row_i in (-1, 0, 1):  # row
            for col_i in (-1, 0, 1):  # col
                if row_i == 0 and col_i == 0:
                    continue
                else:
                    voisin_row = m + row_i
                    voisin_col = n + col_i
                    if (0 <= voisin_row < self.line_nb) and (0 <= voisin_col < self.col_nb):
                        if self.grille[voisin_row][voisin_col] == VIVANTE:
                            voisins += 1
        return voisins

    def evoluer(self):
        next_grille = []
        for m in range(self.line_nb):
            rangee = ""
            for n in range(self.col_nb):
                voisins = self.compter_voisins(m, n)
                if self.grille[m][n] == VIVANTE:
                    if voisins < 2 or voisins > 3:
                        rangee += MORTE
                    else:
                        rangee += VIVANTE
                else: # la cellule est morte
                    if voisins == 3:
                        rangee += VIVANTE
                    else:
                        rangee += MORTE

            next_grille.append(rangee)
        self.grille = next_grille


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = LifeGame()
    game.afficher()
    print()
    game.evoluer()
    game.afficher()
    print()
    game.evoluer()
    game.afficher()
