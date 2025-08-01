SELECT risklevel,
COUNT(*) AS total_mothers,
AVG(heartrate) AS avg_heart_rate,
MIN(heartrate) AS min_heart_rate,
MAX(heartrate) AS max_heart_rate,
STDDEV(heartrate) AS stvdev_heart_rate
FROM health
WHERE risklevel IN ("Low","High")
GROUP BY risklevel;