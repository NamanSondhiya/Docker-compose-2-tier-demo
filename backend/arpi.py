from flask import Flask, jsonify
import os

arpi = Flask(__name__)

def load_games():
    with open('games.txt', 'r') as f:
        return f.readlines()

@arpi.route('/')
def index():
    return "Hello, From BaCkend!"

@arpi.route('/api')
def api():
    games = load_games()
    return jsonify({"games": games})

if __name__ == '__main__':
    arpi.run(port=8000, host='0.0.0.0', debug=True) 