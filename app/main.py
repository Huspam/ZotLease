from flask import Flask, render_template, request
from api import *
import os
import psycopg2
import json

app = Flask(__name__)
pg_conn_string = os.environ["PG_CONN_STRING"]
connection = psycopg2.connect(pg_conn_string)
cursor = connection.cursor()

# insert_data(connection,cursor, 'VDC', 'Quad', 'Male', 62714, 'Sublet', 'February', 'June', 1004, 'Hi, please message me if interested!')
# get_data(connection,cursor)

@app.route("/", methods=['GET'])
def index():
    listings = get_data(connection, cursor)
    return render_template('index.html',listings=listings)

@app.route("/forms/vdc", methods=['GET', 'POST'])
def vdc():
    communities = ['Arroyo Vista', 'Camino del Sol', 'Puerta del Sol', 'Plaza Verde', 'Plaza Verde II', 'Vista Del Campo', 'Vista Del Campo Norte']
    roomtypes = ['Single', 'Double', 'Quad']
    genders = ['Male', 'Female']
    #unit
    leasetypes = ['Sublease', 'Sublet']
    startdates = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    enddates = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    #price
    #description
    return render_template('vdc.html', communities=communities, roomtypes=roomtypes, genders=genders, leasetypes=leasetypes, startdates=startdates, enddates=enddates)

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

@app.route("/forms/success", methods=['GET', 'POST'])
def add_listing():
    listing = [request.form.get(key) for key in request.form.keys()]
    insert_data(connection, cursor, *listing)
    return render_template('listingsuccess.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    connection.close()