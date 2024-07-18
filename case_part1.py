#import Flask
from flask import Flask
from requests import request

app = Flask(__name__)

@app.route('/')
def index():
    response = request('GET', "https://api.chucknorris.io/jokes/random/")
    return response.json()["value"]

if __name__ == "__main__":
    app.run()