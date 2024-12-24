from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"

@app.route('/api/data')
def get_data():
    response = requests.get('http://backend:8000/api/data')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
