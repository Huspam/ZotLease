from flask import Flask, render_template, request
from api import *
import os
import psycopg2

app = Flask(__name__)
pg_conn_string = os.environ["PG_CONN_STRING"]
connection = psycopg2.connect(pg_conn_string)
cursor = connection.cursor()

@app.route("/", methods=['GET'])
def index():
    listings = get_data(connection, cursor)
    return render_template('index.html',listings=listings)

@app.route("/forms/enter", methods=['GET'])
def enter():
    communities = ['Arroyo Vista', 'Camino del Sol', 'Puerta del Sol', 'Plaza Verde', 'Plaza Verde II', 'Vista Del Campo', 'Vista Del Campo Norte']
    roomtypes = ['Single', 'Double', 'Quad']
    genders = ['Male', 'Female']
    leasetypes = ['Sublease', 'Sublet']
    startdates = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    enddates = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return render_template('listEntry.html', communities=communities, roomtypes=roomtypes, genders=genders, leasetypes=leasetypes, startdates=startdates, enddates=enddates)

@app.route("/listings/yourListings", methods=['GET'])
def pList():
    return render_template('personalList.html')

@app.route("/listings/savedListings", methods=['GET'])
def sList():
    return render_template('saveList.html')

@app.route("/listings", methods=['GET'])
def listing():
    return render_template('otherList.html')

@app.route("/forms/success", methods=['GET', 'POST'])
def add_listing():
    listing = [request.form.get(key) for key in request.form.keys()]
    insert_data(connection, cursor, *listing)
    return render_template('listSuccess.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    connection.close()