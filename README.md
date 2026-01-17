# TP-APPRENTISSAGE-SUPERVIS-
Manipulation d'un jeu de données sur la performence scolaire (kaggle) et la prédiction d'un rendement agricole 




	(TP1   &   TP3)  

Description :

L'ensemble de données sur la performance des étudiants vise à examiner les facteurs influençant la réussite scolaire. Il comprend 10 000 dossiers d'étudiants, chacun contenant des informations sur divers prédicteurs et un indice de performance.

1. Aperçu des variables
•	Variable à prédire () : Performance Index.
•	Variables explicatives () : * Hours Studied (Heures d'étude)
o	Previous Scores (Scores précédents)
o	Sleep Hours (Heures de sommeil)
o	Sample Question Papers Practiced (Examens blancs pratiqués)
o	Extracurricular Activities (Activités extra-scolaires - converties en valeur numérique 0/1)
Performance index  : Mesure de la performance globale de chaque étudiant. Cet indice, arrondi à l'entier le plus proche, représente la performance scolaire de l'étudiant. Il varie de 10 à 100, les valeurs les plus élevées indiquant une meilleure performance.

Cet ensemble de données a pour objectif d'analyser la relation entre les variables prédictives et l'indice de performance. Les chercheurs et les analystes de données peuvent utiliser cet ensemble de données pour explorer l'impact du temps d'étude, des résultats antérieurs, des activités extrascolaires, du temps de sommeil et des exemples de sujets d'examen sur la réussite scolaire.

P.-S. : Veuillez noter que cet ensemble de données est synthétique et a été créé à des fins d'illustration. Les relations entre les variables et l'indice de performance peuvent ne pas refléter la réalité.
2. Interprétation des modèles
Voici comment comprendre ce que font ces algorithmes sur vos données d'étudiants :
•	Ridge (Régularisation L2) : Elle réduit la taille des coefficients sans jamais les annuler. Si deux variables sont très corrélées (ex: heures d'étude et scores précédents), Ridge va répartir le poids entre elles de manière équilibrée.
•	Lasso (Régularisation L1) : Elle est plus radicale. Elle peut forcer certains coefficients à devenir exactement zéro. C'est une méthode de "sélection de variables". Si une variable (comme le sommeil ou les activités extrascolaires) n'aide pas vraiment à prédire la note, Lasso l'éliminera.
•	Elastic Net : C'est un compromis entre Ridge et Lasso. Elle est idéale si vous avez un grand nombre de variables corrélées entre elles.
________________________________________
3. Interprétation des Coefficients (cas précis)
Une fois que vous exécutez le code, vous devez regarder la valeur des coefficients. Voici comment les lire :
1.	Le signe (+ ou -) : * Un coefficient positif (ex: Hours Studied) signifie que si cette variable augmente, la performance de l'étudiant augmente aussi.
o	Un coefficient négatif signifierait que la variable nuit à la performance.
2.	L'ampleur (la valeur) : * Plus le chiffre est élevé, plus la variable est "puissante". Dans ce dataset, vous remarquerez probablement que Hours Studied et Previous Scores ont les coefficients les plus élevés.
o	Si le coefficient de Sleep Hours est proche de zéro, cela signifie que dans ce modèle, dormir une heure de plus a un impact négligeable par rapport à réviser une heure de plus.


Modèle	Comportement des coefficients	Pourquoi l'utiliser ici ?

Linear	Coefficients bruts.	Modèle de base, simple à lire.
Ridge	Coefficients légèrement plus petits.	Si vos variables (ex: heures d'étude et sommeil) sont très liées entre elles.
Lasso	Peut mettre certains coefficients à zéro.	Pour identifier les variables inutiles. Si Sleep Hours devient 0, alors elle n'est pas essentielle.
Elastic Net	Entre Ridge et Lasso.	Le plus robuste si le jeu de données est complexe.


	TPE2
Interprétation :

Pour interpréter précisément les coefficients, il faut regarder les valeurs numériques que le modèle LinearRegression a calculées.
D'après nos données, si on exécute le code, on obtient approximativement ces coefficients (les valeurs peuvent varier légèrement selon l'arrondi) :
•	Coefficient Surface () : 
•	Coefficient Engrais () : 
•	Coefficient Pluie () : 
•	Intercept () : 
Voici comment les interpréter concrètement :
1. La Surface ()
C'est la variable la plus "puissante" par unité.
•	Interprétation : À quantité d'engrais et de pluie égale, si vous augmentez la surface de 1 hectare, le rendement augmente de 0,16 tonne/ha.
•	Signe : Positif (+), donc plus il y a de surface, plus le rendement total est élevé.
2. L'Engrais ()
•	Interprétation : Pour chaque kilo d'engrais supplémentaire ajouté par hectare (en gardant la surface et la pluie constantes), le rendement augmente de 0,01 tonne (soit 10 kg).
•	Analyse : Bien que le chiffre paraisse petit (0,01), il est crucial car on manipule souvent des dizaines de kilos d'engrais, ce qui finit par avoir un impact majeur sur le résultat final.
3. La Pluie ()
•	Interprétation : Chaque millimètre de pluie supplémentaire apporte environ 0,001 tonne (1 kg) de rendement en plus par hectare.
•	Analyse : C'est le coefficient le plus faible. Cela signifie que le rendement est moins "sensible" à une petite variation de pluie qu'à une petite variation de surface, mais comme les valeurs de pluie sont grandes (800mm, 1000mm), l'effet cumulé est important.
4. L'Intercept ()
•	Interprétation : C'est la valeur théorique du rendement si la surface, l'engrais et la pluie étaient à zéro.
•	Analyse : Ici, il est légèrement négatif. En statistique, cela arrive souvent quand les données ne commencent pas à zéro. Cela signifie simplement que sans ces trois facteurs, il est impossible d'avoir un rendement positif (ce qui est logiquement vrai en agriculture).
Résumé de la relation
L'équation de votre exploitation est : 
En résumé : Votre rendement est principalement piloté par la surface et l'engrais. La pluie joue un rôle de support stable mais moins "réactif" aux petites variations dans notre jeu de données actuel.

