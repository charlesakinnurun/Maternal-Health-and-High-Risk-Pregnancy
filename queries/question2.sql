--How many patients are classified as "High" risk versus "Low" risk?
SELECT risklevel,COUNT(*) AS count FROM health 
GROUP BY risklevel
ORDER BY count DESC;