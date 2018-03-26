from sqlite3 import *

def conn():
    con=connect("books.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    con.commit()
    con.close()
conn()
def insert(title_text,author_text,year_text,isbn_text):
    con=connect("books.db")
    cur=con.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title_text,author_text,year_text,isbn_text))
    con.commit()
    con.close()
def view():
    con=connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    lis=cur.fetchall()
    #print(lis)
    con.close()
    return lis

def search(title_text="",author_text="",year_text="",isbn_text=""):
    con=connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title_text,author_text,year_text,isbn_text))
    lis=cur.fetchall()
    #print(lis)
    con.close()
    return lis

def delete(id):
    con=connect("books.db")
    cur=con.cursor()
    cur.execute("DELETE FROM book WHERE id=? ",(id,))
    con.commit()
    con.close()


def update(id,title_text,author_text,year_text,isbn_text):
    con=connect("books.db")
    cur=con.cursor()
    cur.execute("UPDATE book SET title=? , author=? , year=? , isbn=? WHERE id=?",(title_text,author_text,year_text,isbn_text,id))
    con.commit()
    con.close()

#insert("The Half","Chetan",2012,20125626)
#update(8,"the ha","chet","201544","9425110195")
#view()

#search("The Hal","JKIKBK",2012,"GJBJ")
