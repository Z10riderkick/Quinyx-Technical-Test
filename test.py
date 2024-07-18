from requests import request

response = request('GET', "https://api.chucknorris.io/jokes/random")
print(response.json()["value"])