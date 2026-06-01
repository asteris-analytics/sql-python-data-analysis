SELECT * FROM employees;

SELECT name, salary
FROM employees;

SELECT *
FROM employees
WHERE salary > 1500;

SELECT department, AVG(salary)
FROM employees
GROUP BY department;

SELECT employees.department,
       AVG(employees.salary) AS average_salary,
       departments.manager

FROM employees

INNER JOIN departments
ON employees.department = departments.department

GROUP BY employees.department;