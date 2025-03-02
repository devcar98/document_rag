from haystack.components.preprocessors import DocumentCleaner

class DocumentCleaning:
    """
    The following set of Documents is used for the purpose of Cleaning the Text, but the
    the level of the Document.
    """
    def __init__(self):
        try:

            self.document_cleaner_obj = DocumentCleaner(keep_id= True,
                                                      ascii_only=True,
                                                      remove_empty_lines=True,
                                                      remove_extra_whitespaces=True,
                                                      remove_repeated_substrings=True
                                                    )
        except Exception as err:
            print("Error in Forming the Document Cleaner object", err)
            self.document_cleaner_obj = None

    def document_cleaner(self, documents):
        try:
            documents = self.document_cleaner_obj.run(documents)
            return documents['documents']
        except Exception as err:
            print('Error whole cleaning the documents')
            documents = []
            return documents


