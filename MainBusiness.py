import sys
from PyQt5.QtWidgets import QApplication
from Business4 import BusinessCalc

app = QApplication(sys.argv)

Business = BusinessCalc()

sys.exit(app.exec_())
