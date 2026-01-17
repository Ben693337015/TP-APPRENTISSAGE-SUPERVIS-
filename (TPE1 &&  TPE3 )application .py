import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import os

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analyse de Performance Étudiante")
        
        # --- CORRECTION ICI : Utilisation du 'x' minuscule et sans espace ---
        self.root.geometry("1100x850")

        self.load_data()
        self.create_widgets()

    def load_data(self):
        file_path = 'Student_Performance.csv'
        if not os.path.exists(file_path):
            messagebox.showerror("Erreur", f"Fichier '{file_path}' introuvable dans le dossier.")
            return

        self.df = pd.read_csv(file_path)
        # Encodage binaire pour les activités
        self.df['Extracurricular Activities'] = self.df['Extracurricular Activities'].map({'Yes': 1, 'No': 0})
        
        self.X = self.df.drop('Performance Index', axis=1)
        self.y = self.df['Performance Index']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42)
        
        # Initialisation et entraînement des modèles
        self.models = {
            'Linéaire': LinearRegression(),
            'Ridge': Ridge(alpha=1.0),
            'Lasso': Lasso(alpha=0.1),
            'ElasticNet': ElasticNet(alpha=0.1, l1_ratio=0.5)
        }
        
        for name in self.models:
            self.models[name].fit(self.X_train, self.y_train)

    def create_widgets(self):
        # Titre principal
        tk.Label(self.root, text="Comparaison des Modèles de Régression", font=("Helvetica", 16, "bold")).pack(pady=15)

        # Tableau (Treeview)
        frame_table = tk.Frame(self.root)
        frame_table.pack(pady=10, padx=20, fill=tk.X)

        cols = ('Variable', 'Linéaire', 'Ridge', 'Lasso', 'ElasticNet')
        self.tree = ttk.Treeview(frame_table, columns=cols, show='headings', height=6)
        
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=140, anchor="center")
        
        self.tree.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.fill_coefficients()

        # Bouton d'action
        btn_plot = tk.Button(self.root, text="Générer le Graphique de Comparaison", 
                             command=self.show_plot, bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), padx=20)
        btn_plot.pack(pady=10)

        # Conteneur pour le graphique
        self.plot_frame = tk.Frame(self.root)
        self.plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.canvas = None

    def fill_coefficients(self):
        # On insère les coefficients dans le tableau
        for i, var_name in enumerate(self.X.columns):
            row_values = [var_name]
            for m_name in self.models:
                coef = self.models[m_name].coef_[i]
                row_values.append(f"{coef:.4f}")
            self.tree.insert('', tk.END, values=row_values)

    def show_plot(self):
        # Nettoyage de l'ancien graphique si existant
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        # Préparation des données pour Seaborn
        data_list = []
        for name, model in self.models.items():
            for i, var in enumerate(self.X.columns):
                data_list.append({'Modèle': name, 'Variable': var, 'Coefficient': model.coef_[i]})
        
        df_plot = pd.DataFrame(data_list)

        # Création de la figure Matplotlib
        fig, ax = plt.subplots(figsize=(9, 5))
        sns.barplot(data=df_plot, x='Variable', y='Coefficient', hue='Modèle', ax=ax)
        ax.set_title("Impact de chaque variable selon le modèle de régularisation")
        plt.xticks(rotation=20)
        plt.tight_layout()

        # Affichage dans Tkinter
        self.canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()