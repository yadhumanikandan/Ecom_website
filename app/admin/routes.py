from flask import Blueprint, render_template, redirect, url_for, request


# Defining a blueprint
admin_bp = Blueprint('admin_bp', __name__, template_folder='templates', static_folder='static')



@admin_bp.route("/")   # Focus here
def admin_home():
    return redirect(url_for("admin_bp.admin_login"))



@admin_bp.route("/login", methods=["POST", "GET"])
def admin_login():
    if request.method == "POST":
        return "<h1>admin</h1>"
    else:
        return render_template("admin_login.html")
    



