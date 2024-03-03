
import tkinter as tk
from tkinter import filedialog

from lifegame import LifeGame

CELL_SIZE = 400

class Application(tk.Tk):
    def __init__(self, jeu_de_la_vie):
        super().__init__()
        self.taille_case = None
        self.jeu_en_cours = False
        self.jeu_de_la_vie = jeu_de_la_vie
        self.canevas = tk.Canvas(self, width=400, height=400, bg='white')
        self.canevas.pack()
        self.bouton_start = tk.Button(self, text="Démarrer", command=self.demarrer)
        self.bouton_start.pack(side=tk.LEFT)
        self.bouton_stop = tk.Button(self, text="Arrêter", state=tk.DISABLED, command=self.arreter)
        self.bouton_stop.pack(side=tk.LEFT)
        self.bouton_evoluer = tk.Button(self, text="Un pas", command=self.evoluer)
        self.bouton_evoluer.pack(side=tk.LEFT)
        self.bouton_selectionner_fichier = tk.Button(self, text="Sélectionner un fichier",
                                                     command=self.selectionner_fichier)
        self.bouton_selectionner_fichier.pack(side=tk.LEFT)
        self.bouton_clear = tk.Button(self, text = "Vider", command=self.clean_screen)
        self.bouton_clear.pack(side=tk.LEFT)

        self.canevas.bind("<ButtonRelease-1>", self.inverser_un_point)

    def selectionner_fichier(self):
        chemin_fichier = filedialog.askopenfilename(title="Sélectionner un fichier")
        if chemin_fichier:
            # Lire le contenu du fichier et mettre à jour la grille du jeu
            with open(chemin_fichier, 'r') as f:
                contenu = f.read().strip()
                contenu = contenu.splitlines()
                self.jeu_de_la_vie.grille = contenu
            self.jeu_de_la_vie.calculate_size()
            self.dessiner_grille()

    def clean_screen(self):
        """erase all data from grid"""
        self.jeu_de_la_vie.clear()
        self.dessiner_grille()

    def dessiner_grille(self):
        self.canevas.delete(tk.ALL)
        self.taille_case = 400 // self.jeu_de_la_vie.row_nb
        for row in range(self.jeu_de_la_vie.row_nb):
            for col in range(self.jeu_de_la_vie.col_nb):
                couleur = 'black' if self.jeu_de_la_vie.est_vivante(row, col) else 'white'
                self.canevas.create_rectangle(col*self.taille_case, row*self.taille_case,
                                              (col+1)*self.taille_case, (row+1)*self.taille_case,
                                              fill=couleur, outline='gray')

    def inverser_un_point(self, event):
        """Inverse un point après avoir arrêté le jeu s'il est en cours"""
        if self.jeu_en_cours:
            self.jeu_en_cours = False
            for but in [self.bouton_start, self.bouton_evoluer, self.bouton_clear, self.bouton_selectionner_fichier]:
                but["state"] = tk.NORMAL

        x, y = event.x, event.y

        # trouve la case à inverser
        row = y // self.taille_case
        col = x // self.taille_case
        self.jeu_de_la_vie.inverser(row, col)
        self.dessiner_grille()

    def demarrer(self):
        self.jeu_en_cours = True
        self.bouton_stop["state"] = tk.NORMAL
        for but in [self.bouton_start, self.bouton_evoluer, self.bouton_clear, self.bouton_selectionner_fichier]:
            but["state"] = tk.DISABLED
        self.jouer()

    def arreter(self):
        self.jeu_en_cours = False
        self.bouton_stop["state"] = tk.DISABLED
        for but in [self.bouton_start, self.bouton_evoluer, self.bouton_clear, self.bouton_selectionner_fichier]:
            but["state"] = tk.NORMAL

    def evoluer(self):
        self.jeu_de_la_vie.evoluer()
        self.dessiner_grille()

    def jouer(self):
        if self.jeu_en_cours:
            self.evoluer()
            self.after(500, self.jouer)



if __name__ == "__main__":
    # Initialisation du jeu de la vie avec une grille de 20x20 et quelques cellules vivantes
    # jeu = LifeGame(r"./galaxy.txt")
    jeu = LifeGame(r"./initiale.txt")
    # Création de l'application Tkinter
    app = Application(jeu)
    app.dessiner_grille()
    app.mainloop()
