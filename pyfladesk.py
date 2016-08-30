import sys,webbrowser

from PyQt5.QtCore import QThread, QUrl,pyqtSignal,QSize
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEnginePage

# CONFIG
PORT = 5000
ROOT_URL = 'http://localhost:{}'.format(PORT)
WIDTH = 300
HEIGHT = 400
WINDOW_TITLE = "PyFladesk"
ICON = 'appicon.png'


# run flask on seperate theared
class FlaskThread(QThread):
    def __init__(self, application):
        QThread.__init__(self)
        self.application = application

    def __del__(self):
        self.wait()

    def run(self):
        self.application.run(port=PORT)


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.resize (WIDTH , HEIGHT)
        self.setWindowTitle(WINDOW_TITLE)
        self.webView = WebView(self)
        self.setCentralWidget(self.webView)
        


class WebView(QWebEngineView):
    def __init__(self ,parent=None):
        super(WebView,self).__init__(parent)

    def dragEnterEvent(self,e):
        e.ignore()

    def dropEvent(self,e):
        e.ignore()

    def contextMenuEvent(self,e):
        pass
    
    # open links in default browser 
    # stolen from http://stackoverflow.com/a/3188942/1103397 :D
    def linkClicked(self,url): 
        webbrowser.open(url.toEncoded().data())
        
        
def provide_GUI_for(application):
    qtapp = QApplication(sys.argv)

    webapp = FlaskThread(application)
    webapp.start()

    qtapp.aboutToQuit.connect(webapp.terminate)

    mainWindow = MainWindow()
    # set app icon    
    mainWindow.setWindowIcon(QIcon(ICON))
    
    
    mainWindow.webView.load(QUrl(ROOT_URL))
    mainWindow.show()

    return qtapp.exec_()


if __name__ == '__main__':
    from routes import app
    provide_GUI_for(app)
