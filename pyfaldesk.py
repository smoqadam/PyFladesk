import sys

from PyQt4.QtCore import QThread, QUrl
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebView


PORT = 5000
ROOT_URL = 'http://localhost:{}'.format(PORT)


class FlaskThread(QThread):
    def __init__(self, application):
        QThread.__init__(self)
        self.application = application

    def __del__(self):
        self.wait()

    def run(self):
        self.application.run(port=PORT)


def provide_GUI_for(application):
    qtapp = QApplication(sys.argv)

    webapp = FlaskThread(application)
    webapp.start()

    qtapp.aboutToQuit.connect(webapp.terminate)

    webview = QWebView()
    webview.load(QUrl(ROOT_URL))
    webview.show()

    return qtapp.exec_()


if __name__ == '__main__':
    from routes import app
    sys.exit(provide_GUI_for(app))
