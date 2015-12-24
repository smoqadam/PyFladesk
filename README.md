## PyFladesk
create desktop application by using Flask and QtWebKit 

## IDEA 

Rather than open Flask app in user browser, create a QWebview and then run Flask app on it.


## Notice 
I'm new to python and I'm going to improve my python knowledge. I was looking for new way to create desktop applications. Create this project for learning purpose. Maybe/surely my codes need to more improvements.
###### 
## How to use

add your routes in `routes.py`

ex: 

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
  
```
then run your desktop app 

`> python pyfladesk.py`


## Contributing

FEEL FREE TO TELL ME IF YOU SEE ANY MISTAKE OR NOTABLE THINGS BY OPENING A NEW ISSUE OR SENDING PULL REQUEST

## Thanks
Thanks to [Mathias Ettinger](http://codereview.stackexchange.com/users/84718/mathias-ettinger) for his [review](http://codereview.stackexchange.com/questions/114221/python-gui-by-qtwebkit-and-flask/114307#114307)
