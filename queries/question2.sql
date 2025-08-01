SELECT MIN(age) AS minimum_age,MAX(age) AS maximum_age,
(MAX(age)-MIN(age)) AS age_range
FROM health;