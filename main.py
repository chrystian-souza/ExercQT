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

        self.lbl_resultado = QLabel()
        self.btn_calcular = QPushButton('Calcular')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_altura)
        layout.addWidget(self.txt_altura)
        layout.addWidget(self.lbl_largura)
        layout.addWidget(self.txt_largura)
        layout.addWidget(self.lbl_profundidade)
        layout.addWidget(self.txt_profundidade)
        layout.addWidget(self.lbl_resultado)
        layout.addWidget(self.btn_calcular)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.btn_calcular.clicked.connect(self.calcular_metro_cubico)

        # Largura * Altura * Profundidade

    def calcular_metro_cubico(self):
        resultado = str(
            float(self.txt_largura.text()) *
            float(self.txt_altura.text()) *
            float(self.txt_profundidade.text())
        )
        self.lbl_resultado.setText(f'O volume cúbico é: {resultado}')


app = QApplication(sys.argv)
principal = MainWindow()
principal.show()
app.exec()
