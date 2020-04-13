import sqlite3

'''
Connect sqlite.
Can save in memory: ':memory:' or in file: 'employee.db'
'''
conn = sqlite3.connect('employee.db')
c = conn.cursor()

# Simple Action
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")

c.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 50000)")
c.execute("SELECT * FROM employees WHERE last='Schafer'")

print(c.fetchone()) # Show one result, can use (c.fetchall(), c.fetchmany())

# Commit and Close
conn.commit()
conn.close()
