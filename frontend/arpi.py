from flask import Flask, render_template, jsonify
import requests

arpi = Flask(__name__)

BACKEND_URL = 'http://backend:8000'

@arpi.route('/')
def index():
    return render_template('index.html')

@arpi.route('/api')
def api():
    response = requests.get(f'{BACKEND_URL}/api')
    return response.json()

if __name__ == '__main__':
    arpi.run(port=8001, host='0.0.0.0', debug=True)