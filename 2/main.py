import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QDateTime


class Diary(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("diary.ui", self)

        self.events = []

        self.btnAdd.clicked.connect(self.add_event)

    def add_event(self):
        name = self.editName.text().strip()

        if not name:
            return

        date = self.calendar.selectedDate()
        time = self.timeEdit.time()
        dt = QDateTime(date, time)

        self.events.append((dt, name))
        self.events.sort(key=lambda x: x[0])

        self.refresh()
        self.editName.clear()

    def refresh(self):
        self.listEvents.clear()
        for dt, name in self.events:
            text = dt.toString("dd.MM.yyyy HH:mm")
            self.listEvents.addItem(f"{text} — {name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Diary()
    w.show()
    sys.exit(app.exec_())