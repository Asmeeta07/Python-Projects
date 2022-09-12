from flask import Flask, redirect,url_for

app = Flask(__name__)

#define the pages on the website

@app.route("/")    #decorator that tells flask where to go to run this func
def home():
    return "Hello this is the main page <h1>Hello<h1>"

#another page
@app.route("/<name>")
def user(name):
    return "Hello {}!".format(name)

#redirect different pages from home
@app.route("/admin")
def admin():
    return redirect((url_for("home")))  #we have to mention the "home" function

#redirect to specific function that take argument
@app.route("/FAQ")
def FAQ():
    return redirect(url_for("user",name = "Friend!"))


if __name__ == "__main__":
    app.run(debug=True)
