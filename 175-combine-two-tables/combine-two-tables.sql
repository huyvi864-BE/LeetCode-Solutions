# Write your MySQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
JOIN Address a ON p.personId = a.personId
UNION

SELECT p.firstName, p.lastName, NULL AS city, NULL AS state 
FROM Person p
LEFT JOIN Address a ON p.personId  = a.personId
WHERE a.addressId IS NULL;