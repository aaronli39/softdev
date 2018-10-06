# Team DhataBhases: Xiaojie(Aaron) Li, Sophia Xia
# SoftDev1 pd8
# K16 -- No Trouble
# 2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
# build SQL stmt, save as string
command = """
CREATE TABLE students(
    name TEXT,
    age INTEGER,
    id INTEGER)
"""
c.execute(command)    #run SQL statement
num_peeps = 0
# populate sql table for peeps.csv
with open("peeps.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        num_peeps += 1
        command = "INSERT INTO students(name, age, id) VALUES('" + row['name'] + "', " + row['age'] + ", " + row['id'] + ");"
        c.execute(command)

# create courses table
command = """
CREATE TABLE courses(
    code TEXT,
    mark INTEGER,
    id INTEGER)
"""
c.execute(command)    #run SQL statement

# populate sql table for courses.csv
with open("courses.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        command = "INSERT INTO courses(code, mark, id) VALUES('" + row['code'] + "', " + row['mark'] + ", " + row['id'] + ");"
        c.execute(command)

# create average table
command = """
CREATE TABLE averages(
    name TEXT,
    oasis INTEGER,
    average REAL)
"""
c.execute(command)    #run SQL statement
command = """
SELECT name, students.id, mark FROM students, courses
WHERE students.id = courses.id
"""
c.execute(command)
avg = c.fetchall()
print(avg)
current = avg[0][0]
sum = 0
count = 0
for i in avg:
    if i[0] == current:
        sum += i[2]
        count += 1
    else:
        print("sum: " + str(sum))
        print(str(sum/count) + " " + i[0])
        current = i[0]
        sum = i[2]
        count = 1
#==========================================================

db.commit() #save changes
db.close()  #close database
