import sys
import math
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication,\
                            QPushButton, QLabel
import PyQt5.QtGui as QtGui


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 460, 600)
        self.setWindowTitle('Калькулятор')
        self.res = 0
        self.text  = ''

        self.button_dot = QPushButton(self)
        self.button_dot.move(10, 530)
        self.button_dot.resize(80, 60)
        self.button_dot.setText(".")
        self.button_dot.clicked.connect(self.run)

        self.button_zero = QPushButton(self)
        self.button_zero.move(100, 530)
        self.button_zero.resize(80, 60)
        self.button_zero.setText("0")
        self.button_zero.clicked.connect(self.run)

        self.button_c = QPushButton(self)
        self.button_c.move(190, 530)
        self.button_c.resize(80, 60)
        self.button_c.setText("C")
        self.button_c.clicked.connect(self.clear)

        self.button_res = QPushButton(self)
        self.button_res.move(280, 530)
        self.button_res.resize(80, 60)
        self.button_res.setText("=")
        self.button_res.clicked.connect(self.resul)

        self.button_1 = QPushButton(self)
        self.button_1.move(10, 460)
        self.button_1.resize(80, 60)
        self.button_1.setText("1")
        self.button_1.clicked.connect(self.run)

        self.button_2 = QPushButton(self)
        self.button_2.move(100, 460)
        self.button_2.resize(80, 60)
        self.button_2.setText("2")
        self.button_2.clicked.connect(self.run)

        self.button_3 = QPushButton(self)
        self.button_3.move(190, 460)
        self.button_3.resize(80, 60)
        self.button_3.setText("3")
        self.button_3.clicked.connect(self.run)

        self.button_4 = QPushButton(self)
        self.button_4.move(10, 390)
        self.button_4.resize(80, 60)
        self.button_4.setText("4")
        self.button_4.clicked.connect(self.run)

        self.button_5 = QPushButton(self)
        self.button_5.move(100, 390)
        self.button_5.resize(80, 60)
        self.button_5.setText("5")
        self.button_5.clicked.connect(self.run)

        self.button_6 = QPushButton(self)
        self.button_6.move(190, 390)
        self.button_6.resize(80, 60)
        self.button_6.setText("6")
        self.button_6.clicked.connect(self.run)

        self.button_7 = QPushButton(self)
        self.button_7.move(10, 320)
        self.button_7.resize(80, 60)
        self.button_7.setText("7")
        self.button_7.clicked.connect(self.run)

        self.button_8 = QPushButton(self)
        self.button_8.move(100, 320)
        self.button_8.resize(80, 60)
        self.button_8.setText("8")
        self.button_8.clicked.connect(self.run)

        self.button_9 = QPushButton(self)
        self.button_9.move(190, 320)
        self.button_9.resize(80, 60)
        self.button_9.setText("9")
        self.button_9.clicked.connect(self.run)

        self.button_plus = QPushButton(self)
        self.button_plus.move(280, 460)
        self.button_plus.resize(80, 60)
        self.button_plus.setText("+")
        self.button_plus.clicked.connect(self.summ)

        self.button_minus = QPushButton(self)
        self.button_minus.move(280, 390)
        self.button_minus.resize(80, 60)
        self.button_minus.setText("-")
        self.button_minus.clicked.connect(self.minus)

        self.button_mult = QPushButton(self)
        self.button_mult.move(280, 320)
        self.button_mult.resize(80, 60)
        self.button_mult.setText("*")
        self.button_mult.clicked.connect(self.multi)

        self.button_divi = QPushButton(self)
        self.button_divi.move(280, 250)
        self.button_divi.resize(80, 60)
        self.button_divi.setText("/")
        self.button_divi.clicked.connect(self.divis)

        self.button_fact = QPushButton(self)
        self.button_fact.move(190, 250)
        self.button_fact.resize(80, 60)
        self.button_fact.setText("n!")
        self.button_fact.clicked.connect(self.fact)

        self.button_sin = QPushButton(self)
        self.button_sin.move(370, 320)
        self.button_sin.resize(80, 60)
        self.button_sin.setText("sin")
        self.button_sin.clicked.connect(self.sin)

        self.button_cos = QPushButton(self)
        self.button_cos.move(370, 390)
        self.button_cos.resize(80, 60)
        self.button_cos.setText("cos")
        self.button_cos.clicked.connect(self.cos)

        self.button_tg = QPushButton(self)
        self.button_tg.move(370, 460)
        self.button_tg.resize(80, 60)
        self.button_tg.setText("tan")
        self.button_tg.clicked.connect(self.tan)

        self.button_ctg = QPushButton(self)
        self.button_ctg.move(370, 530)
        self.button_ctg.resize(80, 60)
        self.button_ctg.setText("ctan")
        self.button_ctg.clicked.connect(self.ctan)

        self.button_pi = QPushButton(self)
        self.button_pi.move(370, 250)
        self.button_pi.resize(80, 60)
        self.button_pi.setText("п")
        self.button_pi.clicked.connect(self.run)

        self.button_sqr = QPushButton(self)
        self.button_sqr.move(100, 250)
        self.button_sqr.resize(80, 60)
        self.button_sqr.setText("√")
        self.button_sqr.clicked.connect(self.sqr)

        self.button_sqr = QPushButton(self)
        self.button_sqr.move(10, 250)
        self.button_sqr.resize(80, 60)
        self.button_sqr.setText("+/-")
        self.button_sqr.clicked.connect(self.pm)

        self.label = QLabel(self)
        self.label.resize(600, 30)
        self.label.move(10, 50)
        self.label.font()

        self.show()

    def run(self):
        if self.sender().text() == ".":
            if "." not in self.text:
                self.text += '.'
                self.label.setText(self.text)
        elif self.label.text() == "п":
            self.res = math.pi
            self.text = math.pi
            self.label.setText(math.pi)
        elif self.sender().text() == "0" and self.label.text() != "0":
            self.text += '0'
            self.label.setText(self.text)
        elif self.label.text() == "0" or self.label.text() == "":
            self.text = self.sender().text()
            self.label.setText(self.text)
        else:
            self.text += self.sender().text()
            self.label.setText(self.text)

    def flags(self):
        self.pf = False
        self.mf = False
        self.multf = False
        self.df = False
        self.ff = False
        self.sinf = False
        self.cosf = False
        self.tanf = False
        self.ctanf = False
        self.pmf = False
        self.sf = False

    def summ(self):
        self.flags()
        self.pf = True
        self.res = float(self.text)
        self.text = ''

    def minus(self):
        self.flags()
        self.mf = True
        self.res = float(self.text)
        self.text = ''

    def multi(self):
        self.flags()
        self.multf = True
        self.res = float(self.text)
        self.text = ''

    def divis(self):
        self.flags()
        self.df = True
        self.res = float(self.text)
        self.text = ''

    def fact(self):
        self.flags()
        self.ff = True
        self.res = float(self.text)
        self.text = ''

    def sin(self):
        self.flags()
        self.sinf = True
        self.res = float(self.text)
        self.text = ''

    def cos(self):
        self.flags()
        self.cosf = True
        self.res = float(self.text)
        self.text = ''

    def tan(self):
        self.flags()
        self.tanf = True
        self.res = float(self.text)
        self.text = ''

    def ctan(self):
        self.flags()
        self.ctanf = True
        self.res = float(self.text)
        self.text = ''

    def pm(self):
        self.flags()
        self.pmf = True
        self.res = float(self.text)
        self.text = ''

    def sqr(self):
        self.flags()
        self.sf = True
        self.res = float(self.text)
        self.text = ''

    

    def resul(self):
        if self.pf:
            self.flags()
            self.res += float(self.text)

        if self.mf:
            self.flags()
            self.res -= float(self.text)

        if self.multf:
            self.flags()
            self.res *= float(self.text)

        if self.df:
            self.flags()
            self.res /= float(self.text)

        if self.ff:
            self.flags()
            self.res = math.factorial(self.res)

        if self.sinf:
            self.flags()
            self.res = math.sin(self.res)

        if self.cosf:
            self.flags()
            self.res = math.cos(self.res)

        if self.tanf:
            self.flags()
            self.res = math.tan(self.res)

        if self.ctanf:
            self.flags()
            self.res = 1/math.tan(self.res)

        if self.pmf:
            self.flags()
            self.res = -self.res

        if self.sf:
            self.flags()
            self.res = math.sqrt(self.res)

        self.text = self.res
        print(self.text)
        if self.text == int(self.text):
            self.text = int(self.text)

        self.label.setText(str(self.text))
        print((self.text))

    def clear(self):
        self.text = ''
        self.res = 0
        self.label.setText(self.text)
        print((self.text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())
