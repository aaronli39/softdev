from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    print("app name:")
    print(app)
    return render_template("test.html")

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return "wwwaaHHH wooOO"

if __name__ == "__main__":
    app.debug = True
    app.run()

    
