from flask import Flask
from src.routes import set_routes

app = Flask(__name__)


set_routes(app)
