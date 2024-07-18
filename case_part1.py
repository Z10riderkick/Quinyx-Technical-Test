#import Flask

from flask import Flask, json, redirect, url_for, session
from requests import request

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.before_request
def index():
    if session['response'] == None:
        Jokes = []
        for i in range(10):
            Jokes.append(request('GET', "https://api.chucknorris.io/jokes/random/").json()["value"])
        session['response'] = Jokes

@app.route('/getjokes', methods= ['GET', 'POST'], endpoint = "getjokes")
def getjokes():
    Jokes = session['response']
    message = ""
    for i in Jokes:
        message = message + f'<li>{i}</li>'
    return message

if __name__ == "__main__":
    app.run()