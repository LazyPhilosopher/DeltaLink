from flask import Flask, render_template, Response
from config import Config							#configuration file declared (SECRET_KEY)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#print(__name__)
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)						# database
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models