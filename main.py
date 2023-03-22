import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Cálculo de dentro cúbico')

        self.lbl_altura = QLabel('Altura')
        self.txt_altura = QLineEdit()

        self.lbl_largura = QLabel('Largura')
        self.txt_largura = QLineEdit()

        self.lbl_profundidade = QLabel('Prufundidade')
        self.txt_profundidade = QLineEdit()

        self.lbl_resultade = QLabel()
        self.btn_calcular = QPushButton('Calcular')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_altura)
        layout.addWidget(self.txt_altura)
        layout.addWidget(self.lbl_largura)
        layout.addWidget(self.txt_largura)
        layout.addWidget(self.lbl_profundidade)
        layout.addWidget(self.txt_profundidade)
        layout.addWidget(self.lbl_resultade)
        layout.addWidget(self.btn_calcular)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)
principal = MainWindow()
principal.show()
app.exec()

