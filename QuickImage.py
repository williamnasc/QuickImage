__author__ = 'William Nascimento'
__version__ = "0.0.0"
__maintainer__ = "William Nascimento"
__status__ = "Development"


import cv2
import pytesseract
import subprocess


class QuickImage:
    """Classe facilitadora para a extração de textos de prints de tela."""

    def __init__(self):
        """Inicia a instância do objeto e configura os parâmetros iniciais."""
        pass

    def get_image(self):
        """Define a imagem, de algum arquivo ou do clipboard."""
        pass

    def read_image(self):
        """Ler o texto contido na imagem."""
        pass

    def get_text(self):
        """Trata o texto e retorna em forma de string."""
        pass

    def add_to_clipboard(self):
        """Adiciona o texto para o cliboard do computador."""
        pass