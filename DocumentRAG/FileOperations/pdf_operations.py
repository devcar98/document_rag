import os.path

from PyPDF2 import PdfReader
import os


class PDFOperations:

    def __init__(self, file_obj):
        self.file_path = os.path.join(os.getcwd(),file_obj.filename)
        with open(self.file_path,"wb") as f:
            content = file_obj.file.read()
            f.write(content)
        self.extracted_text = []

    def extract_text(self):
        try:
            print('Trying to Read the file path')
            pdf_obj = PdfReader(self.file_path)
            print('This is my pdf file path',self.file_path)
            counter = 0
            while counter < len(pdf_obj.pages[0:]):
                page_obj = pdf_obj.pages[counter]
                text = page_obj.extract_text()
                self.extracted_text.append(text)
                counter = counter +1

        except Exception as err:
            self.extracted_text = []
        return self.extracted_text