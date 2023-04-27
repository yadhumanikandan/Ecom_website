from flask import Flask, render_template, url_for, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "jsdklfj"


db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password_hash = db.Column(db.String(100))

    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash


######################################################################################
@app.route("/data")                                                                  #
def data():                                                                          #          delete
    return render_template("data.html", data = users.query.all())                    #
######################################################################################


@app.route("/")
def index():
    #check if user already in session
    if "email" in session:
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))
    

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        found_user = users.query.filter_by(email = request.form["email"]).first()
        #check if user already exist in database
        if found_user == None:
            #if user not exit
            session["username"] = request.form["username"]
            session["email"] = request.form["email"]
            session.permanent = True

            password_hash = generate_password_hash(request.form["password"])
            usr = users(session["username"], session["email"], password_hash)
            db.session.add(usr)
            db.session.commit()
            return redirect(url_for("home"))
        else:
            #if already exist
            return "<h1>user already exist</h1>"
    else:
        return render_template("register.html")

@app.route("/home")
def home():
    #check if user alreasy logged in
    if "email" in session:
        return render_template("home.html", email = session["email"])
    else:
        return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if "email" in session:
        return redirect(url_for("home"))
    else:
        if request.method == "POST":
            found_user = users.query.filter_by(email=request.form["email"]).first()
            if found_user == None: 
                return redirect(url_for("signup"))
            elif check_password_hash(found_user.password_hash, request.form["password"]):
                session["email"] = request.form["email"]
                session["username"] = found_user.username
                session.permanent = True
                return redirect(url_for("home"))
            else:
                return redirect(url_for("login"))
            
        else:
            return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))



if __name__ == "__main__":
    with app.app_context():
        db.create_all()   
    app.run(debug=True)
