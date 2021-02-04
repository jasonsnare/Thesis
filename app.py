from flask import Flask, render_template, request, jsonify
from execute_ou import predictOverUnder
from execute_spread import predictSpread

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/overunder', methods=['GET', 'POST'])
def overunder():
    return render_template('overunder.html')

@app.route('/spread', methods=['GET', 'POST'])
def spread():
    return render_template('spread.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
    name = request.form['name']
    email = request.form['email']
    pred = predictOverUnder(email, name)
    pred = str(pred)
    return jsonify({'name' : pred})

@app.route('/process1', methods=['POST', 'GET'])
def process1():
    name = request.form['name']
    email = request.form['email']
    pred = predictSpread(email, name)
    pred = str(pred)
    return jsonify({'name' : pred})

if __name__ == "__main__":
    app.run()