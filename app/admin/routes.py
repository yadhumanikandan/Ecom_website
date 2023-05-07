from flask import Blueprint, render_template, redirect, url_for, request, session
# from app import db
# from app.models import admin


# Defining a blueprint
admin_bp = Blueprint('admin_bp', __name__, template_folder='templates', static_folder='static')



# think of a way to impliment admin authentication



# admin session should not be permanent
@admin_bp.route("/")
def admin_index():
    return redirect(url_for("admin_bp.admin_login"))



@admin_bp.route("/login", methods=["POST", "GET"])
def admin_login():
    if request.method == "POST":
        return "<h1>admin</h1>"
    else:
        return render_template("admin_login.html")
    


@admin_bp.route("/home")
def admin_home():
    return render_template("admin_home.html")
