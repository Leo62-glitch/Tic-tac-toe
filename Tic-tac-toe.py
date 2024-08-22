import tkinter as tk
import random

def verifier_victoire(grille, joueur):
    """Vérifie si le joueur a gagné."""
    for ligne in grille:
        if all(cell == joueur for cell in ligne):
            return True
    for col in range(3):
        if all(grille[row][col] == joueur for row in range(3)):
            return True
    if all(grille[i][i] == joueur for i in range(3)):
        return True
    if all(grille[i][2 - i] == joueur for i in range(3)):
        return True
    return False

def mouvement_robot(grille):
    """Effectue un mouvement aléatoire pour le robot."""
    libres = [(r, c) for r in range(3) for c in range(3) if grille[r][c] == " "]
    return random.choice(libres) if libres else None

def clic_bouton(row, col):
    """Gère le clic sur un bouton."""
    global joueur_actuel
    if grille[row][col] == " " and joueur_actuel == "X":
        grille[row][col] = joueur_actuel
        boutons[row][col].config(text=joueur_actuel)
        if verifier_victoire(grille, joueur_actuel):
            resultat_label.config(text="Tu as gagné !")
            root.after(2000, redemarrer_jeu)  # Attendre 2 secondes avant de redémarrer le jeu
            return
        elif all(cell != " " for ligne in grille for cell in ligne):
            resultat_label.config(text="Match nul !")
            root.after(2000, redemarrer_jeu)  # Attendre 2 secondes avant de redémarrer le jeu
            return
        joueur_actuel = "O"
        # Mouvement du robot
        ligne, col = mouvement_robot(grille)
        if ligne is not None and col is not None:
            grille[ligne][col] = joueur_actuel
            boutons[ligne][col].config(text=joueur_actuel)
            if verifier_victoire(grille, joueur_actuel):
                resultat_label.config(text="Le robot a gagné !")
                root.after(2000, afficher_game_over)  # Afficher la fenêtre de fin de jeu
                return
            elif all(cell != " " for ligne in grille for cell in ligne):
                resultat_label.config(text="Match nul !")
                root.after(2000, redemarrer_jeu)  # Attendre 2 secondes avant de redémarrer le jeu
                return
        joueur_actuel = "X"

def redemarrer_jeu():
    """Redémarre le jeu."""
    global grille, joueur_actuel
    grille = [[" " for _ in range(3)] for _ in range(3)]
    joueur_actuel = "X"
    for row in range(3):
        for col in range(3):
            boutons[row][col].config(text=" ")
    resultat_label.config(text="C'est ton tour !")

def afficher_game_over():
    """Affiche la fenêtre de fin de jeu."""
    game_over_window = tk.Toplevel(root)
    game_over_window.title("Game Over")
    game_over_label = tk.Label(game_over_window, text="Le robot a gagné !", font=("Arial", 20))
    game_over_label.pack(pady=10)
    ok_button = tk.Button(game_over_window, text="OK", command=game_over_window.destroy)
    ok_button.pack(pady=10)

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Création de la grille
grille = [[" " for _ in range(3)] for _ in range(3)]
joueur_actuel = "X"

# Création des boutons pour la grille
boutons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        boutons[row][col] = tk.Button(root, text=" ", font=("Arial", 40), width=5, height=2,
                                      command=lambda r=row, c=col: clic_bouton(r, c))
        boutons[row][col].grid(row=row, column=col)

# Label pour afficher le résultat
resultat_label = tk.Label(root, text="C'est ton tour !", font=("Arial", 20))
resultat_label.grid(row=3, column=0, columnspan=3)

# Lancer l'interface graphique
root.mainloop()
