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
                );
                """)

def enter_data(cur: sqlite3.Cursor):
    listOfTables = cur.execute(
        """
        SELECT name FROM sqlite_master WHERE type='table'
        """).fetchall();
    cur.execute("""
        INSERT INTO BOOKS
        (id, book_name, authors_name, publisher, price, quantity)
        VALUES
        (1474934986, "THE WILD FOLK", "SYLVIA LINSTEADT", "USBORNE PUBLISHING LTD", 399, 19),
        (9385288660, "THE HINDUS: AN ALTERNATIVE HISTORY", "WENDY DONIGER", "SPEAKING TIGER", 999, 17),
        (0143130080, "UPSTREAM: SELECTED ESSAYS", "MARY OLIVER", "PENGUIN BOOKS", 499, 24),
        (0060786523, "A SUITABLE BOY: A NOVEL", "VIKRAM SETH", "HARPER PERENNIAL MODERN CLASSICS", 1556, 5),
        (0571334652, "NORMAL PEOPLE", "SALLY ROONEY", "FABER & FABER", 499, 8),
        (1234566873, "ARIEL", 'SYLVIA PLATH', 'FABER & FABER', 399, 15),
        (1029384856, "ANXIOUS PEOPLE", "FREDRIK BACKMAN", 'SIMON & SCHUSTER', 499, 0)
                """)
create_table(cur)
enter_data(cur)

con.commit()
con.close()
