import sqlite3
import numpy as np

conn = sqlite3.connect('mydatabase2.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Professor;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Department;
DROP TABLE IF EXISTS MemberSC;
DROP TABLE IF EXISTS MemberPC;

CREATE TABLE Department(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);
      
CREATE TABLE Student(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT NOT NULL,
    roll   INTIGER UNIQUE NOT NULL,
    dob INTIGER,
    gender TEXT  
);
CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT NOT NULL,
    code   TEXT UNIQUE NOT NULL,
    dept_id INTIGER
);
CREATE TABLE MemberSC(
    student_id     INTEGER,
    course_id   INTEGER,
    PRIMARY KEY (student_id, course_id)
);
CREATE TABLE Professor(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT NOT NULL,
    hindex   INTIGER,
    position TEXT
);
CREATE TABLE MemberPC(
    professor_id     INTEGER,
    course_id   INTEGER,
    PRIMARY KEY (professor_id, course_id)
);                    
''')




def addstudent():
    n = input("Enter the name: ")
    r = int(input("Enter the roll number: "))
    d = int(input("Enter Date of Birth in YYYYMMDD format: "))
    g = input("Enter M for Male or F for Female: ")
    if g!='M' or g!='F':
        g = 'U'
    cur.execute('''INSERT OR IGNORE INTO Student (name, roll, dob, gender)
        VALUES ( ?, ?, ?, ? )''', ( n,r,d,g ) )
    conn.commit()
    return

def adddept():
    n = input("Enter the name of the Department: ")
    cur.execute('''INSERT OR IGNORE INTO Department (name)
        VALUES(?)''', (n,))
    conn.commit()
    return

def addcourse():
    n = input("Enter the course name: ")
    c = input("Enter the course code: ")
    d = input("Enter department name: ")
    cur.execute('SELECT count(*) FROM Department WHERE name = ?',(d,))
    a = cur.fetchone()[0]
    if a==0:
        print("Department Not Found. Adding Department.")
        adddept()
    cur.execute('''SELECT id FROM Department WHERE name = ?''',(d,))
    a = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Course (name, code, dept_id)
        VALUES ( ?, ?, ? )''', ( n,c,a ) )
    conn.commit()
    return

def addprofessor():
    n = input("Enter the name: ")
    h = int(input("Enter the hindex: "))
    p = input("Enter the position: ")
    cur.execute('''INSERT OR IGNORE INTO Professor (name, hindex, position)
        VALUES ( ?, ?, ? )''', ( n,h,p ) )
    conn.commit()
    return

def enrollprof():
    n = input("Enter your name: ")
    cur.execute('''SELECT id FROM Professor WHERE name = ?''',(n,))
    a = cur.fetchone()[0]
    n = int(input("Enter Course Code: "))
    cur.execute('''SELECT id FROM Course WHERE code = ?''',(n,))
    b = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO MemberPC (professor_id, course_id)
        VALUES ( ?, ? )''', ( a,b ) )
    conn.commit()
    return

def enrollstudent():
    n = input("Enter your name: ")
    cur.execute('''SELECT id FROM Student WHERE name = ?''',(n,))
    a = cur.fetchone()[0]
    n = int(input("Enter Course Code: "))
    cur.execute('''SELECT id FROM Course WHERE code = ?''',(n,))
    b = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO MemberSC (student_id, course_id)
        VALUES ( ?, ? )''', ( a,b ) )
    conn.commit()
    return





    
    
