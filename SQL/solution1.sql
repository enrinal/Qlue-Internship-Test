SELECT date AS day,
COUNT(CASE WHEN score >= 0.00 THEN 1 ELSE NULL END) AS num_pos_scores,
COUNT(CASE WHEN score < 0.00 THEN 1 ELSE NULL END) AS num_neg_scores
FROM assessments
WHERE is_date >= STR_TO_DATE('2011-03-01', '%Y-%m-%d') 
AND is_date <= STR_TO_DATE('2011-04-30', '%Y-%m-%d')
GROUP BY DATE(date); 
