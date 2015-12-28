import sys

from PyQt4.QtCore import QThread, QUrl
from PyQt4.QtGui import QApplication,QMainWindow
from PyQt4.QtWebKit import QWebView


PORT = 5000
ROOT_URL = 'http://localhost:{}'.format(PORT)
WIDTH = 300
HEIGHT = 400
WINDOW_TITLE = "PyFladesk"

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
        


class WebView(QWebView):
    def __init__(self ,parent=None):
        super(WebView,self).__init__(parent)

    def dragEnterEvent(self,e):
        e.ignore()

    def dropEvent(self,e):
        e.ignore()

    def contextMenuEvent(self,e):
        pass

def provide_GUI_for(application):
    qtapp = QApplication(sys.argv)

    webapp = FlaskThread(application)
    webapp.start()

    qtapp.aboutToQuit.connect(webapp.terminate)

    mainWindow = MainWindow()
    mainWindow.webView.load(QUrl(ROOT_URL))
    mainWindow.show()

    return qtapp.exec_()


if __name__ == '__main__':
    from routes import app
    provide_GUI_for(app)
