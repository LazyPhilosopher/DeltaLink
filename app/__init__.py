from flask import Flask, render_template, Response

#print(__name__)
app = Flask(__name__)

from app import routes