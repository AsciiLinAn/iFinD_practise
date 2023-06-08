import sqlite3

# Connect to the database
conn = sqlite3.connect('students.db')

# Create a cursor object
c = conn.cursor()

# Delete the table if it exists
c.execute('DROP TABLE IF EXISTS student_scores')

# Create a new table to store student scores
c.execute('''CREATE TABLE student_scores
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              student_id INTEGER,
              name TEXT,
              chinese INTEGER,
              math INTEGER,
              english INTEGER,
              science INTEGER,
              total INTEGER)''')

# Insert at least 10 student scores using SQL INSERT statement
insert_data = [(101, 'Alice', 80, 90, 90, 88, 0),
               (102, 'Bob', 75, 68, 92, 78, 0),
               (103, 'Charlie', 90, 87, 91, 89, 0),
               (104, 'David', 68, 79, 70, 73, 0),
               (105, 'Ella', 86, 0, 88, 90, 0),
               (106, 'Frank', 78, 81, 85, 76, 0),
               (107, 'Grace', 92, 89, 94, 90, 0),
               (108, 'Henry', 85, 72, 83, 88, 0),
               (109, 'Isabella', 89, 85, 90, 92, 0),
               (110, 'Jack', 76, 82, 83, 72, 0)]

c.executemany("INSERT INTO student_scores (student_id, name, chinese, math, english, science, total) VALUES (?, ?, ?, ?, ?, ?, ?)", insert_data)

# Update the total scores of all students
c.execute("""
UPDATE student_scores
SET total = chinese + math + english + science;
""")

# Use fetchall() method to query math scores that are lower than 60
c.execute("SELECT * FROM student_scores WHERE math < 60")
result = c.fetchall()
print(result)

# Use SQL UPDATE statement to modify the Chinese score for student 101
c.execute("UPDATE student_scores SET chinese = 85 WHERE student_id = 101")

# Use SQL DELETE statement to delete the student records with math scores lower than 60
c.execute("DELETE FROM student_scores WHERE math < 60")

# Commit the changes and close the connection
conn.commit()
conn.close()

# Connect to the database
conn = sqlite3.connect('students.db')

# Create a cursor object
c = conn.cursor()

# Select all rows from the table
c.execute('SELECT * FROM student_scores')

# Fetch all rows and print them to the console
rows = c.fetchall()
for row in rows:
    print(row)

# Close connection
conn.close()

