import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout


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


app = QApplication(sys.argv)
principal = MainWindow()
principal.show()
app.exec()

