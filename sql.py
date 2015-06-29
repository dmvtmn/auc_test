# sql.py - Create a SQLite3 table and populate it with data


import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect("offre.db") as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute("""CREATE TABLE ubscores
             (ub TEXT, score_saturation INT, score_performance INT, score_loyalty INT, score_dynamisme INT, score_final TEXT)
              """)

    # insert dummy data into the table
    c.execute('INSERT INTO ubscores VALUES("Poudres", 100, 42, 40, 66, "red")')
    c.execute('INSERT INTO ubscores VALUES("Liquides premium", 100, 64, 34, 67, "red")')
    c.execute('INSERT INTO ubscores VALUES("Tablettes", 99, 20, 1, 59, "orange")')
    c.execute('INSERT INTO ubscores VALUES("Marque propre",1, 29, 35, 57, "green")')
