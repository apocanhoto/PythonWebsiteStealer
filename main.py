import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebKit import *

class Render(QWebPage):  
  def __init__(self, urls, cb):
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.urls = urls  
    self.cb = cb
    self.crawl()  
    self.app.exec_()  
      
  def crawl(self):  
    if self.urls:  
      url = self.urls.pop(0)  
      print('Downloading '), url  
      self.mainFrame().load(QUrl(url))  
    else:  
      self.app.quit()  
        
  def _loadFinished(self, result):  
    frame = self.mainFrame()  
    url = str(frame.url().toString())  
    html = frame.toHtml()  
    self.cb(url, html)
    self.crawl()  


def scrape(url, html):
    pass # add scraping code here


urls = ['http://webscraping.com', 'http://webscraping.com/blog']  
r = Render(urls, cb=scrape)