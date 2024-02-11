import sqlite3
import global_var

def createDb():
    try:
        conn=sqlite3.connect("grid.db")
        cursor=conn.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS GRID(
                        id INTEGER  PRIMARY KEY,
                        val INTEGER NOT NULL)''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("SQL lite error: ", e)

def store(TwoDArray):
    try:
        conn = sqlite3.connect("grid.db")
        cursor = conn.cursor()
        #cursor.execute('INSERT INTO GRID(id, val) VALUES(?,?)', ("00", TwoDArray[0][0]))
        for i in range(0,len(TwoDArray)):
            for j in range(0,len(TwoDArray)):
                print(TwoDArray[i][j])
                s=f"{i}{j}"
                cursor.execute('INSERT INTO GRID(id, val) VALUES(?,?)',(s,TwoDArray[i][j]))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("SQL lite error: ", e)

def retrive():
    try:
        conn = sqlite3.connect("grid.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM GRID")
        DATA=cursor.fetchall()
        for row in DATA:
            print(row)
        conn.close()
    except sqlite3.Error as e:
        print("SQL lite error: ", e)

def update(index,val):
    try:
        conn = sqlite3.connect("grid.db")
        cursor = conn.cursor()
        data=(val, index)
        cursor.execute('UPDATE  GRID SET val = ? WHERE id=?',data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("SQL lite error: ", e)


