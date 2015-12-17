from main import *



@app.route('/')
def index():      
	#return 'hi' 
	return render_template('index.html')
