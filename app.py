from flask import Flask, render_template, url_for, redirect, request, session

app = Flask(__name__)
app.secret_key = "jsdklfj"

@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))
    


@app.route("/home")
def home():
    if "username" in session:
        return render_template("home.html", username = session["username"])
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if "username" in session:
        return redirect(url_for("home"))
    else:
        if request.method == "POST":
            session["username"] = request.form["username"]
            session.permanent = True
            return redirect(url_for("home"))
        else:
            return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)
