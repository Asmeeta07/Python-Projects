from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

#render html templates

@app.route("/")
def home():
    return "Hello"

#show dynamic information on the screen
#display the user name in the home page
#pass a list

@app.route("/<name>")
def user(name):
    return render_template("index.html",content = name, mylist = ["Jubi", "Maina","Mamu"])




if __name__ == "__main__":
    app.run()