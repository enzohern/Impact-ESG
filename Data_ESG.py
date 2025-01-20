import pandas as pd
import numpy as np

# Charger le dataset à partir d'un fichier CSV
file_path = "ESG_data_project"  # Remplacez par le chemin ou le nom de votre fichier
df = pd.read_csv(file_path)

# Afficher les premières lignes du dataset pour inspection
print("Données initiales :")
print(df.head())

# 1. ---------------- NETTOYAGE DES DONNÉES ----------------

# Supprimer les colonnes inutiles (si des colonnes ne sont pas pertinentes pour l'analyse)
# Supposons que les colonnes 'plant_id' et 'risk_description' ne sont pas nécessaires
colonnes_a_supprimer = ['plant_id', 'risk_description']
df = df.drop(columns=colonnes_a_supprimer, errors='ignore')

# Gérer les valeurs manquantes
# Options : remplacer par la moyenne, la médiane, une valeur spécifique ou supprimer les lignes
df['co2_emissions_tons'] = df['co2_emissions_tons'].fillna(df['co2_emissions_tons'].mean())
df['co2_captured_tons'] = df['co2_captured_tons'].fillna(0)
df['renewable_energy_percentage'] = df['renewable_energy_percentage'].fillna(0)
df['reforestation_area_ha'] = df['reforestation_area_ha'].fillna(0)
df['paris_agreement_alignment_score'] = df['paris_agreement_alignment_score'].fillna(df['paris_agreement_alignment_score'].median())

# Supprimer les lignes avec des valeurs critiques manquantes
df = df.dropna(subset=['year', 'country', 'plant_name'])

# Corriger les types de données
df['year'] = df['year'].astype(int)
df['country'] = df['country'].astype(str)
df['plant_name'] = df['plant_name'].astype(str)

# 2. ---------------- TRANSFORMATIONS ----------------

# Créer une nouvelle colonne : Bilan carbone (Émissions - Capture)
df['carbon_balance'] = df['co2_emissions_tons'] - df['co2_captured_tons']

# Créer une nouvelle colonne : Statut du bilan carbone
df['carbon_status'] = np.where(df['carbon_balance'] <= 0, 'Neutre', 'Positif')

# Créer une nouvelle colonne : Consommation d'énergie renouvelable en KWh
df['renewable_energy_kwh'] = (df['energy_consumption_kwh'] * df['renewable_energy_percentage']) / 100

# Créer une nouvelle colonne : Différence entre émissions actuelles et projetées
df['emission_difference'] = df['future_emission_projection_tons'] - df['co2_emissions_tons']

# Normaliser les scores de conformité (les échelles sont mises entre 0 et 100 si nécessaire)
df['compliance_score_normalized'] = (df['compliance_score'] / df['compliance_score'].max()) * 100

# 3. ---------------- ANALYSES PRÉLIMINAIRES ----------------

# Calculer des statistiques de base pour comprendre les données
statistiques = df.describe()
print("\nStatistiques de base du dataset :")
print(statistiques)

# Identifier les valeurs aberrantes des émissions de CO2 (percentile 95)
seuil_emission_co2 = df['co2_emissions_tons'].quantile(0.95)
valeurs_aberrantes = df[df['co2_emissions_tons'] > seuil_emission_co2]
print("\nValeurs aberrantes des émissions de CO2 (percentile 95) :")
print(valeurs_aberrantes)

# 4. ---------------- SAUVEGARDER LE DATASET TRAITÉ ----------------

# Exporter les données nettoyées et transformées vers un nouveau fichier CSV
processed_file_path = "processed_dataset.csv"
df.to_csv(processed_file_path, index=False)

print(f"\nLe dataset traité a été sauvegardé dans : {processed_file_path}")
