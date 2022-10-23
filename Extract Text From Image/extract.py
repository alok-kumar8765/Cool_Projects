import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# this is the file exe loction of tessereact which was installed in your system

text = pytesseract.image_to_string(img)
print(text)