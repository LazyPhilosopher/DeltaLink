from flask import Flask, render_template, Response
from config import Config							#configuration file declared (SECRET_KEY)

#print(__name__)
app = Flask(__name__)
app.config.from_object(Config)

from app import routes