# Exploration de la base de données IRIS avec Streamlit

Ce projet permet d'explorer la base de données IRIS à l'aide de l'application interactive développée avec **Streamlit**. L'utilisateur peut télécharger un fichier CSV ou utiliser la base de données IRIS native. Il est possible d'afficher des statistiques descriptives, de filtrer les données et de générer différents types de graphiques interactifs.

## Fonctionnalités

- **Chargement du dataset** : L'utilisateur peut télécharger un fichier CSV ou charger la base de données IRIS.
- **Affichage des informations sur le dataset** : Statistiques descriptives et aperçu du dataset.
- **Filtrage des données** : Filtrer les données en fonction d'une colonne.
- **Graphiques interactifs** : Plusieurs types de graphiques sont disponibles :
  - Histogramme avec KDE
  - Scatterplot
  - Lineplot
  - Countplot
  - Boxplot
- **Matrice de corrélation** : Affichage de la matrice de corrélation des colonnes numériques.

## Prérequis

Avant de lancer l'application, assurez-vous que vous avez installé les dépendances suivantes :

- Python 3.x
- Streamlit
- Pandas
- Seaborn
- Matplotlib

## Installation

1. Clonez ce repository :
   ```bash
   git clone https://github.com/Apasize/streamlit_iris_exploration.git
   cd streamlit-iris-exploration
