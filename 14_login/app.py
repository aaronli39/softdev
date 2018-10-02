'''
Xiaojie(Aaron) Li
SoftDev1 pd6
K14 -- Do I Know You?
2018-10-01
'''

# import all the stuffs
from flask import Flask, render_template, request, url_for, session, redirect
import os

# instantiate 
app = Flask(__name__)

app.secret_key = os.urandom(32)

@app.route("/")
def index() :
    print(app.secret_key)
    print(request.method)
    if "username" in session:
        return render_template("welcome.html", username = session["username"])
    else:
        return render_template("login.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST" and request.form["username"] == "c00lman" and request.form["password"] == "c00lpass":
        session["username"] = "c00lman"
        return redirect(url_for("index"))
    else:
        if request.form["username"] != "c00lman":
            problem = "username"
        else:
            problem = "password"
        return render_template("error.html", problem = problem)

@app.route("/drop")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)
