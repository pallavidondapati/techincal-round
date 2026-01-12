import csv
import sqlite3
connection=sqlite3.connect("users.db")
cursor=connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
""")
with open("users.csv",mode="r",newline="",encoding="utf-8") as file:
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        try:
            cursor.execute(
                "INSERT INTO users (name,email) VALUES (?,?)",
                (row["name"],row["email"])
            )
        except Exception as e:
            print(e)
connection.commit()
cursor.execute("SELECT * FROM users")
rows=cursor.fetchall()
for  row in rows:
    print(row)
connection.close()
print("csv imported successfully")