## PyFladesk
create desktop application by using Flask and QtWebKit 

## IDEA 

Rather than open Flask app in user browser, create a QWebview and then run Flask app on it.

## Prerequisites
 - Python3
 - Flask
 - PyQt5

## How to use

1. Download or clone the project
2. Add your routes in `routes.py`

ex: 

```python
 from flask import render_template
 from app import app
 
 @app.route('/')
 def index():
     return render_template('index.html')
 
 @app.route('/page2')
 def page2():
     return render_template('page2.html')
  
```
3. Run `app.py` 

`> python3 app.py`

#### Sample RSS Reader app

I wrote a sample Rss reader app by PyFladesk. you can find it [here](https://github.com/smoqadam/PyFladesk-rss-reader).


## Contributing

FEEL FREE TO TELL ME IF YOU SEE ANY MISTAKE OR NOTABLE THINGS BY OPENING A NEW ISSUE OR SENDING A PULL REQUEST

## Thanks
Thanks to [Mathias Ettinger](http://codereview.stackexchange.com/users/84718/mathias-ettinger) for his [review](http://codereview.stackexchange.com/questions/114221/python-gui-by-qtwebkit-and-flask/114307#114307)
