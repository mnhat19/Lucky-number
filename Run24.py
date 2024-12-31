from PyQt6.QtWidgets import QApplication, QMainWindow

from Ex24 import Ex24

app=QApplication([])
myWindow= Ex24()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()