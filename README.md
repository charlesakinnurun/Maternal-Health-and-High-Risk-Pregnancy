# Introduction
![Maternal Health](assets/maternal.jpg)
This dataset, named maternal_health.csv, contains medical information related to maternal health. It includes key health indicators such as blood pressure, blood sugar, body temperature, and heart rate, recorded for expectant mothers. The data also classifies the level of health risk, making it suitable for maternal health analysis and predictive modeling
***
🔍 SQL queries and Python script? Check them out [here](/queries/):
# Background
Driven by the need to explore maternal health patterns and outcomes, this analysis leverages a comprehensive dataset containing vital health metrics of expectant mothers. The goal is to identify key factors influencing maternal health risk, uncover trends in physiological indicators such as blood pressure, blood sugar, temperature, and heart rate, and generate actionable insights to support better health outcomes for mothers.
# Questions
### Demographics & General Stats
1. What is the average age of mothers in this dataset?
2. What is the age range (minimum and maximum) of the mothers?
3. How many unique risk levels are present in the dataset?
### Blood Pressure & Sugar
4. What is the average systolic blood pressure across all mothers?
5. How does diastolic blood pressure vary across different risk levels?
6. Are there any mothers with both high systolic and diastolic blood pressure?
7. What is the average blood sugar level?
8. How many mothers have blood sugar above 140 mg/dL?
### Heart Rate
9. What is the range of heart rates recorded in the dataset?
10. Do mothers with high risk levels have significantly different heart rates than those with low risk?
### Risk Level Analysis
11. What percentage of mothers fall into the high-risk category?
12. How many mothers in the dataset are considered low risk?
13. What is the average age of mothers in the high-risk group?
14. Which blood pressure type (systolic or diastolic) shows the strongest correlation with risk level?
### Multivariate Relationships
15. Is there a trend between age and risk level?
# Tools I Used
For my deep dive into the digital advertising strategies, I harnessed the power of several key tools:
- **Pandas:** Essential python library used for data manipulation, analysis, and cleaning.
- **SQL:** The backbone of my analysis, allowing me to query the database and unearth critical insights.
- **MySQL:** The chosen database management system, ideal for handling the job posting data.
- **Visual Studio Code:** My go-to for database management and executing SQL queries.
- **Git & GitHub:** Essential for version control and sharing my SQL scripts and analysis, ensuring collaboration and project tracking.
# Database Creation
```sql
CREATE SCHEMA `maternalhealth` ;
```
# Table Creation
```sql
CREATE TABLE health(
    age INT,
    SystolicBP INT,
    Diastolic INT,
    BS FLOAT,
    BodyTemp INT,
    BMI FLOAT,
    PreviousComplications INT,
    PreexistingDiabetes INT,
    GestationalDiabetes INT,
    MentalHealth INT,
    HeartRate INT,
    RiskLevel VARCHAR(255)
);
```
# The Analysis
#### Which blood pressure type (systolic or diastolic) shows the strongest correlation with risk level?
```python
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

```
#### Is there a trend between age and risk level?
```python
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

```
#### How many mothers have blood sugar above 140 mg/dL?
```sql
SELECT COUNT(*) FROM health
WHERE bs > 140;
```
#### Do mothers with high risk levels have significantly different heart rates than those with low risk?
```sql
SELECT risklevel,
COUNT(*) AS total_mothers,
AVG(heartrate) AS avg_heart_rate,
MIN(heartrate) AS min_heart_rate,
MAX(heartrate) AS max_heart_rate,
STDDEV(heartrate) AS stvdev_heart_rate
FROM health
WHERE risklevel IN ("Low","High")
GROUP BY risklevel;
```
The remaining queries are provided below.
[Queries](/queries/)
# What I Learned
Throughout this journey, I’ve sharpened my data analysis skills by diving deep into maternal health data using Pandas:
- **🧩 Powerful Data Handling:** Gained hands-on experience with advanced data cleaning and transformation techniques—filtering and reshaping the maternal health dataset for better clarity and usability.
- **📊 Insightful Aggregation:** Used groupby() and aggregation functions like mean(), count(), and sum() to uncover patterns across health indicators such as blood pressure, sugar levels, and heart rate. Also explored pivot_table to generate structured summaries of health risk categories.
- **💡 Data-Driven Insights:** Enhanced my analytical thinking by translating real-world health questions into actionable insights through targeted Pandas operations, supporting better understanding of maternal risk factors.
# Conclusions
This project, through the analysis of maternal health data, has offered meaningful insights into the factors affecting maternal health risk. The outcomes of this analysis help identify key health indicators and patterns that influence risk levels in expectant mothers. Healthcare professionals and analysts can gain a clearer understanding of maternal health dynamics by focusing on impactful metrics such as blood pressure, blood sugar, heart rate, and body temperature. This exploration underscores the importance of continuous health data analysis and adaptability in identifying at-risk individuals and supporting informed medical decision-making.
