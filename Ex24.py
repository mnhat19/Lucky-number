from random import randrange

from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow

from Interface24 import Ui_MainWindow

class Ex24(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.pla_money = 100
        self.mac_money = 100

    def setupUi(self, Interface24):
        super().setupUi(Interface24)
        self.Interface24 = Interface24
        self.pushButton.clicked.connect(self.random)
        self.pushButton_2.clicked.connect(self.new_game)
        self.pushButton_3.clicked.connect(self.exit)

    def show(self):
        self.Interface24.show()

    def random(self):

        if self.pla_money <30:
            self.pushButton.setEnabled(False)
            return
        else:
            self.pla_money -= 30
            self.mac_money += 30
            spin1 = randrange(0, 8)
            spin2 = randrange(0, 9)
            spin3 = randrange(0, 11)

        # Hiển thị kết quả của từng spin
        self.label.setText(str(spin1))
        self.label_2.setText(str(spin2))
        self.label_3.setText(str(spin3))

        a = self.pla_money
        b = self.mac_money

        # Kiểm tra logic và cập nhật số tiền
        if spin1 == 7:
            a += 100 + b * 0.5
            b -= b * 0.5
        if spin2 == 7:
            a += 30 + b * 0.5
            b -= b * 0.5
        if spin3 == 7:
            a += 10
        if spin1 == 7 and spin2 == 7 and spin3 == 7:
            a += 140 + b
            b = 0

        # Cập nhật lại số tiền
        self.pla_money = int(a)
        self.mac_money = int(b)

        # Hiển thị số tiền trên giao diện
        self.label_pla.setText(str(int(a)))
        self.label_mac.setText(str(int(b)))

    def new_game(self):
        self.pla_money =100
        self.mac_money =100
        self.pushButton.setEnabled(True)
        self.label.setText("7")
        self.label_2.setText("7")
        self.label_3.setText("7")
        self.label_mac.setText("100")
        self.label_pla.setText("100")

    def exit(self):
        dlg = QMessageBox(self.Interface24)
        dlg.setWindowTitle("Exit confirmation")
        dlg.setText("Are you sure you want to exit?")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        # check the user confirmation
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            QApplication.instance().quit()
        else:
            self.Interface24.show()
