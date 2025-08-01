-- What is the average BMI for patients with a "High" risk level?
SELECT AVG(bmi) AS average_bmi FROM health
WHERE risklevel = "High";