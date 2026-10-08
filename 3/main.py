import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Notebook(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("notebook.ui", self)

        self.contacts = []

        self.btnAdd.clicked.connect(self.add_contact)

    def add_contact(self):
        name = self.editName.text().strip()
        phone = self.editPhone.text().strip()

        if not name or not phone:
            QMessageBox.warning(self, "Ошибка", "Заполните оба поля")
            return

        self.contacts.append((name, phone))
        self.refresh()

        self.editName.clear()
        self.editPhone.clear()

    def refresh(self):
        self.listContacts.clear()
        for name, phone in self.contacts:
            self.listContacts.addItem(f"{name}: {phone}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Notebook()
    w.show()
    sys.exit(app.exec_())