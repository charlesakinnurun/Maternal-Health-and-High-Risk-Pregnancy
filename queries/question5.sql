SELECT risklevel,
COUNT(*),
AVG(diastolic) AS avg_diastolic,
MIN(diastolic) AS min_diastolic,
MAX(diastolic) AS max_diastolic,
STDDEV(diastolic) AS stddev_diastolic
FROM health
GROUP BY risklevel
ORDER BY risklevel;