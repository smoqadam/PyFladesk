import sys
from PyQt5 import QtCore, QtWidgets, QtWebKitWidgets, QtGui


class ApplicationThread(QtCore.QThread):
    def __init__(self, application, port=5000):
        super(ApplicationThread, self).__init__()
        self.application = application
        self.port = port

    def __del__(self):
        self.wait()

    def run(self):
        self.application.run(port=self.port, threaded=True)


class WebView(QtWebKitWidgets.QWebView):
    def __init__(self, root_url, parent=None):
        super(WebView, self).__init__(parent)
        self.root_url = root_url
        self.page().setLinkDelegationPolicy(QtWebKitWidgets.QWebPage.DelegateAllLinks)
        self.page().linkClicked.connect(self.__link_clicked)
        self.load(QtCore.QUrl(self.root_url))

    def __link_clicked(self, url):
        """Open external links in browser and internal links in the webview"""
        ready_url = url.toEncoded().data().decode()
        if self.root_url not in ready_url:
            QtGui.QDesktopServices.openUrl(url)
        else:
            self.load(QtCore.QUrl(ready_url))


def init_gui(application, port=5000, width=300, height=400,
             window_title="PyFladesk", icon="appicon.png", argv=None):
    if argv is None:
        argv = sys.argv

    # Application Level
    qtapp = QtWidgets.QApplication(argv)
    webapp = ApplicationThread(application, port)
    webapp.start()
    qtapp.aboutToQuit.connect(webapp.terminate)

    # Main Windows Level
    window = QtWidgets.QMainWindow()
    window.resize(width, height)
    window.setWindowTitle(window_title)
    window.setWindowIcon(QtGui.QIcon(icon))

    # WebView Level
    webView = WebView(f'http://localhost:{port}', window)
    window.setCentralWidget(webView)

    window.show()

    return qtapp.exec_()
