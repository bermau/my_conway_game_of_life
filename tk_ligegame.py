
import tkinter as tk
from tkinter import filedialog

from lifegame import LifeGame


class Application(tk.Tk):
    def __init__(self, jeu_de_la_vie):
        super().__init__()
        self.jeu_de_la_vie = jeu_de_la_vie
        self.canevas = tk.Canvas(self, width=400, height=400, bg='white')
        self.canevas.pack()
        self.bouton_start = tk.Button(self, text="Démarrer", command=self.demarrer)
        self.bouton_start.pack(side=tk.LEFT)
        self.bouton_stop = tk.Button(self, text="Arrêter", command=self.arreter)
        self.bouton_stop.pack(side=tk.LEFT)
        self.bouton_evoluer = tk.Button(self, text="Évoluer", command=self.evoluer)
        self.bouton_evoluer.pack(side=tk.LEFT)
        self.bouton_selectionner_fichier = tk.Button(self, text="Sélectionner un fichier",
                                                     command=self.selectionner_fichier)
        self.bouton_selectionner_fichier.pack(side=tk.LEFT)
        self.bouton_clear = tk.Button(self, text = "Vider", command=self.clean_screen)
        self.bouton_clear.pack(side=tk.LEFT)

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
        taille_case = 400 // self.jeu_de_la_vie.row_nb
        for x in range(self.jeu_de_la_vie.row_nb):
            for y in range(self.jeu_de_la_vie.col_nb):
                couleur = 'black' if self.jeu_de_la_vie.est_vivante(x, y) else 'white'
                self.canevas.create_rectangle(x*taille_case, y*taille_case,
                                              (x+1)*taille_case, (y+1)*taille_case,
                                              fill=couleur, outline='gray')


    def demarrer(self):
        self.jeu_en_cours = True
        self.jouer()

    def arreter(self):
        self.jeu_en_cours = False

    def evoluer(self):
        self.jeu_de_la_vie.evoluer()
        self.dessiner_grille()

    def jouer(self):
        if self.jeu_en_cours:
            self.evoluer()
            self.after(500, self.jouer)



if __name__ == "__main__":
    # Initialisation du jeu de la vie avec une grille de 20x20 et quelques cellules vivantes
    jeu = LifeGame(r"./galaxy.txt")

    # Création de l'application Tkinter
    app = Application(jeu)
    app.dessiner_grille()
    app.mainloop()
