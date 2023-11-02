import sqlite3

try:
    connection_obj = sqlite3.connect('pizza_chain.db')
    cur = connection_obj.cursor()
    cur.execute("SELECT COUNT (*) FROM Customer_reviews")
    result = cur.fetchone()
    print(result)
    print("Submitted Command")
    connection_obj.close()
except sqlite3.Error as error:
    print("Error while creating Customer Reviews Table", error)
finally:
    if connection_obj:
        connection_obj.close()
        print("Connection now closed")



