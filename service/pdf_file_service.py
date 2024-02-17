from PIL import Image
from io import BytesIO
import pytesseract
import PyPDF2


class PdfFileService:

    def __init__(self):
        print("Starting PdfFileService")

    # Linux setup
    # sudo apt-get update
    # sudo apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn

    # Windows setup
    # download binary from https://github.com/UB-Mannheim/tesseract/wiki. then add
    # pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

    def read_text_from_image(self, image_path):
        try:
            # Open an image file
            with Image.open(image_path) as img:
                # Perform OCR on the image
                pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
                text = pytesseract.image_to_string(img)
                return text
        except Exception as e:
            print("Error reading the image:", e)
            return None

    def read_pdf_file_by_path(self, pdf_path):
        text = ""
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                # Convert PDF page to image
                page_text = page.extract_text()
                # Append extracted text to the result
                text += page_text
        return text

    def read_pdf_file(self, pdf_content):
        text = ""
        with BytesIO(pdf_content) as f:
            reader = PyPDF2.PdfReader(f)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                # Convert PDF page to image
                page_text = page.extract_text()
                # Append extracted text to the result
                text += page_text
        return text
