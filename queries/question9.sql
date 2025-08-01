SELECT MAX(heartrate) AS max_heart_rate,
MIN(heartrate) AS min_heart_rate,
(MAX(heartrate) - MIN(heartrate)) AS range_heart_rate
FROM health;