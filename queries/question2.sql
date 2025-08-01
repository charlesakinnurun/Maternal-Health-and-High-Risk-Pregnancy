SELECT risklevel,COUNT(*) AS count FROM health 
GROUP BY risklevel
ORDER BY count DESC;