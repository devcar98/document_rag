import chromadb
import os

class VectorDatabaseChroma:
    """
    The Following Class would be used to Create a Vector Database and Store the embeddings into it.
    """
    def __init__(self,knowledge_base):
        try:
            self.chroma_db_client = chromadb.PersistentClient(path=os.getcwd())
            self.collection_obj = self.chroma_db_client.get_or_create_collection(name=f"KNOWLEDGE_BASE_{str(knowledge_base).upper()}",
                                                           metadata={
                                                               "hnsw:space": "cosine",
                                                               "hnsw:search_ef": 100
                                                           })
        except Exception as err:
            print("Error while Configuring the Vector Database", err)
            self.chroma_db_client = None
            self.collection_obj = None
    def insert_vector_embeddings(self,document_store,document_name):

        counter = 0
        while counter < len(document_store):
            content = document_store[counter].content
            embeddings = document_store[counter].embedding
            id = document_store[counter].id
            self.collection_obj.upsert(documents = [content],
                                    embeddings = [embeddings],
                                    metadatas = [{"DocumentName":document_name}],
                                    ids =[id])

            counter = counter + 1


    def fetch_embeddings(self,question):
        try:
            result = self.collection_obj.query(n_results = 50, query_texts = [question])
            return result
        except Exception as err:
            print("An Error Occured while Fetching the Embeddings")