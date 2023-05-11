import cv2
import pytesseract
import subprocess

# lendo img com opencv
# img = cv2.imread("meu_nome.png")
img = cv2.imread(r"imgs\paste.png")

# apontar onde esta o executavel do tesseract
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\Tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\Tesseract.exe"

resultado = pytesseract.image_to_string(img)

# TRATANDO A STRING RECEBIDA
s = resultado.split()
saida = ''
for word in s:
    if word[len(word)-1] == '-':
        saida += word
    else:
        saida += word+' '
print(saida)

# ADICIONANDO A STRING AO CLIPBOARD
command = 'echo '+saida+'|clip'
subprocess.run(command, shell=True)