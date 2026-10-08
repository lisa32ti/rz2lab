import sys
import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Antiplag(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "antiplag.ui")
        uic.loadUi(ui_path, self)

        self.statusbar.showMessage("Готово")

        self.btnCalc.clicked.connect(self.compare)

    def compare(self):
        lines1 = [l.strip() for l in self.text1.toPlainText().splitlines() if l.strip()]
        lines2 = [l.strip() for l in self.text2.toPlainText().splitlines() if l.strip()]

        if not lines1 or not lines2:
            self.set_status("Заполните оба текста", "orange")
            return

        set2 = set(lines2)
        matches = sum(1 for l in lines1 if l in set2)
        percent = matches / len(lines1) * 100

        threshold = self.spinThreshold.value()

        if percent >= threshold:
            msg = f"Плагиат! Совпадение {percent:.1f}% (порог {threshold:.1f}%)"
            self.set_status(msg, "red")
        else:
            msg = f"Уникально. Совпадение {percent:.1f}% (порог {threshold:.1f}%)"
            self.set_status(msg, "green")

    def set_status(self, message, color):
        self.statusbar.setStyleSheet(f"color: {color};")
        self.statusbar.showMessage(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Antiplag()
    w.show()
    sys.exit(app.exec_())