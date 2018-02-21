from flask import Flask
from gui import provide_GUI_for

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    provide_GUI_for(app)