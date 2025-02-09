from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

api_key = os.environ['API-KEY']
app = Flask(__name__)
app.config['SECRET_KEY'] = api_key

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User,user_id)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/index.html')
def home():
    if current_user.is_authenticated:
        return render_template("index.html",name=current_user.name,is_auth = current_user.is_authenticated)
    return render_template("index.html",is_auth = current_user.is_authenticated)

@app.route('/register',methods=["GET","POST"])
def register():
    if request.method == "POST":
        hash_and_salted_password = generate_password_hash(
            request.form.get("password"),
            method="pbkdf2:sha256",
            salt_length=8
        )
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hash_and_salted_password,
        )
        user = db.session.execute(db.select(User).where(User.email == new_user.email)).scalar()
        if user:
            return render_template("register.html",is_auth=current_user.is_authenticated,warning=True)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("register.html",is_auth=current_user.is_authenticated)



@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if check_password_hash(user.password,password):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            return render_template("login.html",warning=True,is_auth = current_user.is_authenticated)
    return render_template("login.html", is_auth = current_user.is_authenticated)

@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html",name=current_user.name,is_auth = current_user.is_authenticated)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download', methods=["GET",'POST'])
@login_required
def download():

    return send_from_directory('static', path="files/cheat_sheet.pdf")



if __name__ == "__main__":
    app.run(debug=True,port=5001)
