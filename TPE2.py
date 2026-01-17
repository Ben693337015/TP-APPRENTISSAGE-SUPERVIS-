import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Préparation des données d'entraînement
surface = np.array([1, 2, 3, 4, 5, 2, 3, 5, 4, 1])
engrais = np.array([50, 60, 70, 80, 90, 55, 65, 85, 75, 45])
pluie = np.array([800, 900, 1000, 1100, 1200, 850, 950, 1150, 1050, 780])
rendement = np.array([1.5, 2.0, 2.6, 3.0, 3.5, 1.8, 2.4, 3.4, 3.1, 1.4])

X = np.column_stack((surface, engrais, pluie))

# 2. Entraînement du modèle
model = LinearRegression()
model.fit(X, rendement)



# Préparation des données
data = {
    'Surface': [1,2,3,4,5,2,3,5,4,1],
    'Engrais': [50,60,70,80,90,55,65,85,75,45],
    'Pluie': [800,900,1000,1100,1200,850,950,1150,1050,780],
    'Rendement': [1.5,2.0,2.6,3.0,3.5,1.8,2.4,3.4,3.1,1.4]
}
df = pd.DataFrame(data)

# Création de la figure avec 3 sous-graphiques
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Visualisation des Droites de Régression par Variable', fontsize=16)

features = ['Surface', 'Engrais', 'Pluie']
colors = ['steelblue', 'seagreen', 'indianred']

for i, col in enumerate(features):
    # sns.regplot trace les points ET la droite de régression
    sns.regplot(x=col, y='Rendement', data=df, ax=axes[i], color=colors[i])
    axes[i].set_title(f'{col} vs Rendement')
    axes[i].grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

print("=== Modèle de prédiction de rendement prêt ===")
print("Tapez 'q' à tout moment pour quitter.\n")

# 3. Boucle interactive
while True:
    try:
        entree = input("Appuyez sur Entrée pour continuer ou 'q' pour quitter : ").lower()
        if entree == 'q':
            break

        # Saisie des données
        s = float(input("Surface (ha) : "))
        e = float(input("Engrais (kg) : "))
        p = float(input("Pluie (mm) : "))

        # Calcul
        prediction = model.predict([[s, e, p]])
        
        print("-" * 30)
        print(f"Rendement prédit : {prediction[0]:.2f} tonnes/ha")
        print("-" * 30 + "\n")

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.\n")

print("Programme terminé.")

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Création d'un DataFrame pour faciliter la manipulation
df = pd.DataFrame({
    'Surface': surface,
    'Engrais': engrais,
    'Pluie': pluie,
    'Rendement': rendement
})

