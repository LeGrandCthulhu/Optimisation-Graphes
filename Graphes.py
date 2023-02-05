import Graphes_fonctions as gf
import tkinter as tk
import numpy as np

root = tk.Tk()

root.title("Optimisation de graphes pondérés")
root.geometry("1080x720")
root.config(background="black")

#Création du canvas des graphes
canvas = tk.Canvas(root, bg="black", height=1013, width=1500, highlightthickness=0)


# Création de la zone de paramétrage en haut à droite
para = tk.Frame(root, bg="black")
texte_explications = tk.Label(para, text="Rentrez le nombre de noeuds dans le graphes", bg="black", font=("Arial", 15), fg="white")
entree = tk.Entry(para, bg="white", font=("Arial", 15))
validation = tk.Button(para, text="Valider", bg="grey", fg="white", font=("Arial", 15), command=lambda: gf.on_click(entree.get(), canvas))
para.grid(row=0, column=1, sticky=tk.N)
texte_explications.grid(row=0, column=0)
entree.grid(row=1, column=0)
validation.grid(row=2, column=0)



canvas.grid(row=0, column=0)

root.mainloop()