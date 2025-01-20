Mesures DAX et Explications
Section 1 : Émissions et Énergie (Emissions and Energy)
Énergie Renouvelable Moyenne

DAX
Copier
Modifier
Avg_Renewable_Energy = AVERAGE('Emissions and Energy'[renewable_energy_percentage])
Description : Cette mesure calcule le pourcentage moyen d'énergie renouvelable utilisé dans toutes les usines. Cela permet de comprendre l'engagement global en matière de transition énergétique.

Bilan Carbone

DAX
Copier
Modifier
Carbon_Balance = SUM('Emissions and Energy'[co2_emissions_tons]) - SUM('Emissions and Energy'[co2_captured_tons])
Description : Cette mesure calcule le bilan carbone total en soustrayant le CO₂ capturé du CO₂ émis pour toutes les usines.

Bilan Carbone par Pays

DAX
Copier
Modifier
Carbon_Balance_x_Country = 
SUMX(
    VALUES('Plants'[country]),
    SUM('Emissions and Energy'[co2_emissions_tons]) - SUM('Emissions and Energy'[co2_captured_tons])
)
Description : Cette mesure calcule le bilan carbone pour chaque pays, en agrégeant les émissions et les captations de CO₂ par pays.

Impact Projeté des Énergies Renouvelables

DAX
Copier
Modifier
Projected_Renewable_Impact = CALCULATE(
    AVERAGE('Emissions and Energy'[renewable_energy_percentage]),
    FILTER('Emissions and Energy', 'Emissions and Energy'[future_emission_projection_tons] > 0)
)
Description : Cette mesure estime l'impact moyen des énergies renouvelables pour les usines ayant des projections futures d'émissions positives.

Total de CO₂ Capturé

DAX
Copier
Modifier
Total_CO2_Captured = SUM('Emissions and Energy'[co2_captured_tons])
Description : Cette mesure donne le total de CO₂ capturé par toutes les usines.

Total de CO₂ Émis

DAX
Copier
Modifier
Total_CO2_Emissions = SUM('Emissions and Energy'[co2_emissions_tons])
Description : Cette mesure calcule le total de CO₂ émis.

Consommation Énergétique Totale

DAX
Copier
Modifier
Total_Energy_Consumption = SUM('Emissions and Energy'[energy_consumption_kwh])
Description : Cette mesure donne la somme totale de l'énergie consommée en kWh.

Émissions Futuristes Projetées

DAX
Copier
Modifier
Total_Projected_Emissions = SUM('Emissions and Energy'[future_emission_projection_tons])
Description : Cette mesure donne le total des émissions projetées à l'avenir.

Section 2 : Environnement (Environmental)
Impact Moyen sur la Biodiversité

DAX
Copier
Modifier
Avg_Biodiversity_Impact = AVERAGE('Environmental'[biodiversity_impact_score])
Description : Cette mesure calcule l'impact moyen sur la biodiversité pour toutes les usines.

Superficie Totale Reboisée

DAX
Copier
Modifier
Total_Reforested_Area = SUM('Environmental'[reforestation_area_ha])
Description : Cette mesure donne la superficie totale (en hectares) des zones reboisées.

Nombre Total d’Espèces Impactées

DAX
Copier
Modifier
Total_Species_Impacted = SUM('Environmental'[species_impacted])
Description : Cette mesure donne le nombre total d'espèces affectées par les activités des usines.

Section 3 : Finance
Dépenses Totales

DAX
Copier
Modifier
Total_Expenses = SUM('Finance'[expenses_usd])
Description : Cette mesure calcule les dépenses totales des usines.

Revenus Totaux

DAX
Copier
Modifier
Total_Revenue = SUM('Finance'[revenue_usd])
Description : Cette mesure calcule les revenus totaux générés par les usines.

Section 4 : Gouvernance (Governance)
Score Moyen de Conformité

DAX
Copier
Modifier
Avg_Compliance_Score = AVERAGE('Governance'[compliance_score])
Description : Cette mesure calcule la moyenne des scores de conformité des usines, indiquant leur respect des normes ESG.

Pourcentage Moyen de Femmes dans les Postes de Leadership

DAX
Copier
Modifier
Avg_Women_in_Leadership = AVERAGE('Governance'[women_in_leadership_percentage])
Description : Cette mesure calcule le pourcentage moyen de femmes occupant des postes de direction dans toutes les usines.

Score Total de Conformité

DAX
Copier
Modifier
Compliance_Score_Total = SUM('Governance'[compliance_score])
Description : Cette mesure calcule le score de conformité total pour toutes les usines.

Investissements Sociaux Totaux

DAX
Copier
Modifier
Total_Social_Investments = SUM('Governance'[investment_social_programs_usd])
Description : Cette mesure calcule le montant total investi dans des programmes sociaux.

Section 5 : Risques (Risk)
Score Moyen d’Alignement sur l’Accord de Paris

DAX
Copier
Modifier
Avg_Paris_Alignment = AVERAGE('Risk'[paris_agreement_alignment_score])
Description : Cette mesure calcule la moyenne des scores d'alignement des usines avec l'Accord de Paris.

Nombre de Catégories de Risques

DAX
Copier
Modifier
Risk_Category_Count = COUNT('Risk'[risk_category])
Description : Cette mesure compte le nombre de catégories de risques identifiées dans toutes les usines.
