import sqlite3, csv
from create_datasets import FILE_NAMES

con = sqlite3.connect("pizza_chain.db")
cur = con.cursor()
cur.execute("CREATE TABLE customer_reviews (id, title, review, date, ratings)")

for file in FILE_NAMES:
    with open(file, 'r') as f:
        dr = csv.DictReader(f)
        to_db = [(i[''], i['title'], i['review'], i['date'], i['ratings']) for i in dr]

    cur.executemany("INSERT INTO customer_reviews (id, title, review, date, ratings VALUES (?,?,?,?,?);",to_db)
    con.commit()
    con.close()

