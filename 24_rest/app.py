from flask import Flask, render_template
from util import num
import json, urllib.request, os

# instantiate flask app
app = Flask(__name__)

# make secret key
app.secret_key = os.urandom(32);

# definte index route
@app.route("/")
def index():
    # get a link with random date
    link = num.main()

    # try opening the url(because some dates might not work)
    try:
        url = urllib.request.urlopen(link)
        data = json.loads(url.read().decode())
    except: # if error, use the definite function
        link = num.definite()
        data = json.loads(urllib.request.urlopen(link).read().decode())
        temp = False
    print(link)
    print(data)
    return render_template("index.html", date = data['date'], img = data["url"], explan = data["explanation"])

# run flask
if __name__ == "__main__":
    app.run(debug = True)
