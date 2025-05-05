import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QDialog

class Modal(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secondary Window")
        self.setGeometry(200, 200, 400, 300)
        self.label = QLabel("This is the secondary window", self)
        self.label.move(50, 50)

class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello PyQt5")
        self.setGeometry(100, 100, 800, 600)
        self.label1 = QLabel("Text 1", self)
        self.label1.move(50, 50)

        self.label2 = QLabel("Text 2", self)
        self.label2.move(50, 100)

        self.label3 = QLabel("Text 3", self)
        self.label3.move(50, 150)

        self.label4 = QLabel("Text 4", self)
        self.label4.move(50, 200)

        self.quit_button = QPushButton("Quit", self)
        self.quit_button.move(50, 250)
        self.quit_button.clicked.connect(self.close)

        self.modal_button = QPushButton("Modale", self)
        self.modal_button.move(200, 250)
        self.modal_button.clicked.connect(self.show_modal)

        self.secondary_window = None

    def show_modal(self):
        self.secondary_window = Modal()
        self.secondary_window.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())