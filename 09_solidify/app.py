# import flask
from flask import Flask

# instantiate instance of Flask class
app = Flask(__name__)

# route 1: homepage
@app.route("/")
def herro():
    text = '''
    <h1 style='text-align: center;'>Hello Peeps!</h1>
    <br><br><form action="/static/index.html">
        <center><input type="submit" value="Click for Surprise!"/></center>
    </form>'''
    return text
