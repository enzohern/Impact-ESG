Impact ESG : Analyse et Visualisation de Données avec Power BI et Python
Description du Projet
Le projet Impact ESG a pour objectif d'analyser, de modéliser et de visualiser des données liées aux indicateurs environnementaux, sociaux et de gouvernance (ESG) pour les entreprises et les institutions financières. Il s'appuie sur des données synthétiques générées pour simuler des scénarios réels, traitées avec Python et visualisées à travers des tableaux de bord interactifs dans Power BI.
Ce projet met en avant les principes de durabilité et de responsabilité d'entreprise tout en démontrant des compétences techniques avancées dans :
•	Le traitement et le nettoyage des données.
•	La modélisation des indicateurs ESG.
•	La création de tableaux de bord dynamiques.
•	Une analyse approfondie des tendances et des risques.
________________________________________
Table des Matières
1.	Introduction
2.	Données
3.	Traitement et Modélisation
4.	Visualisation avec Power BI
5.	Conclusion
6.	Exécution du Projet
7.	Structure du Projet
________________________________________
Introduction
La durabilité est devenue une priorité pour les entreprises et institutions à travers le monde. Ce projet vise à démontrer comment les indicateurs ESG peuvent être collectés, traités et utilisés pour créer des visualisations utiles qui soutiennent les décisions stratégiques.
Objectifs principaux :
1.	Analyser des indicateurs clés tels que les émissions de CO₂, la consommation d'énergie, l'impact sur la biodiversité et le respect des réglementations.
2.	Modéliser les projections climatiques et évaluer les risques associés au respect d'accords internationaux comme l'Accord de Paris.
3.	Fournir des outils visuels pour comprendre les performances ESG à différents niveaux : par site, par pays et à l'échelle globale.
________________________________________
Données
Le jeu de données utilisé dans ce projet contient des informations générées synthétiquement avec Python (bibliothèque Faker) pour représenter des scénarios réels. Il comprend les catégories suivantes :
1.	Indicateurs Environnementaux :
o	Émissions et capture de CO₂.
o	Consommation d'énergie et utilisation d'énergies renouvelables.
o	Impact sur la biodiversité et superficie reboisée.
2.	Indicateurs Sociaux :
o	Pourcentage de femmes en postes de direction.
o	Investissements dans les programmes sociaux.
3.	Indicateurs de Gouvernance :
o	Score de conformité réglementaire.
o	Catégorisation des risques et plans d'atténuation.
4.	Risques et Projections :
o	Projections des émissions futures.
o	Alignement avec l'Accord de Paris.
Taille du dataset : 1000 lignes et 23 colonnes.
________________________________________
Traitement et Modélisation
Traitement des Données avec Python
Le script Python effectue les étapes suivantes :
1.	Nettoyage des Données : Gestion des valeurs manquantes, des doublons et des anomalies.
2.	Standardisation : Conversion des unités et normalisation des champs principaux.
3.	Transformations : Création de colonnes supplémentaires pour des analyses avancées comme le "Bilan Carbone" ou les "Projections Futures".
Le code complet est disponible dans le fichier data_processing.py.
Modélisation des Indicateurs dans Power BI
Dans Power BI, des mesures avancées en DAX ont été créées pour modéliser les indicateurs clés :
•	Indicateurs Environnementaux :
o	Moyenne d'utilisation des énergies renouvelables.
o	Bilan carbone (émissions moins capture).
•	Indicateurs Sociaux :
o	Pourcentage moyen de femmes en leadership.
•	Indicateurs de Gouvernance :
o	Score moyen de conformité réglementaire.
•	Risques :
o	Projection des émissions futures.
________________________________________
Visualisation avec Power BI
Des tableaux de bord interactifs dans Power BI permettent :
1.	D'analyser les émissions et la consommation d'énergie au fil des années.
2.	De comparer les performances ESG par site et par pays.
3.	D'évaluer la conformité avec des objectifs climatiques comme l'Accord de Paris.
4.	D'identifier des tendances, des anomalies et des opportunités d'amélioration.
Exemples de Tableaux de Bord :
1.	Tableau de Bord Environnemental :
o	Visualisation des émissions de CO₂, des énergies renouvelables et du bilan carbone.
2.	Tableau de Bord Social :
o	Présentation des investissements dans les programmes sociaux et de la diversité en leadership.
3.	Tableau de Bord de Gouvernance :
o	Évaluation de la conformité réglementaire et des risques associés.
________________________________________
Conclusion
Le projet Impact ESG montre comment les données ESG peuvent être utilisées efficacement pour soutenir la durabilité et la responsabilité d'entreprise. Cette analyse fournit :
•	Des informations exploitables pour améliorer les performances ESG.
•	Des projections utiles pour se conformer aux normes internationales telles que l'Accord de Paris.
•	Des outils visuels accessibles pour communiquer des résultats aux parties prenantes.
Leçons Retenues :
1.	L'importance du nettoyage et de la modélisation des données pour obtenir des résultats significatifs.
2.	La puissance des mesures DAX pour créer des métriques personnalisées et détaillées.
3.	Le rôle des tableaux de bord dans la visualisation de grands volumes de données complexes.
