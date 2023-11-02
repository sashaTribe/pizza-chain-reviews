import sqlite3, csv
from create_datasets import FILE_NAMES

try:
    con = sqlite3.connect("pizza_chain.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Customer_reviews")
    cur.execute("CREATE TABLE Customer_reviews (company,title, review, date, ratings)")

    for file in FILE_NAMES:
        with open(file, 'r', encoding= 'utf-8') as f:
            dr = csv.DictReader(f)
            to_db = [(i['Company Name'],i['Title of Review'], i['Review Description'], i['Date of Review'], i['No. of stars']) for i in dr]

        cur.executemany("INSERT INTO customer_reviews (company,title, review, date, ratings) VALUES (?,?,?,?,?);",to_db)
        con.commit()
        print(file, " uploaded to db")
    con.close()
except sqlite3.Error as error:
    print("Error while creating Customer Reviews Table", error)
finally:
    if con:
        con.close()
        print("Connection now closed")

