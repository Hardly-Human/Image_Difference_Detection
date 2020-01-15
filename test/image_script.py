import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img1 = Image.open('imageA.bmp')
img2 = Image.open('imageB.bmp')

text1 = pytesseract.image_to_string(img1)
text2 = pytesseract.image_to_string(img2)

file1 = open("result_images.txt",'w+')

file1.write("first image text : ")
file1.write(text1)
file1.write("\nsecond image text : ")
file1.write(text2)

file1.write("\nsimlarities in image : ")
if(len(text1) > len(text2)):
    file1.write(text2)
else:
    file1.write(text1)
    
file1.close()
