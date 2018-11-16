"""
Xiaojie(Aaron) Li
Softdev pd8
K26 -- Getting More REST
2018-11-15
"""

import json, urllib.request, os
from flask import Flask, render_template

app = Flask(__name__)

# root route displays all APIs
@app.route("/")
def home():
    return render_template("index.html")

# route for world population info
@app.route("/world")
def world():
    url = urllib.request.urlopen("http://api.population.io:80/1.0/countries")
    data = json.loads(url.read().decode())
    print(data["countries"])
    print("\n\n------------------------------------")
    print(data["countries"][2])
    countries = data["countries"]
    # for i in range(0, 3):
    #     countries.remove(countries.index("Less developed"))
    # print(countries)
    return render_template('api_1.html', countries = data["countries"])

# route for quote of the day
@app.route("/quotes")
def quotes():
    url = urllib.request.urlopen("https://favqs.com/api/qotd")
    data = json.loads(url.read().decode())
    print(data["quote"])
    data = data["quote"]
    print(data["author"])
    print(data["body"])
    return render_template("api_2.html", author = data["author"], body = data["body"])

# route for pupper
@app.route("/pupperino")
def doggy():
    url = urllib.request.urlopen("https://dog.ceo/api/breeds/image/random")
    data = json.loads(url.read().decode())
    print("\n\n___________________________________________________")
    print(data["message"])
    return render_template("api_3.html", img = data["message"])

if __name__ == "__main__":
    app.run(debug = True)
