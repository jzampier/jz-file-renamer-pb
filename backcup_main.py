import os
import shutil
from PyQt6.QtWidgets import *
from mainUI import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Purpose: Controlador
        """
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Renomeador de Arquivos')

        self.pasta = ''
        self.btn_sele_pasta.clicked.connect(self.selecionar_pasta)
        self.btn_renomear.clicked.connect(self.renomear_arquivos)

    def selecionar_pasta(self):
        """
        Purpose: abre a janela e salva o caminho da pasta
        """
        self.pasta = QFileDialog.getExistingDirectory(
            self,
            'Selecionar Pasta',
            '/home',
            QFileDialog.Option.ShowDirsOnly | QFileDialog.Option.DontResolveSymlinks,
        )
        self.le_caminho.setText(self.pasta)
        self.pasta = str(self.pasta)

    def renomear_arquivos(self):
        """
        Purpose:Percorre as subpastas e renomeia os arquivos de acordo com a pasta mãe.
        """
        #! Adquire uma lista de pastas com base no caminho capturado pela funcao selecionar pasta
        folders = os.listdir(self.pasta)
        for folder in folders:

            # *Adquire uma lista de arquivos que está dentro de cada subpasta
            files = os.listdir(r'{}/{}'.format(self.pasta, folder))

            # ?Acessar cada arquivo dentro da sub-pasta
            for file in files:

                # *Pega o Nome do arquivo e sua extensão e guarda em 2 variaveis
                nome_arquivo, extensao = os.path.splitext(file)

                #!Renomeia o arquivo com o os.rename(nome_original_com_caminho , nome_alterado_com_caminho)
                os.rename(
                    r'{}/{}/{}'.format(self.pasta, folder, file),
                    r'{}/{}/{}_{}{}'.format(
                        self.pasta, folder, folder, nome_arquivo, extensao
                    ),
                )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
