'''
Xiaojie(Aaron) Li
SoftDev1 pd6
K08 -- Fill Yer Flask
2018-09-19
'''

# import flask
from flask import Flask

# instantiate instance of Flask class
app = Flask(__name__)

# route 1: homepage
@app.route("/")
def herro():
    text = '''
    <h1 style='text-align: center;'>Hello World!</h1>
    <p style='text-align: center'>Welcome to Aaron's Webpage!</p>
    <br><br><form action="/about">
        <center><input type="submit" value="About Aaron"/></center>
    </form>
    <form action="/info">
        <center><input type="submit" value="About this HW"/></center>
    </form>
    '''
    return text

# route 2: a page about Aaron <--- ME!!!
@app.route("/about")
def aaron():
    text = '''
    <h1 style='text-align: center'>Aaron is siMplY amAzYiNG</h1>
    <br><br><form action="/">
        <center><input type="submit" value="Homepage"/></center>
    </form>
    '''
    return text

# route 3: a page with a question...
@app.route("/info")
def hw():
    text = '''
    <h1 style='text-align: center'>Can I Flask You Something?</h1>
    <br><br><form action="/">
        <center><input type="submit" value="Homepage"/></center>
    </form>
    '''
    return text

# I use $flask run so I do not need to do app.run()
