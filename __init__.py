from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)


app.config['SECRET_KEY'] = 'c8c4a40898f5b9e8e7022f9f34556a4d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///primeiro.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça o login para acessar esta página'
login_manager.login_message_category = 'alert-info'


from primeirositeflask import routes
