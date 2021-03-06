import os
import sys
import time
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout, QSpinBox
from PyQt5.QtCore import QCoreApplication
import smtplib
from Mymail import Go

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        qbtn = QPushButton('Завершить работу', self)
        qbtn.clicked.connect(self.shutdown)
        self.spin = QSpinBox()
        self.spin.setRange(0, 3600000)
        self.spin.setSingleStep(60)
        self.spin.setValue(60)
        vbox = QVBoxLayout()
        vbox.addWidget(qbtn)
        vbox.addWidget(self.spin)
        self.setWindowTitle('Завершение по таймеру')
        self.show()
        self.setLayout(vbox)
        self.setGeometry(150, 150, 250, 150)

    def shutdown(self):
        time.sleep(self.spin.value())
        Go()
        myCmd = 'shutdown /s /t 0'
        os.system(myCmd)
        self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


