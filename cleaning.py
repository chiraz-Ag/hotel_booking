import pandas as pd

# Charger le dataset
chemin_fichier = "C:/Users/ASUS VIVOBOOK X413J/Desktop/data/mini_projet/hotel_booking.csv"  # Remplacez par le chemin vers votre fichier
df = pd.read_csv(chemin_fichier)

# Afficher le nombre de colonnes
print(f"Nombre de colonnes : {df.shape[1]}")

# Afficher les titres des colonnes
print("Titres des colonnes :")
print(df.columns.tolist())

# Afficher une ligne exemple
print("Exemple d'une ligne :")
print(df.iloc[0])

# Vérifier les valeurs manquantes
missing_values = df.isnull().sum()

# Afficher les colonnes avec leurs valeurs manquantes
print("Nombre de valeurs manquantes par colonne :")
print(missing_values[missing_values > 0])

# Supprimer la colonne 'company'
df = df.drop(columns=['company'])

# Remplir les valeurs manquantes dans la colonne 'children' avec 0
df['children'] = df['children'].fillna(0)



