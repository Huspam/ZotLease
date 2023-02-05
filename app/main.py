from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

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