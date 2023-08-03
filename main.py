# This is a sample Python script.

from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/next')
def next_page():
    return render_template('next_page.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask API!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run()