from flask import Flask

app = Flask(__name__)
from app import views       #avoid circular reference with app



