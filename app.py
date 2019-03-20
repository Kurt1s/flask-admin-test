from flask import Flask, render_template
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
# from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

# set optional bootswatch theme
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/kurtis/SoftEng/flask-admin-test/admin.db'
app.config['SECRET_KEY'] = 'mysecret'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# DB initialization
db = SQLAlchemy(app)

#ORM Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())


@app.route("/")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")



# Flask and Flask-SQLAlchemy initialization here
admin = Admin(app, name='Flask-Admin', template_mode='bootstrap3')

admin.add_view(ModelView(User, db.session))

if __name__ == '__main__':
    app.run(debug=True)