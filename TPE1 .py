

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Chargement des données
df = pd.read_csv('Student_Performance.csv')

df.head()


df.info()

# 2. Prétraitement
# On convertit 'Extracurricular Activities' (Yes/No) en valeurs numériques (1/0)
df['Extracurricular Activities'] = df['Extracurricular Activities'].map({'Yes': 1, 'No': 0})

# 3. Séparation des variables
# X = variables prédictrices, y = variable cible (Performance Index)
X = df.drop('Performance Index', axis=1)
y = df['Performance Index']

# 4. Division en set d'entraînement et de test (80% entraînement, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Création et entraînement du modèle
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Prédictions et évaluation
y_pred = model.predict(X_test)


from sklearn import metrics


# Calcul des métriques
mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = metrics.r2_score(y_test, y_pred)

# Affichage des résultats
print("--- Évaluation du Modèle ---")
print(f"MAE (Erreur Moyenne Absolue) : {mae:.2f}")
print(f"MSE (Erreur Quadratique Moyenne) : {mse:.2f}")
print(f"RMSE (Racine de l'Erreur Moyenne) : {rmse:.2f}")
print(f"R² (Coefficient de détermination) : {r2:.4f}")


# Configuration du style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 5))

# --- GRAPHIQUE 1 : Droite de régression pour 'Hours Studied' ---
plt.subplot(1, 2, 1)
sns.regplot(x='Hours Studied', y='Performance Index', data=df, 
            line_kws={"color": "red"}, scatter_kws={'alpha':0.3})
plt.title('Heures d\'étude vs Performance')
plt.xlabel('Heures d\'étude')
plt.ylabel('Performance Index')

# --- GRAPHIQUE 2 : Valeurs Réelles vs Prédites ---
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_pred, alpha=0.5, color='blue')
# Tracer la ligne de perfection (y = x)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', linewidth=2)
plt.title('Valeurs Réelles vs Prédictions')
plt.xlabel('Valeurs Réelles')
plt.ylabel('Prédictions du Modèle')

plt.tight_layout()
plt.show()





## Regression logistique

#. Transformation des données

# Nous allons créer une nouvelle colonne Passed qui sera notre cible (y).

#  1 : Si Performance Index ≥ 50 (Réussite)

# 0 : Si Performance Index < 50 (Échec)



## TP3  Application dans notre cas dataset

from sklearn.linear_model import Ridge, Lasso, ElasticNet

# Initialisation des modèles
ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)
elastic = ElasticNet(alpha=0.1, l1_ratio=0.5)

# Entraînement
ridge.fit(X_train, y_train)
lasso.fit(X_train, y_train)
elastic.fit(X_train, y_train)

# Comparaison des coefficients
coeff_df = pd.DataFrame({
    'Variable': X.columns,
    'Linear': model.coef_,
    'Ridge': ridge.coef_,
    'Lasso': lasso.coef_,
    'ElasticNet': elastic.coef_
})

print("--- Comparaison des Coefficients ---")
print(coeff_df)





