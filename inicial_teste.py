import cv2
import pytesseract

# lendo img com opencv
img = cv2.imread("meu_nome.png")

# apontar onde esta o executavel do tesseract
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\Tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\Tesseract.exe"

resultado = pytesseract.image_to_string(img)

print(resultado)