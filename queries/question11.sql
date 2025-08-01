SELECT 
  ROUND(
    100.0 * SUM(CASE WHEN risklevel = 'High' THEN 1 ELSE 0 END) / COUNT(*), 
    2
  ) AS high_risk_percentage
FROM health;
