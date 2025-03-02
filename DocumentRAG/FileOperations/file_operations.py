import sys
from DocumentRAG.FileOperations.pdf_operations import PDFOperations


class FileOperations:

    """
    The Following Class would be used to Re-Direct the Extensions to the actual PreProcessing of the Document
    """

    def __init__(self,file_extension, file_obj):

        self.file_extension = file_extension
        self.file_obj = file_obj
        self.file_operation_obj = self.__file_operation()

    def __file_operation(self):

        try:
            if self.file_extension == "pdf":
                file_operations_obj = PDFOperations(self.file_obj)
            else:
                print("Only PDF Files are supported as of now")
                file_operations_obj = None


        except Exception as err:
                print("Some Exception was raised in the File Operations Class Private Method")
                file_operations_obj = None
        return file_operations_obj