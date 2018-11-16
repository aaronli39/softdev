
import json, urllib.request, os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

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

if __name__ == "__main__":
    app.run(debug = True)
