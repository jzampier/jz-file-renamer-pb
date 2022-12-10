import os
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
        if self.pasta != '':
            #! Adquire uma lista de pastas com base no caminho capturado pela funcao selecionar pasta
            pastas_pocos = os.listdir(self.pasta)
            for poco in pastas_pocos:

                assuntos = os.listdir(r'{}/{}'.format(self.pasta, poco))
                # print(assuntos)

                for assunto in assuntos:

                    # *Acessa os arquivos que estão dentro de cada pasta assunto
                    files = os.listdir(r'{}/{}/{}'.format(self.pasta, poco, assunto))
                    i = 0
                    # ?Acessar cada arquivo dentro da sub-pasta
                    for file in files:

                        # *Pega o Nome do arquivo e sua extensão e guarda em 2 variaveis
                        nome_arquivo, extensao = os.path.splitext(file)

                        #!Renomeia o arquivo com o os.rename(nome_original_com_caminho , nome_alterado_com_caminho)
                        if i < 1:
                            os.rename(
                                r'{}/{}/{}/{}'.format(self.pasta, poco, assunto, file),
                                r'{}/{}/{}/{}_{}{}'.format(
                                    self.pasta, poco, assunto, poco, assunto, extensao
                                ),
                            )
                        else:
                            os.rename(
                                r'{}/{}/{}/{}'.format(self.pasta, poco, assunto, file),
                                r'{}/{}/{}/{}_{}_{}{}'.format(
                                    self.pasta,
                                    poco,
                                    assunto,
                                    poco,
                                    assunto,
                                    i,
                                    extensao,
                                ),
                            )
                        i += 1
            self.le_caminho.setText('')
            self.pasta = ''
            msg = QMessageBox()
            msg.setText('Arquivos renomeados com sucesso!')
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setText('Selecione uma pasta antes de prosseguir')
            msg.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
