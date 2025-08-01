import pandas as pd

# Load dataset
df = pd.read_csv("datasets/maternal_health.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Encode risk level
risk_map = {'low risk': 1, 'mid risk': 2, 'high risk': 3}
df['risk_numeric'] = df['risk_level'].map(risk_map)

# Correlation between Age and Risk Level
correlation_age_risk = df['age'].corr(df['risk_numeric'])

print(f"Correlation between Age and Risk Level: {correlation_age_risk:.3f}")
