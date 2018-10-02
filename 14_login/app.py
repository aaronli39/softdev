'''
Xiaojie(Aaron) Li
SoftDev1 pd6
K14 -- Do I Know You?
2018-10-01
'''

# import all the stuffs
from flask import Flask, render_template, request, url_for, session, redirect
import os

# instantiate flask app
app = Flask(__name__)
# generate a random key for session
app.secret_key = os.urandom(32)

# first route is index
@app.route("/")
def index() :
    print(app.secret_key)
    print(request.method)
    # if user is logged in session, show welcome page with greeting
    if "username" in session:
        return render_template("welcome.html", username = session["username"])
    else:
        # otherwise show log in page
        return render_template("login.html")

# second route is for handling log in request
@app.route("/login", methods = ["GET", "POST"])
def login():
    # if username and password are correct, redirect to welcome page in index
    if request.method == "POST" and request.form["username"] == "c00lman" and request.form["password"] == "c00lpass":
        session["username"] = "c00lman"
        return redirect(url_for("index"))
    else:
        # otherwise, return error page with error
        if request.form["username"] != "c00lman":
            problem = "username"
        else:
            problem = "password"
        return render_template("error.html", problem = problem)

# third route handles logging out, just drop the session
@app.route("/drop")
def logout():
    session.pop("username", None)
    # redirect to log in page in index
    return redirect(url_for("index"))

# run flask
if __name__ == "__main__":
    app.run(debug = True)
