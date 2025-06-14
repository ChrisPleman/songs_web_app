from flask import Flask
import json

with open('sensitive.json', 'r') as f:
    # Get the database credentials
    secret_keys = json.load(f)['secret_keys']

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_keys['SecretKey']

from routes import *

if __name__ == '__main__':
    app.run(debug=True)