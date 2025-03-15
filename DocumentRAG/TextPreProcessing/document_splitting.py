from haystack.components.preprocessors import DocumentSplitter
import nltk



class DocumentSplitting:
    """
    The Following class would be used for the purpose of splitting the Documents
    """
    def __init__(self):

        try:
            nltk.download('punkt_tab')
            self.sentence_splitter_obj = DocumentSplitter(split_by='sentence',
                                                          split_length=5,
                                                          split_overlap=2)
            self.sentence_splitter_obj.warm_up()
            self.paragraph_splitter_obj = DocumentSplitter(split_by='passage',
                                                           split_overlap=1,
                                                           split_length=5)
            self.paragraph_splitter_obj.warm_up()
        except Exception as err:
            self.sentence_splitter_obj = None
            self.paragraph_splitter_obj = None
            print("Error while Creating the Document Splitting Object", err)

    def split_sentence(self, documents):

        try:
            documents = self.sentence_splitter_obj.run(documents)
            return documents['documents']
        except Exception as err:
            print("Error while Chunking", err)
            return None

    def split_paragraph(self, documents):

        try:
            documents = self.paragraph_splitter_obj.run(documents)
            return documents['documents']
        except Exception as err:
            print("Error while Chunking", err)
            return None

