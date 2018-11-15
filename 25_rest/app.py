"""
Xiaojie(Aaron) Li
Softdev pd8
K25 -- Getting More REST
2018-11-14
"""

import json, os, random, requests
from flask import Flask, render_template

# instantiate flask app
app = Flask(__name__)

# make secret key
app.secret_key = os.urandom(32);

# definte index route
@app.route("/")
def index():
    url = 'http://api.repo.nypl.org/api/v1/items/search?q=dog&publicDomainOnly=true&per_page=50'
    auth = 'Token token=zl38cqpmx6e79xp1'
    call = requests.get(url, headers={'Authorization': auth})
    # url = urllib.request.urlopen("http://aaronli39:aaronli39@api.repo.nypl.org/api/v1/items/search?q=dog&publicDomainOnly=true&per_page=50")
    data = call.json()
    print("\n\n______________________________________________________________________________")
    print(data.get('nyplAPI').get('response').get('result')[random.randint(0,48)]['itemLink'])
    print("\n\n______________________________________________________________________________")
    # print(data.get('nyplAPI').get('response').get('result').get(str(random.randint(1,49))))

    info = data.get('nyplAPI').get('response').get('result')[random.randint(0,48)]

    return render_template("index.html", title = info['title'], date = info['dateDigitized'][:10], img = info['itemLink'], explan = info['rightsStatement'])

# run flask
if __name__ == "__main__":
    app.run(debug = True)
