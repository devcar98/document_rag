from haystack.components.embedders import SentenceTransformersDocumentEmbedder


class CreateEmbeddings:
    """
    The Following class is used for the purpose of Creation of the Document Embeddings
    """
    def __init__(self):
        try:
            self.embedding_obj = SentenceTransformersDocumentEmbedder(model="all-MiniLM-L6-v2")
            self.embedding_obj.warm_up()
        except Exception as err:
            self.embedding_obj = None
            print("Error while using the Create Embeddings Object", err)

    def create_embeddings(self, documents):
        try:
            embedded_documents = self.embedding_obj.run(documents)
            embedded_documents = embedded_documents['documents']
        except Exception as err:
            print("An Error Occured while Creating Embeddings of the Document",err)
            embedded_documents = None
        return embedded_documents