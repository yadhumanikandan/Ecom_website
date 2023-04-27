from flask import render_template, session, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from app.models import users

from app.admin.routes import admin_bp


app.register_blueprint(admin_bp, url_prefix='/admin')



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
        

@app.route("/home")
def home():
    #check if user alreasy logged in
    if "email" in session:
        return render_template("home.html", email = session["email"])
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



@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
