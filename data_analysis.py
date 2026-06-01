import sqlite3
import pandas as pd

conn = sqlite3.connect("company.db")

query = """
SELECT e.department AS department ,
       AVG(e.salary) AS average_salary,
       d.manager

FROM employees e

INNER JOIN departments d
ON e.department = d.department
GROUP BY e.department
"""

df = pd.read_sql_query(query, conn)

print(df)
import matplotlib.pyplot as plt
plt.bar(df["department"], df["average_salary"])

plt.title("Average Salary by Department")

plt.show()