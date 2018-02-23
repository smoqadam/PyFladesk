## PyFladesk
Create desktop application by using Flask and QtWebKit 

## Idea

Rather than open Flask app in user browser, create a QWebview and then run Flask app on it.

By default, every internal link is open inside the app and every external link is open in the default browser.

## Dependencies

- Python3
- Flask
- PyQt

Note: Some releases require Conda to properly create a virtual environment

## Versions

There are 3 available versions:

- [PyQt4](https://github.com/smoqadam/PyFladesk/releases/tag/0.1)
- [PyQt5.6](https://github.com/smoqadam/PyFladesk/releases/tag/0.2)
- [PyQt5.10](https://github.com/smoqadam/PyFladesk/releases/tag/1.0)

Note: Both PyQt4 and PyQt5.6 are only made available for compatibility reasons, there is no intention to keep them updated unless requested

## Usage

### New Flask App

1. Download the [lastest release](https://github.com/smoqadam/PyFladesk/releases) and extract it
2. Add your routes in `routes.py`

Example:

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

Linux:
`> python3 app.py`

Windows:
`> python app.py`

### Existing Flask App

1. Check dependences of your project and choose a branch accordingly
2. Download the gui.py 
3. Replace `app.run` with `init_gui(app)`

## Packaging

If you need to deliver your app as an executable file or in a compact folder you can use [PyInstaller](http://www.pyinstaller.org/)

This avoids the need for the Python interpreter and the packages you use inside your project

If you haven't already, install it with pip (if you use virtual environments you should install it inside it)

`pip install pyinstaller`

Some parameters to consider:

- `F` - Bundles everything in a single file
- `w` - Avoid displaying a console
- `--add-data` - Add Folders to the directory/executable

Since Flask relies on a directory structure you should pass it to the folder, in the example case we only have two folders: `templates` and `static`, in case you use a database or some other directory structure you should adapt this.

Note: For more complex scenarios check the [PyInstaller Docs](https://pythonhosted.org/PyInstaller/usage.html)

If we want everything in one executable file we can

Windows: `pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" app.py`

Linux: `pyinstaller -w -F --add-data "templates:templates" --add-data "static:static" app.py` (NOT TESTED)

This will create a folder `dist` with our executable ready to be shipped. The executable will open the main window of our app.

Since Qt is quite big, your executables will be big too. The example app of this repository is 70 MB (69 MB of which are the Qt Component for displaying HTML). This is reasonable taking into account that we are shipping a self contain web browser.

## Sample apps
List of apps which make by PyFladesk.
 
 - [RSS Reader](https://github.com/smoqadam/PyFladesk-rss-reader)


## Contributing Oportunities

Feel free to open issues and pull requests for new features and improvements. This is a guide for things that may be useful for the project:

- Add different backends (wxPython, TKinter, etc)
- Test performance of HTML5 and CSS3
- Add Directory structure for large projects (Flask Patterns)
- Test other micro web frameworks (Bottle, etc)
- Make sample apps

## Thanks
Thanks to [Mathias Ettinger](http://codereview.stackexchange.com/users/84718/mathias-ettinger) for his reviews, one [for the old code](https://codereview.stackexchange.com/a/114307/161364) and one [for the new one](https://codereview.stackexchange.com/a/188124/161364)
