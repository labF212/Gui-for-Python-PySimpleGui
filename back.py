import sqlite3

#criar base de dados
dbase = sqlite3.connect('employee_record.db')
c= dbase.cursor()
dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_records(
                  ID INT PRIMARY KEY NOT NULL,
                  NAME TEXT NOT NULL) ''')

#aplica as mudancas na db
dbase.commit()

def write(ID,NAME):
  c.execute('''INSERT into employee_records(ID,NAME) VALUES(?,?)''',(ID, NAME))
  dbase.commit()

def delete(x):
  c.execute('''delete from employee_records where NAME=?''',x)
  dbase.commit()

def read_task():
  c=dbase.cursor()
  c.execute('''SELECT NAME from employee_records''')
  data=c.fetchall()
  dbase.commit()
  return data