import sys
from PyQt5 import QtCore, QtWidgets, QtGui, QtWebEngineWidgets


def init_gui(application, port=5000, width=300, height=400,
             window_title="PyFladesk", icon="appicon.png"):

    ROOT_URL = 'http://localhost:{}'.format(port)

    # open links in browser from http://stackoverflow.com/a/3188942/1103397 :D
    # thanks to https://github.com/marczellm/qhangups/blob/cfed73ee4383caed1568c0183a9906180f01cb00/qhangups/WebEnginePage.py
    def link_clicked(url, typ, ismainframe):
        ready_url = url.toEncoded().data().decode()
        is_clicked = typ == QtWebEngineWidgets.QWebEnginePage.NavigationTypeLinkClicked
        is_not_internal = ROOT_URL not in ready_url
        if is_clicked and is_not_internal:
            QtGui.QDesktopServices.openUrl(url)
            return False
        return True

    def run_app():
        application.run(port=port, threaded=True)

    # Application Level
    qtapp = QtWidgets.QApplication(sys.argv)
    webapp = QtCore.QThread()
    webapp.__del__ = webapp.wait
    webapp.run = run_app
    webapp.start()
    qtapp.aboutToQuit.connect(webapp.terminate)

    # Main Window Level
    window = QtWidgets.QMainWindow()
    window.resize(width, height)
    window.setWindowTitle(window_title)
    window.setWindowIcon(QtGui.QIcon(icon))

    # WebView Level
    window.webView = QtWebEngineWidgets.QWebEngineView(window)
    window.setCentralWidget(window.webView)

    # WebPage Level
    page = QtWebEngineWidgets.QWebEnginePage()
    page.acceptNavigationRequest = link_clicked
    page.load(QtCore.QUrl(ROOT_URL))
    window.webView.setPage(page)

    window.show()

    return qtapp.exec_()
