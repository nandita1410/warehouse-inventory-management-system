from main import *
import sqlite3

#backend databse operations
class database():
    def conn(self):
        print("Database: connection method called")
        con= sqlite3.connect("inventory.db")
        cur = con.cursor()
        query= "CREATE TABLE IF NOT EXISTS Product (pid integer PRIMARY KEY, pname TEXT, price TEXT, qty TEXT, company TEXT, contact TEXT )"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database: connection method finished")
    def insert(self,pid, name,price, qty, company,contact):
        print("Database: insert method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query = "INSERT INTO Product Values(?,?,?,?,?,?)"
        cur.execute(query,(pid, name, price, qty, company,contact))
        con.commit()
        con.close()
        print("Databse: finished")

    def show(self):
        print("Database: show method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query= "SELECT * FROM Product"
        cur.execute(query)
        rows= cur.fetchall()
        con.close()
        print("Database finished\n")
        return rows

    def delete(self,pid):
        print("Database: delete method called",pid)
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute("DELETE FROM Product where pid=?",(pid,))
        con.commit()
        con.close()
        print(pid,"Datbase finished\n")

    def search(self,pid="",name="", price="", qty="", company="",contact=""):
        print("Database: search method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Product where pid=? or pname=? or price=? or qty=? or company=? or contact=?",(pid, name,price,qty,company,contact))
        row= cur.fetchall()
        con.close()
        print(pid,"Database finished\n")
        return row

    def update(self,pid="",name="", price="", qty="", company="",contact=""):
        print("Database: search method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute("UPDATE Product set pid=? or pname=? or price=? or qty=? or company=? or contact=? where pid=?",(pid,name,price,qty,company,contact,pid))
        con.commit()
        con.close()
        print(pid,"databse finished\n")


