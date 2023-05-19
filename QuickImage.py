__author__ = 'William Nascimento'
__version__ = "0.0.1"
__maintainer__ = "William Nascimento"
__status__ = "Development"


import cv2
import pytesseract
import subprocess
from PIL import ImageGrab


class QuickImage:
    """Classe facilitadora para a extração de textos de prints de tela."""

    def __init__(self):
        """Inicia a instância do objeto e configura os parâmetros iniciais."""
        self.text = None
        self.words = None
        self.img = None

    def get_image(self, filepath=None):
        """Define a imagem, de algum arquivo ou do clipboard."""
        if filepath is None:
            # COPIAR DO CLIPBOARD
            img = ImageGrab.grabclipboard()
            # or ImageGrab.grab() to grab the whole screen!
            img.save(r'imgs\paste.png', 'PNG')
            filepath = r'imgs\paste.png'
            pass
        # PEGAR DE UM LOCAL ESPECIFICO
        self.img = cv2.imread(filepath)
        pass

    def get_text(self):
        """Trata o texto e retorna em forma de string."""
        pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\Tesseract.exe"

        resultado = pytesseract.image_to_string(self.img)

        # TRATANDO A STRING RECEBIDA
        self.words = resultado.split()

        self.text = self._process_words(self.words)

        return self.text

    def add_to_clipboard(self):
        """Adiciona o texto para o cliboard do computador."""
        command = 'echo ' + self.text + '|clip'
        subprocess.run(command, shell=True)
        pass

    def _process_words(self, words):
        saida = ''
        for word in words:
            if word[len(word) - 1] == '-':
                saida += word
            else:
                saida += word + ' '
        return saida


# TESTES
if __name__ == "__main__":
    tool = QuickImage()
    tool.get_image()
    tool.get_text()
    tool.add_to_clipboard()
    pass
