import sqlite3

con = sqlite3.connect("finance.db")
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tshirts
                    (sku text PRIMARY KEY, name text, size text, price real)''')

cur.execute('''INSERT OR IGNORE INTO tshirts VALUES
                    ("SKU1234", "Black logo Tshirts", "medium", "24.99")''')

con.commit()

for row in cur.execute('''SELECT * FROM tshirts'''):
    print(row)