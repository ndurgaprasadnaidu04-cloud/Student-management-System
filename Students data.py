import sqlite3

def setup():
    conn=sqlite3.connect("student.db")
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students(
                   student_name TEXT,
                   student_age INTEGER,
                   student_grade TEXT)''')
    conn.commit()
    conn.close()
def add_student():
    conn=sqlite3.connect("student.db")
    cursor=conn.cursor()
    student_name=input("enter the student name :")
    student_age=int(input("enter the age of the student :"))
    student_grade=input("enter the student grade :")
    cursor.execute('''INSERT INTO students(student_name,student_age,student_grade)values(?,?,?)''',
                   (student_name,student_age,student_grade))
    conn.commit()
    conn.close()
def view_data():
    conn=sqlite3.connect("student.db")
    cursor=conn.cursor()
    cursor.execute('''SELECT * FROM students''')
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
setup()
while True:
    print('-----menu-------')
    print('1-add students data')
    print('2-view data')
    print('3-exit')
    choice=int(input("enter the service :"))
    if choice==1:
        add_student()
    elif choice==2:
        view_data()
    elif choice==3:
        break
    else:
        print("inavlid input")

