from flask import Flask

print("__init__.py file started")
app = Flask(__name__)

from app import routes