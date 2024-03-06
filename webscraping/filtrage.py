import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Chargement des données
data = pd.read_csv('combined_data.csv')

# Nettoyage des données
data.drop_duplicates(inplace=True)

# Gestion des valeurs manquantes
#imputer = SimpleImputer(strategy='mean')
#data['colonne_numerique'] = imputer.fit_transform(data[['colonne_numerique']])

# Normalisation
#scaler = StandardScaler()
#data['colonne_numerique'] = scaler.fit_transform(data[['colonne_numerique']])

# Sauvegarde des données nettoyées
data.to_csv('combined_data_nettoyé.csv', index=False)