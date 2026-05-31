WITH rankedlist AS (
    SELECT 
        country,
        round(SUM(amount),2) AS total_sale,
        DENSE_RANK() OVER (ORDER BY SUM(amount) DESC) AS rn
    FROM orders
    GROUP BY country
)
SELECT total_sale, country
FROM rankedlist 
WHERE rn = 1;