from PyQt5 import QtCore, QtGui, QtWidgets
from forca_internal import Forca_Internal
import os

#função para obter o path dentro do pyinstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

icon_path = resource_path("media\icon.png")

class Ui_Jogo_da_Forca(object):
    
     

    def __init__(self):
         self.jogo = Forca_Internal()
         self.adivinhar = self.jogo.adivinhar




    def setupUi(self, Jogo_da_Forca): 
        #Configuração da janela


        Jogo_da_Forca.setObjectName("Jogo_da_Forca")
        Jogo_da_Forca.resize(680, 400)
        Jogo_da_Forca.setMinimumSize(QtCore.QSize(680, 400))
        Jogo_da_Forca.setMaximumSize(QtCore.QSize(680, 400))
        icon = QtGui.QIcon()
        icon.addFile(icon_path, QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Jogo_da_Forca.setWindowIcon(icon)
        Jogo_da_Forca.setAutoFillBackground(False)
        Jogo_da_Forca.setFrameShadow(QtWidgets.QFrame.Plain)
        #Tela de início


        self.tela_inicio = QtWidgets.QWidget()
        self.tela_inicio.setObjectName(u"tela_inicio")
        self.titulo = QtWidgets.QLabel(self.tela_inicio)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QtCore.QRect(130, -20, 581, 181))
        self.jogar = QtWidgets.QPushButton(self.tela_inicio, clicked=startgame)
        self.jogar.setObjectName(u"jogar")
        self.jogar.setGeometry(QtCore.QRect(430, 290, 201, 81))
        self.jogar.setStyleSheet(u"font: 900 36pt \"Segoe UI Black\";\n"
"color: rgb(188, 112, 255);")
        self.chances_text = QtWidgets.QLabel(self.tela_inicio)
        self.chances_text.setObjectName(u"chances_text")
        self.chances_text.setGeometry(QtCore.QRect(10, 300, 201, 51))
        self.chances_select = QtWidgets.QSpinBox(self.tela_inicio)
        self.chances_select.setObjectName(u"chances_select")
        self.chances_select.setGeometry(QtCore.QRect(220, 300, 71, 51))
        self.chances_select.setStyleSheet(u"font: 700 28pt \"Segoe UI\";")
        self.chances_select.setWrapping(False)
        self.chances_select.setFrame(True)
        self.chances_select.setReadOnly(False)
        self.chances_select.setAccelerated(True)
        self.chances_select.setProperty("showGroupSeparator", False)
        self.chances_select.setMinimum(1)
        self.chances_select.setMaximum(26)
        self.chances_select.setValue(5)
        Jogo_da_Forca.addWidget(self.tela_inicio)
        
        
        #tela de jogo
        self.tela_jogo = QtWidgets.QWidget()
        self.tela_jogo.setObjectName("tela_jogo")
        
        #botões


        self.A = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["A"], "a"))
        self.A.setGeometry(QtCore.QRect(20, 200, 51, 51))
        self.A.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.A.setObjectName("A")
        self.B = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["B"], "b"))
        self.B.setGeometry(QtCore.QRect(70, 200, 51, 51))
        self.B.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.B.setObjectName("B")
        self.C = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["C"], "c"))
        self.C.setGeometry(QtCore.QRect(120, 200, 51, 51))
        self.C.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.C.setObjectName("C")
        self.D = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["D"], "d"))
        self.D.setGeometry(QtCore.QRect(170, 200, 51, 51))
        self.D.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.D.setObjectName("D")
        self.E = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["E"], "e"))
        self.E.setGeometry(QtCore.QRect(220, 200, 51, 51))
        self.E.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.E.setObjectName("E")
        self.F = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["F"], "f"))
        self.F.setGeometry(QtCore.QRect(270, 200, 51, 51))
        self.F.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.F.setObjectName("F")
        self.G = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["G"], "g"))
        self.G.setGeometry(QtCore.QRect(320, 200, 51, 51))
        self.G.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.G.setObjectName("G")
        self.H = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["H"], "h"))
        self.H.setGeometry(QtCore.QRect(370, 200, 51, 51))
        self.H.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.H.setObjectName("H")
        self.I = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["I"], "i"))
        self.I.setGeometry(QtCore.QRect(420, 200, 51, 51))
        self.I.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.I.setObjectName("I")
        self.J = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["J"], "j"))
        self.J.setGeometry(QtCore.QRect(470, 200, 51, 51))
        self.J.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.J.setObjectName("J")
        self.K = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["K"], "k"))
        self.K.setGeometry(QtCore.QRect(520, 200, 51, 51))
        self.K.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.K.setObjectName("K")
        self.L = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["L"], "l"))
        self.L.setGeometry(QtCore.QRect(570, 200, 51, 51))
        self.L.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.L.setObjectName("L")
        self.M = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["M"], "m"))
        self.M.setGeometry(QtCore.QRect(620, 200, 51, 51))
        self.M.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.M.setObjectName("M")
        self.N = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["N"], "n"))
        self.N.setGeometry(QtCore.QRect(20, 250, 51, 51))
        self.N.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.N.setObjectName("N")
        self.O = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["O"], "o"))
        self.O.setGeometry(QtCore.QRect(70, 250, 51, 51))
        self.O.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.O.setObjectName("O")
        self.P = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["P"], "p"))
        self.P.setGeometry(QtCore.QRect(120, 250, 51, 51))
        self.P.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.P.setObjectName("P")
        self.Q = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["Q"], "q"))
        self.Q.setGeometry(QtCore.QRect(170, 250, 51, 51))
        self.Q.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.Q.setObjectName("Q")
        self.R = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["R"], "r"))
        self.R.setGeometry(QtCore.QRect(220, 250, 51, 51))
        self.R.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.R.setObjectName("R")
        self.S = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["S"], "s"))
        self.S.setGeometry(QtCore.QRect(270, 250, 51, 51))
        self.S.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.S.setObjectName("S")
        self.T = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["T"], "t"))
        self.T.setGeometry(QtCore.QRect(320, 250, 51, 51))
        self.T.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.T.setObjectName("T")
        self.U = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["U"], "u"))
        self.U.setGeometry(QtCore.QRect(370, 250, 51, 51))
        self.U.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.U.setObjectName("U")
        self.V = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["V"], "v"))
        self.V.setGeometry(QtCore.QRect(420, 250, 51, 51))
        self.V.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.V.setObjectName("V")
        self.W = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["W"], "w"))
        self.W.setGeometry(QtCore.QRect(470, 250, 51, 51))
        self.W.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.W.setObjectName("W")
        self.X = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["X"], "x"))
        self.X.setGeometry(QtCore.QRect(520, 250, 51, 51))
        self.X.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.X.setObjectName("X")
        self.Y = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["Y"], "y"))
        self.Y.setGeometry(QtCore.QRect(570, 250, 51, 51))
        self.Y.setStyleSheet("font: 700 22pt \"Segoe UI\";")
        self.Y.setObjectName("Y")
        self.Z = QtWidgets.QPushButton(self.tela_jogo, clicked=lambda: escolher(letras["Z"], "z"))
        self.Z.setObjectName(u"Z")
        self.Z.setGeometry(QtCore.QRect(620, 250, 51, 51))
        self.Z.setStyleSheet(u"font: 700 22pt \"Segoe UI\";")

        #palavra a ser descoberta e chances


        self.texto = QtWidgets.QLabel(self.tela_jogo)
        self.texto.setGeometry(QtCore.QRect(30, 80, 611, 111))
        self.texto.setObjectName("texto")
        self.chances_show = QtWidgets.QLabel(self.tela_jogo)
        self.chances_show.setObjectName(u"chances_show")
        self.chances_show.setGeometry(QtCore.QRect(30, 20, 291, 61))
        self.chances_show.setStyleSheet(u"")
        Jogo_da_Forca.addWidget(self.tela_jogo)

        #Tela final

        self.tela_derrota = QtWidgets.QWidget()
        self.tela_derrota.setObjectName(u"tela_derrota")
        self.status = QtWidgets.QLabel(self.tela_derrota)
        self.status.setObjectName(u"derrota")
        self.status.setGeometry(QtCore.QRect(130, 30, 441, 121))
        self.status.setStyleSheet(u"font: 48pt \"Segoe UI\";\n"
"color: rgb(255, 0, 0);")
        self.palavra_correta = QtWidgets.QLabel(self.tela_derrota)
        self.palavra_correta.setObjectName(u"derrota_correta")
        self.palavra_correta.setGeometry(QtCore.QRect(30, 190, 641, 121))
        self.palavra_correta.setStyleSheet(u"font: 48pt \"Segoe UI\";")
        self.sair = QtWidgets.QPushButton(self.tela_derrota, clicked=quit)
        self.sair.setObjectName(u"sair")
        self.sair.setGeometry(QtCore.QRect(20, 310, 231, 51))
        self.sair.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        self.retry = QtWidgets.QPushButton(self.tela_derrota, clicked=retry)
        self.retry.setObjectName(u"retry")
        self.retry.setGeometry(QtCore.QRect(385, 310, 285, 51))
        self.retry.setStyleSheet(u"font: 700 20pt \"Segoe UI\";")
        Jogo_da_Forca.addWidget(self.tela_derrota)

        self.retranslateUi(Jogo_da_Forca)
        Jogo_da_Forca.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Jogo_da_Forca)

        #dicionário com os botões
        self.letras = {
          "A" : self.A, "B" : self.B, "C" : self.C, "D" : self.D, "E" : self.E,
              "F" : self.F, "G" : self.G, "H" : self.H, "I" : self.I, "J" : self.J,
              "K" : self.K, "L" : self.L, "M" : self.M, "N" : self.N, "O" : self.O, 
              "P" : self.P, "Q" : self.Q, "R" : self.R, "S" : self.S, "T" : self.T,
               "U" : self.U, "V" : self.V, "W" : self.W, "X" : self.X, "Y" : self.Y,
               "Z" : self.Z
         }
        letras = self.letras

     #TranslateUi

    def retranslateUi(self, Jogo_da_Forca):
                

        _translate = QtCore.QCoreApplication.translate
        Jogo_da_Forca.setWindowTitle(QtCore.QCoreApplication.translate("Jogo_da_Forca", u"Jogo da Forca", None))
        self.titulo.setText(QtCore.QCoreApplication.translate("Jogo_da_Forca", u"<html><head/><body><p><span style=\" font-size:48pt;\">Jogo da Forca</span></p></body></html>", None))
        self.jogar.setText(QtCore.QCoreApplication.translate("Jogo_da_Forca", u"Jogar", None))
        self.chances_text.setText(QtCore.QCoreApplication.translate("Jogo_da_Forca", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:700;\">Chances</span></p></body></html>", None))
        self.A.setText(_translate("Jogo_da_Forca", "A"))
        self.B.setText(_translate("Jogo_da_Forca", "B"))
        self.C.setText(_translate("Jogo_da_Forca", "C"))
        self.D.setText(_translate("Jogo_da_Forca", "D"))
        self.E.setText(_translate("Jogo_da_Forca", "E"))
        self.F.setText(_translate("Jogo_da_Forca", "F"))
        self.G.setText(_translate("Jogo_da_Forca", "G"))
        self.H.setText(_translate("Jogo_da_Forca", "H"))
        self.I.setText(_translate("Jogo_da_Forca", "I"))
        self.J.setText(_translate("Jogo_da_Forca", "J"))
        self.K.setText(_translate("Jogo_da_Forca", "K"))
        self.L.setText(_translate("Jogo_da_Forca", "L"))
        self.M.setText(_translate("Jogo_da_Forca", "M"))
        self.N.setText(_translate("Jogo_da_Forca", "N"))
        self.O.setText(_translate("Jogo_da_Forca", "O"))
        self.P.setText(_translate("Jogo_da_Forca", "P"))
        self.Q.setText(_translate("Jogo_da_Forca", "Q"))
        self.R.setText(_translate("Jogo_da_Forca", "R"))
        self.S.setText(_translate("Jogo_da_Forca", "S"))
        self.T.setText(_translate("Jogo_da_Forca", "T"))
        self.U.setText(_translate("Jogo_da_Forca", "U"))
        self.V.setText(_translate("Jogo_da_Forca", "V"))
        self.W.setText(_translate("Jogo_da_Forca", "W"))
        self.X.setText(_translate("Jogo_da_Forca", "X"))
        self.Y.setText(_translate("Jogo_da_Forca", "Y"))
        self.Z.setText(_translate("Jogo_da_Forca", "Z"))
        self.texto.setText(_translate("Jogo_da_Forca", f"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">{self.jogo.adivinhando}</span></p></body></html>"))
        self.chances_show.setText(QtCore.QCoreApplication.translate("Jogo_da_Forca", u"<html><head/><body><p><span style=\" font-size:28pt;\">chances: 5</span></p></body></html>", None))
        self.status.setText(QtCore.QCoreApplication.translate("Jogo_da_Forca", u"<html><head/><body><p>Você perdeu!</p></body></html>", None))
        self.palavra_correta.setText(QtCore.QCoreApplication.translate("Jogo_da_Forca", f"<html><head/><body><p><span style=\" font-size:20pt;\">A palavra correta era: {self.jogo.palavra}</span></p></body></html>", None))
        self.sair.setText(QtCore.QCoreApplication.translate("Jogo_da_Forca", u"Sair", None))
        self.retry.setText(QtCore.QCoreApplication.translate("Jogo_da_Forca", u"Jogar novamente", None))

#lista dos botões que precisam ser reativados
ativar = []
     

def escolher(botao: QtWidgets.QPushButton, letra: str) -> None:
     """parametro botao: usado para armazenar os botões já previamente apertados
        parametro letra: usado para buscar pela letra na palavra escolhida
        retorna: None
        adiciona os botões desativados em uma lista para ativar reativar no retry

     """
     ativar.append(botao)
     botao.setDisabled(True)
     ui.jogo.findletra(letra)
     ui.chances_show.setText(f"<html><hea/><body><p><span style=\" font-size:28pt;\">chances: {ui.jogo.chances}</span></p></body></html>")
     gamestatus()


def gamestatus() -> None:
     """checa as chances do jogador ou se a palavra já foi completa
        para finalizar o jogo.
        Caso esteja sem chances ou a palavra já tenha sido completa
        avança para a página final de vitória ou derrota.
     """

     if ui.jogo.palavra == "".join(ui.jogo.adivinhar):
          ui.status.setStyleSheet(u"font: 48pt \"Segoe UI\";\n"
"color: rgb(0, 255, 0);")
          ui.status.setText(u"<html><head/><body><p>Você venceu!</p></body></html>")
          Jogo_da_Forca.setCurrentIndex(2)
     ui.texto.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">{ui.jogo.adivinhando}</span></p></body></html>")
     if ui.jogo.chances == 0:
          Jogo_da_Forca.setCurrentIndex(2)



def startgame() -> None:
     """inicializa as chances do jogador, armazena na classe
     forca_internal e avança para a página do jogo.
     """
     global chances
     chances = ui.chances_select.value()
     ui.jogo.chances = chances
     ui.chances_show.setText(f"<html><head/><body><p><span style=\" font-size:28pt;\">chances: {ui.jogo.chances}</span></p></body></html>")
     Jogo_da_Forca.setCurrentIndex(1)

def quit() -> None:
     """Fecha o aplicativo."""
     sys.exit(app.exec_())

def retry() -> None:
          """Reinicia o programa"""
          ui.__init__()
          ui.jogo.__init__()
          ui.texto.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">{ui.jogo.adivinhando}</span></p></body></html>")
          ui.palavra_correta.setText(f"<html><head/><body><p><span style=\" font-size:20pt;\">A palavra correta era: {ui.jogo.palavra}</span></p></body></html>")
          for botoes in ativar:
               botoes.setDisabled(False)
          Jogo_da_Forca.setCurrentIndex(0)

#inicialização
import sys
app = QtWidgets.QApplication(sys.argv)
Jogo_da_Forca = QtWidgets.QStackedWidget()
ui = Ui_Jogo_da_Forca()
ui.setupUi(Jogo_da_Forca)
Jogo_da_Forca.show()
sys.exit(app.exec_())
