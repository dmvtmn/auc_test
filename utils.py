# import from CSV
2
3 # import the csv library
4 import csv
5
6 import sqlite3
7
8 with sqlite3.connect("new.db") as connection:
9 c = connection.cursor()
10
11 # open the csv file and assign it to a variable
12 employees = csv.reader(open("employees.csv", "rU"))
13
66
# create a new table called employees
15 c.execute("CREATE TABLE employees(firstname TEXT, lastname
TEXT)")
16
17 # insert data into table
18 c.executemany("INSERT INTO employees(firstname, lastname)
values (?, ?)", employees)
