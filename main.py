from core.Core import *

app = Flask(__name__)

from routes import *



if __name__ == '__main__':
	main(app)