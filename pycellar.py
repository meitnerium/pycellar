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




#if conn is not None:
    # create projects table
create_table(sql_create_wines_table)

#else:
#    print("Error! cannot create the database connection.")



#else:
#    print("Error! cannot create the database connection.")

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
#app = dash.Dash()

import requests

#x = requests.get("https://www.saq.com/fr/13298379?q=13298379")
#print(x.text)

#app.layout = html.Div(children=[
#    html.H1(children='Cellar'),
#
#    html.Div(children=[
#    dash_table.DataTable(
#    id='table',
#    columns=["Name" , "id"],
#    data=['Vin1','1'],
#)])
#])


app = dash.Dash(__name__)

params = [
    'Name', 'qte','Millesime', 'Prix d\'achat'
]
value = []
def get_wines():
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = "SELECT * FROM wines"
    conn = create_connection(r"pythonsqlite.db")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    results = cur.fetchall()
    #print(results)
    return results



res = get_wines()
#print(res.count())
#print("TEST1")
numvin=0
for r in res:
    numvin=numvin+1
    print("TEST")
    print(r[1])
    value.append({'Name': r[1],
                  'qte': r[5],
                  'Millesime': r[6],
                  'Prix d\'achat': r[3]})
#value.append( {'Name' : 'Kendall-Jackson Chardonnay Vintners Reserve',
#               'qte' : 2,
#               'Millesime' : 2017,
#               'Prix d\'achat' : '18.85'}
#)

print("TTTTTTEEEEEEEESSSSSTTTTTTTTTTT")
print(len(res))
print(value[:])
app.layout = html.Div([
    dash_table.DataTable(
        id='table-editing-simple',
        columns=(
            [{'id': p, 'name': p} for p in params]
        ),
        data=[
            dict(Model=i, **{param: value[i][param] for param in params})
            for i in range(0, numvin)
        ],
        editable=True,
        sort_action = "native",
        row_selectable = "multi"
    ),
    dcc.Graph(id='table-editing-simple-output')
])

app.run_server(debug=True,host='127.0.0.1',port=8888)
