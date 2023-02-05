import numpy as np

def generer_graphe(noeuds: int):
    noeuds = int(noeuds) # mesure de sécurité temporraire puisque du texte fera planter

    liaisons = np.random.random_integers(0, 1, (noeuds, noeuds))
    np.fill_diagonal(liaisons, 0)
    poids = np.random.random_integers(1, 255, (noeuds, noeuds))
    graphe = np.stack((liaisons, poids), axis=2)

    return graphe


