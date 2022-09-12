from flask import Flask, redirect, render_template, session, request, url_for, flash
from datetime import timedelta
import sqlite3 as sql


app = Flask(__name__)
app.secret_key = "User_secret"
app.permanent_session_lifetime = timedelta(minutes= 5)

connection = sql.connect('user.db')
cur = connection.cursor()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        cur.execute("""SELECT name
                           FROM users
                           WHERE name=?""",
                    (user,))

        found_usr = cur.fetchone()

        if found_usr:
            print("The id of the user".format(found_usr[0]))
            session["email"] = found_usr[2]

`
        flash("Login Successful", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user", methods = ["POST","GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved", "info")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", user = user, email=email)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash("You have been logged out, {}".format(user), "info")
    else:
        flash("Please login first!", "info")
    session.pop("user", None)
    session.pop("email", None)

    return redirect((url_for("login")))



if __name__ == "__main__":
    app.run(debug=True)


