-- Création de la table principale avec toutes les colonnes nécessaires
CREATE TABLE power_plant_data (
    plant_id VARCHAR(50) PRIMARY KEY,
    plant_name VARCHAR(255),
    country VARCHAR(100),
    year INT,
    co2_emissions_tons FLOAT,
    co2_captured_tons FLOAT,
    energy_consumption_kwh FLOAT,
    renewable_energy_percentage FLOAT,
    revenue_usd FLOAT,
    expenses_usd FLOAT,
    reforestation_area_ha FLOAT,
    compliance_score FLOAT,
    audit_count INT,
    women_in_leadership_percentage FLOAT,
    investment_social_programs_usd FLOAT,
    risk_category VARCHAR(50),
    risk_description TEXT,
    mitigation_plan TEXT,
    future_emission_projection_tons FLOAT,
    paris_agreement_alignment_score FLOAT
);

-- Filtrer les données pour l'année 2021, le pays "France" et une plante spécifique
SELECT *
FROM power_plant_data
WHERE year = 2021
  AND country = 'France'
  AND plant_name = 'EDF Plant';

-- Ajouter une colonne temporaire pour le bilan carbone
SELECT 
    plant_id,
    plant_name,
    country,
    year,
    co2_emissions_tons,
    co2_captured_tons,
    (co2_emissions_tons - co2_captured_tons) AS carbon_balance
FROM power_plant_data;

-- Filtrer les plantes qui ne sont pas alignées avec l'Accord de Paris (< 50)
SELECT 
    plant_name,
    country,
    paris_agreement_alignment_score
FROM power_plant_data
WHERE paris_agreement_alignment_score < 50;

-- Calculer la consommation d’énergie renouvelable en kWh
SELECT 
    plant_id,
    plant_name,
    year,
    energy_consumption_kwh,
    renewable_energy_percentage,
    (energy_consumption_kwh * renewable_energy_percentage / 100) AS renewable_energy_kwh
FROM power_plant_data;

-- Identifier les valeurs aberrantes en utilisant le percentile 95
WITH Percentile_95 AS (
    SELECT PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY co2_emissions_tons) AS threshold
    FROM power_plant_data
)
SELECT 
    p.*
FROM power_plant_data p, Percentile_95
WHERE p.co2_emissions_tons > Percentile_95.threshold;

-- Calculer le bénéfice net (revenus - dépenses) et classer les plantes
SELECT 
    plant_id,
    plant_name,
    country,
    year,
    revenue_usd,
    expenses_usd,
    (revenue_usd - expenses_usd) AS net_profit
FROM power_plant_data
ORDER BY net_profit DESC;

-- Lister toutes les plantes ayant un risque élevé
SELECT 
    plant_name,
    country,
    risk_category,
    risk_description,
    mitigation_plan
FROM power_plant_data
WHERE risk_category = 'High';

-- Analyser les tendances des émissions de CO2 au fil des années
SELECT 
    year,
    SUM(co2_emissions_tons) AS total_emissions,
    SUM(co2_captured_tons) AS total_captured
FROM power_plant_data
GROUP BY year
ORDER BY year;
