import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/maternal_health.csv")

# Clean column names (optional but helps avoid errors)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Map risk level to numeric values
risk_map = {
    'low risk': 1,
    'mid risk': 2,
    'high risk': 3
}
df['risk_numeric'] = df['risk_level'].map(risk_map)

# Calculate correlation
correlation_systolic = df['systolic_bp'].corr(df['risk_numeric'])
correlation_diastolic = df['diastolic'].corr(df['risk_numeric'])

print(f"Correlation between Systolic BP and Risk Level: {correlation_systolic:.3f}")
print(f"Correlation between Diastolic BP and Risk Level: {correlation_diastolic:.3f}")

# Interpretation
if abs(correlation_systolic) > abs(correlation_diastolic):
    print("➡️ Systolic BP has a stronger correlation with Risk Level.")
else:
    print("➡️ Diastolic BP has a stronger correlation with Risk Level.")
