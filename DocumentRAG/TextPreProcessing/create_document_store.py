from haystack import Document
from haystack.components.writers import DocumentWriter

class CreateDocument:
    """
    The following class would be used to create the Document Object
    """

    def __init__(self, extracted_text):
        try:
            self.extracted_data = []
            counter = 0
            while counter < len(extracted_text):
                self.extracted_data.append((Document(content = extracted_text[counter])))
                counter = counter + 1
        except Exception as error:

            print("An Error occured during the Document Creation",error)


