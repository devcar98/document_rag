from haystack.components.preprocessors import TextCleaner
from haystack.components.preprocessors import DocumentCleaner

class TextCleaning:

    def __init__(self, ):

        try:
            self.cleaner = TextCleaner(
                convert_to_lowercase=True,
                remove_punctuation=False,
                remove_numbers=False)

        except Exception as err:
            print("An Error occured while Creating with the Text Cleaning object",err)
            self.cleaner = None
    def clean_text(self, extracted_text):

        try:
            extracted_text = self.cleaner.run(texts=extracted_text)
            extracted_text = extracted_text["texts"]
            return extracted_text
        except Exception as err:
            extracted_text = []
        return extracted_text



