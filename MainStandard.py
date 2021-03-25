import sys
from PyQt5.QtWidgets import QApplication
from calc4 import StandardCalc

app = QApplication(sys.argv)

Standard = StandardCalc()

sys.exit(app.exec_())
