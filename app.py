from flask import Flask
from gui import init_gui

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    init_gui(app)