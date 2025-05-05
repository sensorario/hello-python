import sys
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QDialog,
    QWidget,          # MODIFICATO: aggiunto per il central widget
    QVBoxLayout       # MODIFICATO: aggiunto per usare i layout anziché posizionamenti assoluti
)

class Modal(QDialog):
    def __init__(self, parent=None):   # MODIFICATO: esplicito parent
        super().__init__(parent)       # MODIFICATO: passaggio parent al super
        self.setWindowTitle("Secondary Window")
        # self.setGeometry(200, 200, 400, 300)  # Rimosso geometry per lasciare che il layout gestisca le dimensioni
        self.resize(400, 300)           # MODIFICATO: uso resize anziché geometry
        # Layout semplice per centrare il contenuto
        layout = QVBoxLayout()         # MODIFICATO: uso QVBoxLayout
        self.label = QLabel("This is the secondary window")
        layout.addWidget(self.label)
        self.setLayout(layout)         # MODIFICATO: applico il layout

class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello PyQt5")
        self.resize(800, 600)           # MODIFICATO: uso resize anziché geometry

        # Creazione di un central widget con layout verticale
        central = QWidget(self)         # MODIFICATO
        self.setCentralWidget(central)  # MODIFICATO
        layout = QVBoxLayout()          # MODIFICATO
        central.setLayout(layout)       # MODIFICATO

        # Creazione dinamica delle etichette
        texts = ["Text 1", "Text 2", "Text 3", "Text 4"]
        for txt in texts:
            lbl = QLabel(txt, self)
            layout.addWidget(lbl)       # MODIFICATO: aggiungo al layout invece che posizionare manualmente

        # Pulsante Quit
        self.quit_button = QPushButton("Quit", self)
        self.quit_button.clicked.connect(self.close)
        layout.addWidget(self.quit_button)  # MODIFICATO

        # Pulsante Modale
        self.modal_button = QPushButton("Modale", self)
        self.modal_button.clicked.connect(self.show_modal)
        layout.addWidget(self.modal_button)  # MODIFICATO

        # Non serve predefinire secondary_window qui
        # self.secondary_window = None

    def show_modal(self):
        modal = Modal(self)             # MODIFICATO: passo self come parent
        modal.exec()                    # MODIFICATO: uso exec() (nome più moderno)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())
