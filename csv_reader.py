#!/usr/bin/env python

# Use case 1:
# Command line app which receives a csv file as an input. It then connects
# to a sqlite database and inserts csv records in to the database. When it
# completes this task it prints a summary of how many records were inserted
# and how many total records there are.

import sys
import csv
import sqlite3
import fileinput

# Attempt to connect with database
try:
    db = sqlite3.connect('some.db')
except sqlite3.Error as e:
    print("Unable to connect to database")

# Initialize column titles
cols = []

# Initialize rows
rows = []

# Reads csv file argument
with fileinput.input() as f:
    reader = csv.reader(f)
    try:
        cols = reader.__next__()
        filename = fileinput.filename()
        for row in reader:
            rows.append(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

c = db.cursor()

# Create table with data
tablename = filename.split('.')[0]
c.execute("CREATE TABLE IF NOT EXISTS " + tablename + " \
          (id INTEGER PRIMARY KEY AUTOINCREMENT, " + ",".join(cols) + ");")

query = "INSERT INTO " + tablename + "({0}) VALUES({1});\
        ".format(','.join(cols), ','.join('?' * len(cols)))

for row in rows:
    c.execute(query, row)

# Print summary of records
numrows = c.execute("SELECT COUNT(*) FROM " + tablename + ";")
count = c.fetchone()[0]
print(str(fileinput.lineno() - 1) +
      " records inserted, total records are " + str(count))

# Close database connection
db.commit()
db.close()
