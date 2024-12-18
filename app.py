import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Fonction pour vérifier si le dataset est compatible
def validate_columns(data):
    expected_columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
    return all(col in data.columns for col in expected_columns)


# Titre de l'application
st.title("Exploration de la base de données IRIS")

# Choix de la source de la base de données
choice = st.radio(
    "Choisissez la méthode pour charger les données :",
    ("Utiliser la base de données par défaut",
     "Télécharger un fichier CSV manuellement")
)

# Section pour charger les données
if choice == "Utiliser la base de données par défaut":
    # Charger la base de données par défaut (iris.csv)
    data = pd.read_csv("iris.csv")
    st.write(f"Le fichier par défaut a été chargé avec {data.shape[0]} lignes et {data.shape[1]} colonnes.")
    st.dataframe(data)

elif choice == "Télécharger un fichier CSV manuellement":
    # Formulaire de téléchargement de fichier
    uploaded_file = st.file_uploader("Téléchargez votre fichier CSV", type="csv")

    if uploaded_file is not None:
        # Charger le fichier téléchargé
        try:
            data = pd.read_csv(uploaded_file, encoding='utf-8')
        except UnicodeDecodeError:
            st.warning("Erreur d'encodage avec 'utf-8'. Tentative avec 'ISO-8859-1'.")
            data = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
        except Exception as e:
            st.error(f"Une erreur est survenue lors du chargement du fichier : {e}")
        st.write(f"Le fichier téléchargé a {data.shape[0]} lignes et {data.shape[1]} colonnes.")
        st.dataframe(data)

        # Vérification des colonnes du fichier
        if not validate_columns(data):
            st.error("Le fichier téléchargé ne contient pas les colonnes nécessaires.")
            data = None
    else:
        data = None

# Si des données sont chargées, procéder aux sections suivantes
if data is not None:

    # --- Section 1 : Informations sur la dataset ---
    st.header("Informations sur la dataset")
    st.subheader("Statistiques descriptives")
    st.write(data.describe())

    st.subheader("Filtrer les données")
    column = st.selectbox("Choisissez une colonne pour filtrer", data.columns)
    unique_values = data[column].unique()
    selected_value = st.selectbox(f"Filtrer par valeur dans {column}", unique_values)
    filtered_data = data[data[column] == selected_value]
    st.write(f"Données filtrées ({len(filtered_data)} résultats) :")
    st.dataframe(filtered_data)

    # --- Section 2 : Visualisation des données ---
    st.header("Visualisation des données")
    st.subheader("Graphiques")

    # Choisir le type de graphique
    plot_type = st.selectbox("Choisissez le type de graphique",
                             ("Histogramme avec KDE", "Scatterplot", "Lineplot", "Countplot", "Boxplot"))

    # Variables à utiliser pour les graphiques
    x_axis = st.selectbox("Choisissez une colonne pour l'axe X", data.columns)

    if plot_type == "Histogramme avec KDE":
        # Choisir le nombre de bins et activer KDE
        bins = st.slider("Choisissez le nombre de bins", min_value=5, max_value=50, value=20)
        fig, ax = plt.subplots()
        sns.histplot(data=data, x=x_axis, bins=bins, kde=True, ax=ax)
        st.pyplot(fig)

    elif plot_type == "Scatterplot":
        y_axis = st.selectbox("Choisissez une colonne pour l'axe Y", data.columns)
        hue = st.selectbox("Ajouter une variable de couleur (facultatif)", ["Aucune"] + list(data.columns))
        fig, ax = plt.subplots()
        if hue != "Aucune":
            sns.scatterplot(data=data, x=x_axis, y=y_axis, hue=hue, ax=ax)
        else:
            sns.scatterplot(data=data, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif plot_type == "Lineplot":
        y_axis = st.selectbox("Choisissez une colonne pour l'axe Y", data.columns)
        hue = st.selectbox("Ajouter une variable de couleur (facultatif)", ["Aucune"] + list(data.columns))
        fig, ax = plt.subplots()
        if hue != "Aucune":
            sns.lineplot(data=data, x=x_axis, y=y_axis, hue=hue, ax=ax)
        else:
            sns.lineplot(data=data, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif plot_type == "Countplot":
        fig, ax = plt.subplots()
        sns.countplot(data=data, x=x_axis, ax=ax)
        st.pyplot(fig)

    elif plot_type == "Boxplot":
        y_axis = st.selectbox("Choisissez une colonne pour l'axe Y", data.columns)
        fig, ax = plt.subplots()
        sns.boxplot(data=data, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    # --- Section 3 : Analyse supplémentaire (optionnel) ---
    st.header("Analyse supplémentaire")
    st.subheader("Calculer la corrélation")

    # Sélectionner uniquement les colonnes numériques pour la corrélation
    numeric_data = data.select_dtypes(include=["float64", "int64"])

    # Vérifier si des colonnes numériques existent
    if not numeric_data.empty:
        correlation_matrix = numeric_data.corr()
        st.write("Matrice de corrélation des colonnes numériques :")
        st.dataframe(correlation_matrix)

        # Afficher la heatmap de corrélation
        st.subheader("Heatmap de corrélation")
        fig, ax = plt.subplots()
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Il n'y a pas de colonnes numériques dans les données pour calculer la corrélation.")

else:
    st.info("Veuillez choisir un dataset pour commencer l'analyse.")
