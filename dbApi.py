import sqlite3

con = sqlite3.connect("books.db")

cur = con.cursor()

def create_table(cur: sqlite3.Cursor):
    cur.execute("""
                CREATE TABLE BOOKS(
                id INTEGER PRIMARY KEY,
                book_name TEXT NOT NULL,
                authors_name TEXT,
                publisher TEXT,
                price INTEGER NOT NULL,
                quantity INTEGER
                )
                """)

con.commit()
con.close()
