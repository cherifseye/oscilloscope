from sys import setdlopenflags
from PyQt5.QtWidgets import QMainWindow, QFrame, QPushButton, QRadioButton, QWidget, QLabel, QSlider, QDial, QMenuBar, QMenu, QStatusBar, QAction
from PyQt5.QtGui import QFont, QColor
from PyQt5 import QtCore 
import pyqtgraph as pg
import numpy as np



class Oscilloscope(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.graphics()
        self.frameBottom()
        self.channel()
        self.zoom_()
        self.turn()
        self.framediv()
        self.trigered()
        self.coupling()
        self.gain()
        self.level()
        self.setux()
        self.menu()

    def initUI(self):
        self.setGeometry(30, 40, 946, 620)
        self.setObjectName('Oscilloscope')
        self.setWindowTitle('Oscilloscope')
        

    
    def graphics(self):

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setObjectName('centralWidget')
        self.framegraph = QFrame(self.centralWidget)
        self.framegraph.setGeometry(QtCore.QRect(20, 40, 500, 381))
        self.framegraph.setFrameShape(QFrame.StyledPanel)
        self.framegraph.setFrameShadow(QFrame.Raised)
        self.framegraph.setObjectName('framegraph')
        self.graph = pg.PlotWidget(self.framegraph)
        self.graph.setGeometry(QtCore.QRect(10, 10, 480, 361))
        self.graph.setObjectName('graph')
        #self.graph.setBackground('#02659D')
        self.graph.setLabel('left', 'Voltage', 'V')
        self.graph.setLabel('bottom', 'Time', 's')
        y = np.sin(np.linspace(0, 10, 1000)) + np.random.normal(size=1000, scale=0.1)
        self.graph.plot(y, fillLevel=-0.3, brush=(50,50,200,100))
        lr = pg.LinearRegionItem([400, 700])
        lr.setZValue(0)
        self.graph.addItem(lr)
        self.graph.showGrid(x=True, y=True)

    
    def frameBottom(self):
        self.Rbotframe = QFrame(self.centralWidget)
        self.Rbotframe.setGeometry(QtCore.QRect(20, 440, 500, 120))
        self.Rbotframe.setFrameShape(QFrame.StyledPanel)
        self.Rbotframe.setFrameShadow(QFrame.Raised)
        self.Rbotframe.setObjectName('Rbotframe')

        self.setuxlabel = QLabel(self.Rbotframe)
        self.setuxlabel.setGeometry(QtCore.QRect(30, 20, 61, 55))
        self.setuxlabel.setObjectName('lbel_Rbot')
        self.setuxlabel.setText('SETUX')
        self.setuxlabel.setFont(QFont('Arial', 17))
        self.setuxlabel.setStyleSheet('color:#02659D')

        self.osclabel = QLabel(self.Rbotframe)
        self.osclabel.setGeometry(QtCore.QRect(0, 40, 131, 70))
        self.osclabel.setObjectName('lbel_Rbot2')
        self.osclabel.setText('OSCILLOSCOPE')
        self.osclabel.setFont(QFont('Arial', 17))
        self.osclabel.setStyleSheet('color:#02659D')

    def zoom_(self):
        self.zoomframe = QFrame(self.Rbotframe)
        self.zoomframe.setGeometry(QtCore.QRect(270, 0, 70, 100))
        self.zoomframe.setFrameShape(QFrame.StyledPanel)
        self.zoomframe.setFrameShadow(QFrame.Raised)
        self.zoomframe.setObjectName('channelframe')

        self.slider = QSlider(self.zoomframe)
        self.slider.setGeometry(QtCore.QRect(20, 20, 22, 80))
        self.slider.setOrientation(QtCore.Qt.Vertical)
        self.slider.setObjectName('slider')

        self.slidelabel = QLabel(self.zoomframe)
        self.slidelabel.setGeometry(QtCore.QRect(15, 0, 70, 30))
        self.slidelabel.setObjectName('slidelabel')
        self.slidelabel.setText('ZOOM')
        
    def turn(self):
        self.turnframe = QFrame(self.Rbotframe)
        self.turnframe.setGeometry(QtCore.QRect(370, 20, 120, 70))
        self.turnframe.setFrameShape(QFrame.StyledPanel)
        self.turnframe.setFrameShadow(QFrame.Raised)
        self.turnframe.setObjectName('channelframe')

        self.turnOn = QPushButton(self.turnframe)
        self.turnOn.setGeometry(QtCore.QRect(10, 15, 50, 40))
        self.turnOn.setObjectName('turnOn')
        self.turnOn.setText('ON')

        self.turnOff = QPushButton(self.turnframe)
        self.turnOff.setGeometry(QtCore.QRect(60, 15, 50, 40))
        self.turnOff.setObjectName('turnOff')
        self.turnOff.setText('OFF')
        

    def channel(self):
        self.channelframe = QFrame(self.Rbotframe)
        self.channelframe.setGeometry(QtCore.QRect(170, 0, 70, 100))
        self.channelframe.setFrameShape(QFrame.StyledPanel)
        self.channelframe.setFrameShadow(QFrame.Raised)
        self.channelframe.setObjectName('channelframe')
        
        self.channel1 = QRadioButton(self.channelframe)
        self.channel1.setGeometry(QtCore.QRect(10, 10, 70, 20))
        self.channel1.setObjectName('channel1')
        self.channel1.setText('CH1')

        self.channel2 = QRadioButton(self.channelframe)
        self.channel2.setGeometry(QtCore.QRect(10, 30, 70, 20))
        self.channel2.setObjectName('channel1')
        self.channel2.setText('CH2')

        self.channel3 = QRadioButton(self.channelframe)
        self.channel3.setGeometry(QtCore.QRect(10, 50, 70, 20))
        self.channel3.setObjectName('channel1')
        self.channel3.setText('CH3')

        self.channel4 = QRadioButton(self.channelframe)
        self.channel4.setGeometry(QtCore.QRect(10, 70, 70, 20))
        self.channel4.setObjectName('channel1')
        self.channel4.setText('CH4')

    def framediv(self):

        self.framdiv = QFrame(self.centralWidget)
        self.framdiv.setGeometry(QtCore.QRect(575, 40, 150, 120))
        self.framdiv.setFrameShape(QFrame.StyledPanel)
        self.framdiv.setFrameShadow(QFrame.Raised)
        self.framdiv.setObjectName('framdiv')

        self.divlabel = QLabel(self.framdiv)
        self.divlabel.setGeometry(QtCore.QRect(50, 0, 70, 30))
        self.divlabel.setObjectName('divlabel')
        self.divlabel.setText('SEC/DIV')

        self.dial = QDial(self.framdiv)
        self.dial.setGeometry(QtCore.QRect(10, 30, 120, 80))
        self.dial.setObjectName('dial')
        self.dial.setRange(1, 100)

        self.framedivT = QFrame(self.centralWidget)
        self.framedivT.setGeometry(QtCore.QRect(750, 40, 150, 120))
        self.framedivT.setFrameShape(QFrame.StyledPanel)
        self.framedivT.setFrameShadow(QFrame.Raised)
        self.framedivT.setObjectName('framedivT')

        self.dial1 = QDial(self.framedivT)
        self.dial1.setGeometry(QtCore.QRect(10, 30, 120, 80))
        self.dial1.setObjectName('dial1')
        self.dial1.setRange(1, 100)

        self.divlabelT = QLabel(self.framedivT)
        self.divlabelT.setGeometry(QtCore.QRect(40, 0, 70, 30))
        self.divlabelT.setObjectName('divlabelT')
        self.divlabelT.setText('VOLTS/DIV')


    
    def trigered(self):
        self.frmaeTrig = QFrame(self.centralWidget)
        self.frmaeTrig.setGeometry(QtCore.QRect(575, 200, 150, 120))
        self.frmaeTrig.setFrameShape(QFrame.StyledPanel)
        self.frmaeTrig.setFrameShadow(QFrame.Raised)
        self.frmaeTrig.setObjectName('frmaeTrig')
        self.trigeredlabel = QLabel(self.frmaeTrig)
        self.trigeredlabel.setGeometry(QtCore.QRect(40, 10, 70, 30))
        self.trigeredlabel.setObjectName('trigeredlabel')
        self.trigeredlabel.setText('TRIGGERED')
        self.trigeredlabel.adjustSize()

        self.acbutton = QPushButton(self.frmaeTrig)
        self.acbutton.setGeometry(QtCore.QRect(10, 40, 60, 50))
        self.acbutton.setObjectName('acbutton')
        self.acbutton.setText('AC')
        self.dcbutton = QPushButton(self.frmaeTrig)
        self.dcbutton.setGeometry(QtCore.QRect(80, 40, 60, 50))
        self.dcbutton.setObjectName('dcbutton')
        self.dcbutton.setText('DC')
        
    
    def coupling(self):
        self.couplingframe = QFrame(self.centralWidget)
        self.couplingframe.setGeometry(QtCore.QRect(750, 200, 150, 120))
        self.couplingframe.setFrameShape(QFrame.StyledPanel)
        self.couplingframe.setFrameShadow(QFrame.Raised)
        self.couplingframe.setObjectName('couplingframe')
        self.couplinglabel = QLabel(self.couplingframe)
        self.couplinglabel.setGeometry(QtCore.QRect(40, 10, 70, 30))
        self.couplinglabel.setObjectName('couplinglabel')
        self.couplinglabel.setText('COUPLING')
        self.couplinglabel.adjustSize()

        self.AutoButton = QPushButton(self.couplingframe)
        self.AutoButton.setGeometry(QtCore.QRect(10, 40, 60, 50))
        self.AutoButton.setObjectName('AutoButton')
        self.AutoButton.setText('AUTO')
        self.LineButton = QPushButton(self.couplingframe)
        self.LineButton.setGeometry(QtCore.QRect(80, 40, 60, 50))
        self.LineButton.setObjectName('LineButton')
        self.LineButton.setText('LINE')

    
    def gain(self):
        self.gainframe = QFrame(self.centralWidget)
        self.gainframe.setGeometry(QtCore.QRect(575, 360, 150, 60))
        self.gainframe.setFrameShape(QFrame.StyledPanel)
        self.gainframe.setFrameShadow(QFrame.Raised)
        self.gainframe.setObjectName('gainframe')
        self.gainlabel = QLabel(self.gainframe)
        self.gainlabel.setGeometry(QtCore.QRect(60, 10, 60, 10))
        self.gainlabel.setObjectName('gainlabel')
        self.gainlabel.setText('GAIN')
        self.gainlabel.adjustSize()
        self.slide = QSlider(self.gainframe)
        self.slide.setGeometry(QtCore.QRect(10, 30, 130, 40))
        self.slide.setOrientation(QtCore.Qt.Horizontal)
        self.slide.setObjectName('slide')

    def level(self):
        self.levelframe = QFrame(self.centralWidget)
        self.levelframe.setGeometry(QtCore.QRect(750, 360, 150, 60))
        self.levelframe.setFrameShape(QFrame.StyledPanel)
        self.levelframe.setFrameShadow(QFrame.Raised)
        self.levelframe.setObjectName('levelframe')
        self.levellabel = QLabel(self.levelframe)
        self.levellabel.setGeometry(QtCore.QRect(60, 10, 60, 15))
        self.levellabel.setObjectName('levellabel')
        self.levellabel.setText('LEVEL')
        self.slide = QSlider(self.levelframe)
        self.slide.setGeometry(QtCore.QRect(10, 30, 130, 40))
        self.slide.setOrientation(QtCore.Qt.Horizontal)
        self.slide.setObjectName('slide')

    
    def setux(self):
        self.setuxLabel = QLabel(self.centralWidget)
        self.setuxLabel.setGeometry(QtCore.QRect(560, 480, 100, 20))
        self.setuxLabel.setObjectName('setuxLabel')
        self.setuxLabel.setText('PROVIDES BY SETUX TECHNOLOGIES')
        self.setuxLabel.setFont(QFont('Times', 20, QFont.Bold))
        self.setuxLabel.setStyleSheet('color:#02659D')
        self.setuxLabel.adjustSize()

        self.setuxLabel2 = QLabel(self.centralWidget)
        self.setuxLabel2.setGeometry(QtCore.QRect(680, 520, 100, 20))
        self.setuxLabel2.setObjectName('setuxLabel2')
        self.setuxLabel2.setText('www.setux.com')
        self.setuxLabel2.setFont(QFont("Times", 20, QFont.Bold))
        self.setuxLabel2.setStyleSheet("color:#02659D")
        self.setuxLabel2.adjustSize()

    def menu(self):
        exit_act = QAction('Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)

        self.helpContentAction = QAction('&Help Content', self)
        self.aboutAction = QAction('&About', self)
        

        self.dataAction = QAction('&Generate data csv', self)
        self.visualAction = QAction('&Visualize data', self)
        
        
        menuBar = QMenuBar(self)
        menuBar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.setMenuBar(menuBar)
        General = QMenu("&File", self)
        menuBar.addMenu(General)

        helpmenu = menuBar.addMenu("&Help")
        helpmenu.addAction(self.helpContentAction)
        helpmenu.addAction(self.aboutAction)

        data = menuBar.addMenu("&View")
        data.addAction(self.dataAction)
        data.addAction(self.visualAction)

        exit = menuBar.addMenu("&Exit")
        exit.addAction(exit_act)

        menuBar.setNativeMenuBar(False)
        self.setStatusBar(QStatusBar(self))


