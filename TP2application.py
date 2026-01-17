# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 23:57:01 2026

@author: abdou
"""

import tkinter as tk
from tkinter import messagebox
import numpy as np
from sklearn.linear_model import LinearRegression

# --- PARTIE LOGIQUE (VOTRE MODÈLE) ---
surface = np.array([1, 2, 3, 4, 5, 2, 3, 5, 4, 1])
engrais = np.array([50, 60, 70, 80, 90, 55, 65, 85, 75, 45])
pluie = np.array([800, 900, 1000, 1100, 1200, 850, 950, 1150, 1050, 780])
rendement = np.array([1.5, 2.0, 2.6, 3.0, 3.5, 1.8, 2.4, 3.4, 3.1, 1.4])

X = np.column_stack((surface, engrais, pluie))
model = LinearRegression()
model.fit(X, rendement)

# --- PARTIE INTERFACE (TKINTER) ---
def calculer_rendement():
    try:
        # Récupération des valeurs
        s = float(entry_surface.get())
        e = float(entry_engrais.get())
        p = float(entry_pluie.get())
        
        # Prédiction
        pred = model.predict([[s, e, p]])[0]
        
        # Mise à jour du label de résultat
        label_resultat.config(text=f"{pred:.2f} tonnes/ha", fg="#2ecc71")
    except ValueError:
        messagebox.showerror("Erreur de saisie", "Veuillez entrer des nombres valides (ex: 2.5)")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Prédiction de Rendement Agricole")
root.geometry("400x450")
root.config(bg="#f0f3f5")

# Style et Titre
tk.Label(root, text="Simulateur de Récolte", font=("Helvetica", 16, "bold"), bg="#f0f3f5", pady=20).pack()

# Conteneur pour le formulaire
frame = tk.Frame(root, bg="#f0f3f5")
frame.pack(pady=10)

def creer_champ(label_text):
    tk.Label(frame, text=label_text, font=("Arial", 10), bg="#f0f3f5").pack(anchor="w")
    entry = tk.Entry(frame, font=("Arial", 12), width=25)
    entry.pack(pady=5)
    return entry

# Champs de saisie
entry_surface = creer_champ("Surface (ha) :")
entry_engrais = creer_champ("Engrais (kg) :")
entry_pluie = creer_champ("Pluie (mm) :")

# Bouton de calcul
btn_calcul = tk.Button(root, text="Prédire le Rendement", command=calculer_rendement, 
                       bg="#3498db", fg="white", font=("Arial", 11, "bold"), 
                       padx=20, pady=10, cursor="hand2")
btn_calcul.pack(pady=20)

# Affichage du résultat
tk.Label(root, text="Rendement estimé :", font=("Arial", 10, "italic"), bg="#f0f3f5").pack()
label_resultat = tk.Label(root, text="--", font=("Helvetica", 18, "bold"), bg="#f0f3f5")
label_resultat.pack()

root.mainloop()