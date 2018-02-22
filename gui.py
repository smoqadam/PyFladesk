import sys
import webbrowser

from PyQt5 import QtCore, QtWidgets, QtWebKitWidgets, QtGui


def init_gui(application, port=5000, width=300, height=400,
             window_title="PyFladesk", icon="appicon.png"):

    ROOT_URL = 'http://localhost:{}'.format(port)

    # open links in browser from http://stackoverflow.com/a/3188942/1103397 :D
    def link_clicked(url):
        ready_url = url.toEncoded().data().decode()
        if ROOT_URL not in ready_url:
            webbrowser.open(ready_url)
        else:
            window.webView.load(QtCore.QUrl(ready_url))

    def run_app():
        application.run(port=port, threaded=True)

    qtapp = QtWidgets.QApplication(sys.argv)

    webapp = QtCore.QThread()
    webapp.__del__ = webapp.wait
    webapp.run = run_app
    webapp.start()

    qtapp.aboutToQuit.connect(webapp.terminate)

    window = QtWidgets.QMainWindow()
    window.resize(width, height)
    window.setWindowTitle(window_title)
    window.webView = QtWebKitWidgets.QWebView(window)
    window.setCentralWidget(window.webView)
    window.setWindowIcon(QtGui.QIcon(icon))

    window.webView.page().setLinkDelegationPolicy(
        QtWebKitWidgets.QWebPage.DelegateAllLinks)
    window.webView.page().linkClicked.connect(link_clicked)

    window.webView.load(QtCore.QUrl(ROOT_URL))
    window.show()

    return qtapp.exec_()
