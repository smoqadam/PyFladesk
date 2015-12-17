
import sys
from flask import Flask , render_template
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from threading import Thread




class FlaskThread(QThread):

	def __init__(self,app):
		QThread.__init__(self)
		self.app = app

	def __del__(self):
		self.wait()


	def run(self):
		self.app.run()

 

def main(app):
	th = FlaskThread(app)
	th.start()
	#qt init
	qtapp = QApplication(sys.argv)
	qtapp.aboutToQuit.connect(lambda : th.terminate())
	webview = QWebView()
	webview.load(QUrl('http://localhost:5000'))
	webview.show()
	sys.exit(qtapp.exec_())



