import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QMessageBox


class FlagWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("flag.ui", self)

        self.btnDraw.clicked.connect(self.draw)

    def draw(self):
        groups = [self.groupBox_1, self.groupBox_2, self.groupBox_3]
        result = []

        for box in groups:
            chosen = None
            for rb in box.findChildren(QRadioButton):
                if rb.isChecked():
                    chosen = rb.text()
                    break

            if chosen is None:
                QMessageBox.warning(
                    self, "Ошибка",
                    f"Выберите цвет для «{box.title()}»"
                )
                return

            result.append(chosen)

        QMessageBox.information(self, "Флаг", ", ".join(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = FlagWindow()
    w.show()
    sys.exit(app.exec_())