import pytesseract
from PIL import Image
img = Image.open("file.jpeg")

text = pytesseract.image_to_string(img,lang='eng')

print(text)