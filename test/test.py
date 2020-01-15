import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img2 = Image.open('imageB.bmp')


text2 = pytesseract.image_to_string(img2)


print(text2)
