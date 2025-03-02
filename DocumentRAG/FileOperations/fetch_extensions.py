import sys
import os

class FetchExtension:

    def __init__(self,file_obj):
        try:
            self.file_obj = file_obj
            self.file_name = file_obj.filename
            self.extension = self.__determine_file_extension()
        except Exception as err:
            print("Unable to Determine the Extensions")
            self.extension = ""


    def __determine_file_extension(self, ):

        extension = ("")
        try:
            extension = self.file_name.split(".")[1]
        except Exception as err:
            print("Unable to Determint the Extension of the Document")
            extension = ""
        return extension
