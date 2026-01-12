import requests
import sqlite3
connection=sqlite3.connect("books.db")
cursor=connection.cursor()
from flask import jsonify
url="https://openlibrary.org/search.json?q=python"
response=requests.get(url)
print("status code:",response.status_code)
data=response.json()
books=data["docs"]
print(books)
print("Total books fetched:",len(books))
print("First book data:")
print(books[0])
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER
)
""")
connection.commit()
print("Table created successfully")
for book in books:
    title = book.get("title")
    author_list = book.get("author_name")
    year = book.get("first_publish_year")

    if title and author_list and year:
        cursor.execute(
            "SELECT id FROM books WHERE title = ? AND author = ?",
            (title, author_list[0])
        )

        exists = cursor.fetchone()
        if not exists:
             cursor.execute(
            "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
            (title, author_list[0], year)
            )
connection.commit()
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

print("Books in database:")
for row in rows:
    print(row)
