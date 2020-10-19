import sqlite3
connection = sqlite3.connect('accounting.db')
crsr = connection.cursor()

crsr.execute(
    "SELECT * FROM employees WHERE first_name == 'Sarah' AND last_name == 'Day'")

data = crsr.fetchall()
print(data)
