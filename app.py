from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("home")) # integrate with login page

@app.route("/home")
def home():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)