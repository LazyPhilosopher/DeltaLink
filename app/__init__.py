from flask import Flask, render_template, Response
from config import Config							#configuration file declared (SECRET_KEY)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#print(__name__)
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)						# database
migrate = Migrate(app, db)

from app import routes, models