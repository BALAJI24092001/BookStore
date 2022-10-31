import sqlite3

con = sqlite3.connect("books.db")

cur = con.cursor()

def create_table(cur: sqlite3.Cursor):
    cur.execute("""
                CREATE TABLE BOOKS(
                id TEXT PRIMARY KEY,
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
        (id, book_name, authors_name, publisher, price)
        VALUES
        ("1474934986", "THE WILD FOLK", "SYLVIA LINSTEADT", "USBORNE PUBLISHING LTD", 399),
        ("9385288660", "THE HINDUS: AN ALTERNATIVE HISTORY", "WENDY DONIGER", "SPEAKING TIGER", 999),
        ("0143130080", "UPSTREAM: SELECTED ESSAYS", "MARY OLIVER", "PENGUIN BOOKS", 499),
        ("0060786523", "A SUITABLE BOY: A NOVEL", "VIKRAM SETH", "HARPER PERENNIAL MODERN CLASSICS", 1556),
        ("0571334652", "NORMAL PEOPLE", "SALLY ROONEY", "FABER & FABER", 499),
        ("1234566873", "ARIEL", 'SYLVIA PLATH', 'FABER & FABER', 399),
        ("140593025X", "ANXIOUS PEOPLE", "FREDRIK BACKMAN", 'SIMON & SCHUSTER', 499),
        ("9780349117", "SHANTARAM", "GREGORY DAVID ROBERTS", "ABACUS", 599),
        ("0552573507", "A BOY AT THE TOP OF THE MOUNTAIN", "JOHN BOYNE", "RH UK", 450)

                """)
create_table(cur)
enter_data(cur)

con.commit()
con.close()
