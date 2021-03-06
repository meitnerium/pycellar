import sqlite3
from sqlite3 import Error




def create_connection(db_file):
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

def add_wine(wine):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO wines(name,achat_date,prix_achat,saqid,qte,millesisme)
              VALUES(?,?,?,?,?,?) '''
    conn = create_connection(r"pythonsqlite.db")
    cur = conn.cursor()
    print(wine)
    cur.execute(sql, wine)
    conn.commit()
    conn.close()
    return cur.lastrowid

sql_create_wines_table = """ CREATE TABLE IF NOT EXISTS wines (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    achat_date text,
                                    prix_achat text,
                                    saqid integer,
                                    qte integer,
                                    millesisme integer
                                );

                         """


def create_table(create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    conn = create_connection(r"pythonsqlite.db")
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    conn.close()

#if conn is not None:
    # create projects table
create_table(sql_create_wines_table)
wine1= ('Kendall-Jackson Chardonnay Vintners Reserve','2020-02-19','18.85',13298379,2,2017)
wine2= ('Chateau Clarke Listrac-Medoc','2020-02-19','39.85',10677550,2,2015)
wine3= ('William Fevre Chablis Les Champs Royaux','2020-02-19','39.85',10677550,3,2017)
wine4= ('J.Baumer Riesling','2020-02-19','16.85',10677550,2,2018)
wine5= ('Champagne Leclerc','2020-02-19','38.00',11111111,3,1900)
wine6= ('Colleziore','2020-02-19','13.00',11111111,1,2017)
wine7= ('Louderne','2020-02-19','1.00',11111111,3,1900)
wine8= ('Louderne','2020-02-19','1.00',11111111,3,1900)
wine9= ('Rocato','2020-02-19','45.00',11111111,2,1900)
wine10= ('Carpineto','2020-02-19','19.00',11111111,2,1900)
wine11= ('Farnito','2020-02-19','29.00',11111111,2,1900)
wine12= ('St-Thomas','2020-02-19','26.15',927830,3,2017)
#if conn is not None:
    # create projects table
add_wine(wine1)
add_wine(wine2)
add_wine(wine3)
add_wine(wine4)
add_wine(wine5)
add_wine(wine6)
add_wine(wine7)
add_wine(wine8)
add_wine(wine9)
add_wine(wine10)
add_wine(wine11)
add_wine(wine12)