from flask import Flask, render_template
from api import get_data
import os
import psycopg2
import json

app = Flask(__name__)
#add pg_conn_string as environment variable key
#postgresql://thzaw12264:dTnaXXnICWpFY0PfrW0q2g@coiled-drake-4885.6wr.cockroachlabs.cloud:26257/coiled-drake-4885.defaultdb is the value
#need to add verify ssl to connection string later
pg_conn_string = os.environ["PG_CONN_STRING"]
connection = psycopg2.connect(pg_conn_string)
cursor = connection.cursor()

@app.route("/", methods=['GET'])
def index():
    listings = get_data(connection, cursor)
    return render_template('index.html',listings=listings)

@app.route("/forms/vdc", methods=['GET'])
def vdc():
    return render_template('vdc.html')

@app.route("/forms/vdcn", methods=['GET'])
def vdcn():
    return render_template('vdcn.html')

@app.route("/forms/plaza", methods=['GET'])
def plaza():
    return render_template('plaza.html')

@app.route("/forms/puerta", methods=['GET'])
def puerta():
    return render_template('puerta.html')

@app.route("/forms/arroyo", methods=['GET'])
def arroyo():
    return render_template('arroyo.html')

@app.route("/listings/yourlistings", methods=['GET'])
def pList():
    return render_template('personalList.html')

@app.route("/listings/savedlistings", methods=['GET'])
def sList():
    return render_template('saveList.html')

@app.route("/listings", methods=['GET'])
def listing():
    return render_template('otherlisting.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')