from flask import Flask, redirect, render_template, session, request, url_for
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "User_secret"
app.permanent_session_lifetime = timedelta(minutes= 5)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user", usr = user))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return "<h1> Login Successful for {}!!</h1>".format(user)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect((url_for("login")))



if __name__ == "__main__":
    app.run(debug=True)

