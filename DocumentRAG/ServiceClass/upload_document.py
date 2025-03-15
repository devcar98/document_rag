import sys
import os
import pandas as pd
from DocumentRAG.TextPreProcessing.embeddings_creation import CreateEmbeddings
from DocumentRAG.FileOperations.fetch_extensions import FetchExtension
from DocumentRAG.FileOperations.file_operations import FileOperations
from DocumentRAG.TextPreProcessing.text_cleaning import TextCleaning
from DocumentRAG.TextPreProcessing.create_document_store import CreateDocument
from DocumentRAG.TextPreProcessing.document_cleaning import DocumentCleaning
from DocumentRAG.TextPreProcessing.document_splitting import DocumentSplitting
from DocumentRAG.VectorDatabase.vector_database_chroma import VectorDatabaseChroma
from DocumentRAG.EndPoints.DocumentRecord.record_document_logging import  RecordDocuments

class DocumentUpload:

    def __init__(self,file_obj,document_name,document_category,knowledge_base_param):
        """
        The Following Class would behave as the Parent Class for Uploading the Document
        """
        self.file_obj = file_obj
        self.document_name = document_name
        self.document_category = document_category
        self.knowledge_base_params = knowledge_base_param
        self.document_logging = RecordDocuments()

    def execute(self):

        extension_value = FetchExtension(self.file_obj)
        file_operation_obj = FileOperations(extension_value.extension, self.file_obj)
        extracted_text = file_operation_obj.file_operation_obj.extract_text()
        # Once the above Line Gets Executed, we Have the Text Extracted From it
        """
        The Extracted Text would be Going through the Following set of Steps
        
        1. Cleaning of Text
        2. Removal of Extra Spaces --> the Document Store Level
        3. Chunking
        """

        text_cleaning_obj = TextCleaning()
        extracted_text = text_cleaning_obj.clean_text(extracted_text)
        document_store_obj = CreateDocument(extracted_text)
        extracted_text = document_store_obj.extracted_data

        extracted_text = DocumentCleaning().document_cleaner(extracted_text)
        splitting_obj = DocumentSplitting()
        sentence_chunks = splitting_obj.split_sentence(extracted_text)
        paragraph_chunks = splitting_obj.split_paragraph(extracted_text)


        """
        Once the Paragraph Chunks are ready we can Create their Embeddings and Directly Store them in the Vector Database
        """
        embeddings_obj = CreateEmbeddings()
        sentence_embeddings = embeddings_obj.create_embeddings(sentence_chunks)
        paragraph_embeddings = embeddings_obj.create_embeddings(paragraph_chunks)

        """
        Once the Chunks are Ready, we can now Proceed towards adding the Data to the Vector Database
        """
        vector_database_obj = VectorDatabaseChroma(self.knowledge_base_params)
        vector_database_obj.insert_vector_embeddings(sentence_embeddings, self.document_name)
        vector_database_obj.insert_vector_embeddings(paragraph_embeddings, self.document_name)

        self.document_logging.add_records(self.document_name, self.knowledge_base_params)
        return None


















