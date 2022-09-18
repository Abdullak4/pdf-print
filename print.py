# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 01:00:16 2022

@author: abdulla
"""

from PyQt5.QtWidgets import *
import sys 
from PyQt5.QtPrintSupport import *
class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,500,500,500)
        
        self.message()
    def message(self):
        self.t=QTextEdit()
        self.z=QPushButton("Click to print")
        self.z1=QPushButton("Click to convert to pdf")
        self.z.clicked.connect(self.color)
        self.z1.clicked.connect(self.c)
        vb=QVBoxLayout()
        vb.addWidget(self.t)
        hb=QHBoxLayout()
        vb.addLayout(hb)
        hb.addWidget(self.z)
        hb.addWidget(self.z1)
        self.setLayout(vb)
        self.setLayout(hb)
        
    def color(self):
        ok=QPrinter(QPrinter.HighResolution)
        d=QPrintDialog(ok,self)
        
        if d.exec_()==QPrintDialog.Accepted():
            self.t.print_(ok)
        
            
        
    def c(self):
       ok=QPrinter(QPrinter.HighResolution)
       d=self.t.print_(ok)
       pp=QPrintPreviewDialog(ok,self)
       pp.paintRequested.connect(self.d)
       pp.exec_()
        

        
       
        
       
        
app=QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())
