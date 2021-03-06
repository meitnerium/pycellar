import tkinter as tk
import os
import sqlite3
from sqlite3 import Error

class Mywine():
    def __init__(self):
        self.dbfile = "mywine.db"
        if os.path.isfile(self.dbfile):
            print("File exist")
        else:
            self.createdb()

    def create_connection(self,db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file, timeout=30)
            return conn
        except Error as e:
            print(e)

        return conn
# je dois ajouter la location et la souslocation, date ajout
    def createdb(self):
        sql_create_wines_table = """ CREATE TABLE IF NOT EXISTS mywines (
                                            id integer PRIMARY KEY,
                                            qte integer,
                                            barcode integer
                                        );

                                 """
        conn = self.create_connection(self.dbfile)
        try:
            c = conn.cursor()
            c.execute(sql_create_wines_table)
        except Error as e:
            print(e)
        conn.close()

#TODO verifier que le vin (barcode) n'existe pas deja dans la db
    def add_wine(self,barcode):
        """
        Create a new task
        :param conn:
        :param task:
        :return:
        """
        print("barcode")
        print(barcode)
        sql = ''' INSERT INTO mywines (qte,barcode)
                  VALUES(?,?) '''
        conn = self.create_connection(self.dbfile)
        cur = conn.cursor()
        data = ('1', barcode)
        cur.execute(sql, data )
        #cur.execute(sql, 12345)
        conn.commit()
        conn.close()
        return cur.lastrowid

mywine = Mywine()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.data = tk.Text(self)
        self.data.pack(side="top")
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Add wine"
        self.hi_there["command"] = self.add_wine
        self.hi_there.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def add_wine(self):
        wines = self.data.get("1.0",tk.END)
        for wine in wines.split():
            print("test")
            print(wine)
            mywine.add_wine(str(wine))

        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
