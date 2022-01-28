# Write your MySQL query statement below
SELECT lastName, firstName, city, state
FROM Person AS P
LEFT JOIN Address AS A
ON P.personId = A.personId;