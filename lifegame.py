# Jeu de la vie
# D'après livre de Lafourcade

VIVANTE = "#"
MORTE = "-"


class LifeGame():
    def __init__(self, init_file):
        self.file_name = init_file
        self.grille = []
        self.load()
        self.row_nb = None
        self.col_nb = None
        self.calculate_size()

    def calculate_size(self):
        self.row_nb = len(self.grille)
        self.col_nb = len(self.grille)


    def load(self):
        with open(self.file_name, 'r') as f:
            self.grille = f.read().splitlines()

    def afficher(self):
        for i in range(self.row_nb):
            print(self.grille[i])

    def est_vivante (self, m, n):
        return self.grille[m][n] == VIVANTE

    def compter_voisins(self, m, n):
        voisins = 0
        for row_i in (-1, 0, 1):  # row
            for col_i in (-1, 0, 1):  # col
                if row_i == 0 and col_i == 0:
                    continue
                else:
                    voisin_row = m + row_i
                    voisin_col = n + col_i
                    if (0 <= voisin_row < self.row_nb) and (0 <= voisin_col < self.col_nb):
                        if self.grille[voisin_row][voisin_col] == VIVANTE:
                            voisins += 1
        return voisins

    def evoluer(self):
        next_grille = []
        for m in range(self.row_nb):
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

    def faire_n_cycles(self, n=1):
        self.afficher()
        for i in range(n):
            print(f"   cycle {i+1}/{n}")
            self.evoluer()
            self.afficher()

    def clear(self):
        line = MORTE * self.col_nb
        self.grille = [line for i in range(self.row_nb)]
        self.afficher()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = r"./galaxy.txt"
    game = LifeGame(file)
    game.faire_n_cycles(200)
