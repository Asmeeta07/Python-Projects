from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr = user))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    return "<h1>{}</h1>".format(usr)


if __name__ == "__main__":
    app.run(debug=True)