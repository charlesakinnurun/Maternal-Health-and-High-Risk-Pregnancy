--How many patients have preexisting diabetes (Preexisting Diabetes = 1)?
SELECT COUNT(preexistingdiabetes) AS count_preexistingdiabetes FROM health
WHERE preexistingdiabetes = 1;