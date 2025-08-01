--What is the range of systolic blood pressure (Systolic BP) observed in the dataset?


SELECT MIN(systolicbp) AS min_systolicbp,
MAX(systolicbp) AS max_systolicbp,
MAX(systolicbp) - MIN(systolicbp) AS range_systolicbp
FROM health
WHERE systolicbp IS NOT NULL;