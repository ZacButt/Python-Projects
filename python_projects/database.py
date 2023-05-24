
import sqlite3
import os

# List of file names
file_names = [
    "information.docx",
    "myImage.png",
    "Hello.txt",
    "myMovie.mpg",
    "World.txt"
]

# Connect to the database
conn = sqlite3.connect('file_database.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS files
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

# Iterate over the file names and insert the qualifying ones into the database
for file_name in file_names:
    if file_name.endswith('.txt'):
        cursor.execute("INSERT INTO files (name) VALUES (?)", (file_name,))

# Commit the changes to the database
conn.commit()

# Fetch the qualifying text files from the database
cursor.execute("SELECT name FROM files WHERE name LIKE '%.txt'")
qualifying_files = cursor.fetchall()

# Print the qualifying text files
for file in qualifying_files:
    print(file[0])

# Close the database connection
conn.close()
