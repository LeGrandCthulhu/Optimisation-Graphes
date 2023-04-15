import numpy as np
import tkinter as tk
import random as rd

def generer_graphe(noeuds: int) -> np.ndarray:
    noeuds = int(noeuds) # mesure de sécurité temporaire puisque du texte fera planter

    liaisons = np.random.randint(0, 2, (noeuds, noeuds), dtype=np.bool_)
    np.fill_diagonal(liaisons, 0)
    liaisons = np.logical_xor(liaisons, np.transpose(liaisons))
    poids = np.random.randint(1, 256, (noeuds, noeuds))
    graphe = np.stack((liaisons, poids), axis=2)

    return graphe

def afficher_graphe(graphe: np.ndarray, canvas: tk.Canvas) -> dict: 

    # Placer les points
    points = {chr(97+i): [rd.randint(0, 1450), rd.randint(0, 450)] for i in range(graphe.shape[0])} # This Madness
    d = {}
    
    for nom, coords in points.items():
        canvas.create_oval(coords[0], coords[1], coords[0]+10, coords[1]+10, outline="white", fill="white")
        canvas.create_text(coords[0], coords[1]-10, text=nom, font=("Arial", 12), fill="white")

    for lignes in range(graphe.shape[0]):
        l = []
        for collones in range(graphe.shape[0]):
            if graphe[:, :, 0][lignes][collones] == 1:
                canvas.create_line(points[chr(97+lignes)][0]+5, points[chr(97+lignes)][1]+5, points[chr(97+collones)][0]+5, points[chr(97+collones)][1]+5, fill="white")
                l.append(chr(97+collones))
        d[chr(97+lignes)] = l
    
    return d

def resoudre_graphe(graphe: np.ndarray) -> np.ndarray: # Not Implemented
    pass

def afficher_graphe_r(graphe_resolu: np.ndarray) -> None: # Not Implemented
    pass

def on_click(noeuds: int, canvas: tk.Canvas):
    canvas.delete("all")
    G = generer_graphe(noeuds)
    d = afficher_graphe(G, canvas)
    #G_r = resoudre_graphe(G)
    #afficher_graphe_r(G_r)


