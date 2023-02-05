from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/vdc", methods=['GET'])
def vdc():
    return render_template('vdc.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')