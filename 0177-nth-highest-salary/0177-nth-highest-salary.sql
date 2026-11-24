CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT salary FROM( SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk FROM Employee)
      AS ranked
      WHERE rnk = N
  );
END