import sqlite3

# Tworzenie połączenia z bazą danych

conn = sqlite3.connect('sample.db')

# Tworzenie tabeli

conn.execute('''CREATE TABLE Employees
             (ID INT PRIMARY KEY NOT NULL,
             NAME TEXT NOT NULL,
             AGE INT NOT NULL,
             ADDRESS CHAR(50),
             SALARY REAL);''')

# Dodanie rekordów

conn.execute("INSERT INTO Employees (ID, NAME, AGE, ADDRESS, SALARY) \
             VALUES (1, 'John Doe', 28, '123 Main St', 3000.0 )")
conn.execute("INSERT INTO Employees (ID, NAME, AGE, ADDRESS, SALARY) \
             VALUES (2, 'Jane Smith', 32, '456 Oak Ave', 5000.0 )")
conn.execute("INSERT INTO Employees (ID, NAME, AGE, ADDRESS, SALARY) \
             VALUES (3, 'Bob Johnson', 45, '789 Maple Dr', 7500.0 )")

# Zapisanie zmian

conn.commit()

# Wyświetlenie wyników

cursor = conn.execute("SELECT ID, NAME, AGE, ADDRESS, SALARY from Employees")

for row in cursor:

    print("ID = ", row[0])

    print("NAME = ", row[1])

    print("AGE = ", row[2])

    print("ADDRESS = ", row[3])

    print("SALARY = ", row[4], "\n")

# Zamknięcie połączenia

conn.close()
