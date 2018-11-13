from flask import Flask, render_template
import json, urllib.request, os

# instantiate flask app
app = Flask(__name__)

# make secret key
app.secret_key = os.urandom(32);

# definte index route
@app.route("/")
def index():
    with urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=fDt3yjMvHQXteTtvW2I68LVqNNJFXy2raPmyg7AX") as url:
        data = json.loads(url.read().decode())
        print(data)
    return render_template("index.html", img = data['url'])





# run flask
if __name__ == "__main__":
    app.run(debug = True)
