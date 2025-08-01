# What percentage of patients had previous complications (Previous Complications = 1)?
import pandas as pd

# Load the dataset (if not already loaded)
df = pd.read_csv('datasets/maternal_health.csv')

# Calculate the percentage
percentage = (df['Previous Complications'].sum() / len(df)) * 100

# Round to 2 decimal places
percentage_rounded = round(percentage, 2)

print(f"Percentage of patients with previous complications: {percentage_rounded}%")
