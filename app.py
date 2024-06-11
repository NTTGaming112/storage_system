from PySide6.QtWidgets import *

import sys
sys.path.append('main')
sys.path.append('database')
sys.path.append('Object')

from sidebar import MySideBar

app = QApplication()

window = MySideBar()

window.show()
app.exec()