import flask, os, mysql.connector
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
=======
from flask_login import LoginManager
from flask_admin import Admin
from flask_bcrypt import Bcrypt

<<<<<<< HEAD
>>>>>>> parent of 7a83369... Didn't change too much stuff. The links to the sections weren't working and that was becasue the names of the sections had spaces in them so i decided to use the item id instead
=======
>>>>>>> parent of 7a83369... Didn't change too much stuff. The links to the sections weren't working and that was becasue the names of the sections had spaces in them so i decided to use the item id instead
app = flask.Flask(__name__)

SECRET_KEY = os.urandom(32)
app.secret_key = SECRET_KEY

db = mysql.connector.connect(
    host="104.168.136.69",
    user="yscbtlcv_cwkchi5781",
    password="singlebird5781!",
    database="BTSTRIVIA"
)

<<<<<<< HEAD
cursor = db.cursor()
=======
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

admin = Admin(app)

login_manager = LoginManager(app)
login_manager.login_view = 'Login'
login_manager.login_message_category = 'info'
>>>>>>> parent of 7a83369... Didn't change too much stuff. The links to the sections weren't working and that was becasue the names of the sections had spaces in them so i decided to use the item id instead

from main import routes

