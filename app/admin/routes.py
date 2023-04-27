from flask import Blueprint, render_template


# Defining a blueprint
admin_bp = Blueprint('admin_bp', __name__, template_folder='templates', static_folder='static')



@admin_bp.route('/')   # Focus here
def admin_home():
    return render_template("admin_home.html")