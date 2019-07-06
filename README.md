## PyFladesk

Create desktop application by using Flask and QtWebEngine.

## Idea

Rather than open Flask app in user browser, create a QWebview and then run Flask app on it.

By default, every internal link is open inside the app and every external link is open in the default browser.

## Dependencies

- Python3
- Flask
- PyQt

Note: Some releases require Conda to properly create a virtual environment.

## Versions

There are 3 available versions:

- [PyQt4 - Legacy](https://github.com/smoqadam/PyFladesk/releases/tag/0.1)
- [PyQt5.6 - Legacy](https://github.com/smoqadam/PyFladesk/releases/tag/0.2)
- [PyQt5.10](https://github.com/smoqadam/PyFladesk/releases/tag/1.0)

Note: Both PyQt4 and PyQt5.6 are only made available for compatibility reasons, there is no intention to keep them updated unless requested.

## Installation with pip

If you want to install PyFladesk with pip you just run.

`pip install pyfladesk`

Only the latest version (PyQt5.10) is uploaded to PyPI. If you want to use a legacy version check the instructions in the corresponding branch readme. Each version is maintained in a different form due to versions issues so you should check the readme of the branch of the version you want to use.

## No pip installation

In case you don't want to use pip or you want to use a freezed version of PyFladesk, just download the `__init__.py` file from the `pyfladesk` folder and place it in your project (change the name to pyfladesk.py), then you can follow the instructions below.

## Usage

You just need to change two lines:

Add an import at the top:

`from pyfladesk import init_gui`

And wherever you run the app (`app.run`) replace it with:

`init_gui(app)`

Then run your app as usual

### Example

```python
from flask import Flask
from pyfladesk import init_gui

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    init_gui(app)
```

## Parameters

The `init_gui` function has some optional parameters that you may find useful:

```python
init_gui(application, port=5000, width=300, height=400,
             window_title="PyFladesk", icon="appicon.png", argv=None)
```

- port: choose in which port the application will run.
- width: The initial width of the main window.
- height: The initial height of the main window.
- window_title: The main window title.
- icon: the path to the icon file of the main window.
- argv: additional parameters to the `QApplication` instance.

## Packaging

For a full guide on how to package the app in one executable with [PyInstaller](http://www.pyinstaller.org/) file check [this blog post](https://elc.github.io/posts/executable-flask-pyinstaller/)

This avoids the need for the Python interpreter and the packages you use inside your project.

If you haven't already, install it with pip (if you use virtual environments you should install it inside it).

`pip install pyinstaller`

Some parameters to consider:

- `F` - Bundles everything in a single file
- `w` - Avoid displaying a console
- `--add-data` - Add Folders to the directory/executable

Since Flask relies on a directory structure you should pass it to the folder, in the example case we only have two folders: `templates` and `static`, in case you use a database or some other directory structure you should adapt this.

Note: For more complex scenarios check the [PyInstaller Docs](https://pythonhosted.org/PyInstaller/usage.html)

If we want everything in one executable file we can

Windows:

`pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" app.py`

Linux:

`pyinstaller -w -F --add-data "templates:templates" --add-data "static:static" app.py`

Depending on the Linux version, you might need to install `sudo apt install libpython3.x-dev`

This will create a folder `dist` with our executable ready to be shipped. The executable will open the main window of our app.

If you still see `TemplateNotFound`, you may try the following (From [issue #9](https://github.com/smoqadam/PyFladesk/issues/9#issuecomment-372352796)):

Define this in a helper script:

```python
def resource_path(relative_path):
 """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
```

Include this at the top, under imports

```python
if getattr(sys, 'frozen', False):
    template_folder = resource_path('templates')
    static_folder = resource_path('static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)
```

Also from [issue #9](https://github.com/smoqadam/PyFladesk/issues/9#issuecomment-372352796), in Windows 10 you may need to run this script:

`pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" app.py --path 'C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x64'`

Since Qt is quite big, your executables will be big too. The example app of this repository is 70 MB (69 MB of which are the Qt Component for displaying HTML). This is reasonable taking into account that we are shipping a self contain web browser. In case size is crucial, you can follow [this suggestions](https://elc.github.io/posts/executable-flask-pyinstaller/#the-other-problem-the-size)

## Sample apps

List of apps made by PyFladesk

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
