import numpy as np
import tkinter as tk
import math as m
import random as rd

center_x = lambda x0, x1: (x0 + x1) / 2
center_y = lambda y0, y1: (y0 + y1) / 2 

def generer_graphe(noeuds: int):
    noeuds = int(noeuds) # mesure de sécurité temporraire puisque du texte fera planter

    liaisons = np.random.randint(0, 2, (noeuds, noeuds), dtype=np.bool_)
    np.fill_diagonal(liaisons, 0)
    liaisons = np.logical_xor(liaisons, np.transpose(liaisons))
    poids = np.random.randint(1, 256, (noeuds, noeuds))
    graphe = np.stack((liaisons, poids), axis=2)

    return graphe

def afficher_graphe(graphe: np.ndarray): 

    # Placer les points
    points = {chr(97+i): [rd.randint(0, 1450), rd.randint(0, 450)] for i in range(graphe.shape[0])} # This Madness
    print(points)
    

def resoudre_graphe(graphe: np.ndarray): # Not Implemented
    pass

def afficher_graphe_r(graphe_resolu: np.ndarray): # Not Implemented
    pass

def on_click(noeuds: int, canvas: tk.Canvas):
    G = generer_graphe(noeuds)
    afficher_graphe(G, canvas)
    #G_r = resoudre_graphe(G)
    #afficher_graphe_r(G_r)

afficher_graphe(generer_graphe(7))
