## PyFladesk
create desktop application by using Flask and QtWebKit 

## IDEA 

Rather than open Flask app in user browser, create a QWebview and then run Flask app on it.


## Notice 
I'm new to python and I'm looking for new way to create desktop applications. Create this project for learning purpose. Maybe/surely my codes need to more improvements.
###### PLEASE TELL ME IF YOU SEE ANY MISTAKE OR NOTABLE THINGS BY OPENING A NEW ISSUE AND SENDING PULL REQUEST
## How to use

add your routes in `routes.py`

ex: 

```python

from main import *


@app.route('/')
def index():      
	return '<a href="/about">About</a>' 

@app.route('/about')
def about():
  return '<h1>About</h1><a href="/">Home</a>'
  
```
then run your desktop app 

`> python main.py`

