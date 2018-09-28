from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    print("app name:")
    print(app)
    return render_template("test.html")

@app.route("/greetings", methods = ["POST"])
def greet():
    print(request.method)
    print(request.form)
    name = request.form["user"]
    method = request.method
    return render_template("greet.html", name = name, method = method)

if __name__ == "__main__":
    app.debug = True
    app.run()
