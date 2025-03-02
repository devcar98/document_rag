from DocumentRAG.VectorDatabase.vector_database_chroma import VectorDatabaseChroma
from DocumentRAG.LLM.llama3 import LLAMA

class QuestionAnswer:

    def __init__(self, question, document_name, knowledge_base_param):

        try:
            self.question = question
            self.document_name = document_name
            self.knowledge_base_param = knowledge_base_param
            self.llm = LLAMA()

        except Exception as err:
            print('Error in the Question Answer Constructor Function')

    def execute(self):

        results = VectorDatabaseChroma(self.knowledge_base_param).fetch_embeddings(self.question)
        prompt = f"""
                    I am giving you Some Context:
                    Context: {results['documents'][0]}
                    and an Question: {self.question}
                    
                    Kindly answer the given question based on the Context Given to you, do not try to add information from you end.
                    
                    """
        final_result = self.llm.execute(prompt)
        return final_result


