import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class NimGame(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("nim.ui", self)

        self.stones = 0

        self.btnNew.clicked.connect(self.new_game)
        self.btnTake.clicked.connect(self.player_move)

    def new_game(self):
        self.stones = self.spinStart.value()
        self.labelInfo.setText(f"Камней на столе: {self.stones}")
        self.btnTake.setEnabled(True)

    def player_move(self):
        take = self.spinTake.value()

        if take < 1 or take > 3:
            QMessageBox.warning(self, "Ошибка", "Можно взять 1, 2 или 3 камня")
            return
        if take > self.stones:
            QMessageBox.warning(self, "Ошибка", "Нельзя взять больше, чем есть на столе")
            return

        self.stones -= take

        if self.stones == 0:
            self.labelInfo.setText("Вы взяли последний камень. Победа!")
            self.btnTake.setEnabled(False)
            return

        self.ai_move()

    def ai_move(self):
        ai_take = self.stones % 4
        if ai_take == 0:
            ai_take = 1
        ai_take = min(ai_take, self.stones, 3)

        self.stones -= ai_take

        if self.stones == 0:
            self.labelInfo.setText(
                f"ИИ взял {ai_take}. Компьютер взял последний камень. Вы проиграли."
            )
            self.btnTake.setEnabled(False)
            return

        self.labelInfo.setText(
            f"ИИ взял {ai_take}. Камней на столе: {self.stones}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = NimGame()
    w.show()
    sys.exit(app.exec_())