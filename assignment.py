import sqlite3

conn = sqlite3.connect('assignment.db')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileName( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_fileName TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_fileName(col_fileName) VALUES (?)", \
                ('information.docx',))
    cur.execute("INSERT INTO tbl_fileName(col_fileName) VALUES(?)", \
                ('Hello.txt',))
    cur.execute("INSERT INTO tbl_fileName(col_fileName) VALUES(?)", \
                ('myImage.png',))
    cur.execute("INSERT INTO tbl_fileName(col_fileName) VALUES(?)", \
                ('myMovie.mpg',))
    cur.execute("INSERT INTO tbl_fileName(col_fileName) VALUES(?)", \
                ('World.txt',))
    cur.execute("INSERT INTO tbl_fileName(col_fileName) VALUES(?)", \
                ('data.pdf',))
    cur.execute("INSERT INTO tbl_fileName(col_fileName) VALUES(?)", \
                ('myPhoto.jpg',))
    conn.commit()
conn.close()

                
conn = sqlite3.connect('assignment.db')


with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fileName FROM tbl_fileName  WHERE col_fileName LIKE  '%.txt'")
    FileList = cur.fetchall()
    for item in FileList:
        msg = "File Name: {}".format(item)
        print(msg)
                

            
                
                
        

