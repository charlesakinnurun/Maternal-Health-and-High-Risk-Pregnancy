import pandas as pd

# Load the dataset
df = pd.read_csv('datasets/maternal_health.csv')

# Filter patients with gestational diabetes and compute median heart rate
median_hr = df[df['Gestational Diabetes'] == 1]['Heart Rate'].median()

print(f"Median heart rate for gestational diabetes patients: {median_hr} bpm")