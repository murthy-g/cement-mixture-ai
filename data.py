import pandas as pd
import random

# Define the possible values for each column
cement_types = [
    "Ordinary Portland Cement (OPC)",
    "Portland Pozzolana Cement (PPC)",
    "Rapid Hardening Cement",
    "Quick Setting Cement",
    "Low Heat Cement",
    "Sulphate Resistant Cement",
    "White Cement",
    "Colored Cement",
    "Hydrophobic Cement",
    "Oil Well Cement",
    "Masonry Cement",
    "Expansive Cement",
    "Blast Furnace Slag Cement",
    "Composite Cement",
    "Pozzolanic Cement",
    "Air Entraining Cement",
    "High Alumina Cement",
    "Super Sulphated Cement",
    "High-Early-Strength Cement",
    "Composite Cement",
    "Oil Well Cement",
    "Masonry Cement"
]


aggregate_types = [
'Sand',
'Gravel',
'Crushed Stone',
'Crushed Granite',
'Crushed Limestone',
'Crushed Concrete',
'Expanded Clay',
'Expanded Shale',
'Steel Slag',
'Recycled Aggregates',
'Diatomaceous Earth',
'Pumice',
'Scoria',
'Expanded Polystyrene Beads (EPS)']
compressive_strengths = [random.randint(20, 60) for _ in range(1000)]
water_to_cement_ratios = [round(random.uniform(0.35, 0.60), 2) for _ in range(1000)]

# Create a list to store the data
data = []

# Generate 1000 records with random values
for _ in range(1000):
    cement_type = random.choice(cement_types)
    water_to_cement_ratio = random.choice(water_to_cement_ratios)
    aggregate_type = random.choice(aggregate_types)
    compressive_strength = random.choice(compressive_strengths)
    
    data.append([cement_type, water_to_cement_ratio, aggregate_type, compressive_strength])

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame(data, columns=['Cement Type', 'Water-to-Cement Ratio', 'Aggregate Type', 'Compressive Strength (MPa)'])
df.to_csv('cement_data.csv', index=False)

