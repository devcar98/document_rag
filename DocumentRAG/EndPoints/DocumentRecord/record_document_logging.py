import pandas as pd
import os


class RecordDocuments:
    """
    The Following class would be used to record the documents that have been uploaded by the user,
     along with the knowledge base attached with it.
    """
    def __init__(self):
        try:
            self.df = pd.read_csv(filepath_or_buffer = os.path.join(os.getcwd(), "records.csv"))

        except Exception as err:
            print("OOPS seems like the CSV does not exist !!!!!, hence Creating one")
            record_docs_csv = pd.DataFrame(columns=["Document_Name", "Knowledge_Base"])
            record_docs_csv.to_csv(path_or_buf = os.path.join(os.getcwd(), "records.csv"), index=False)
            self.df = pd.read_csv(filepath_or_buffer= os.path.join(os.getcwd(), "records.csv"))
    def add_records(self,document_name, knowledge_base_name):

        try:
            document_name_list = list(self.df["Document_Name"])
            knowledge_base_name_list = list(self.df["Knowledge_Base"])

            document_name_list.append(document_name)
            knowledge_base_name_list.append(knowledge_base_name)

            self.df["Document_Name"] = document_name_list
            self.df["Knowledge_Base"] = knowledge_base_name_list
            self.df.to_csv(path_or_buf=os.path.join(os.getcwd(), "records.csv",),index=False)
        except Exception as err:
            print("Unable to Add the Records in the Database")

    def read_records(self,):

        try:
            data = pd.read_csv(filepath_or_buffer=os.path.join(os.getcwd(), "records.csv"))
            return data
        except Exception as err:
            print("No CSV Exist in the System !!!")
            return {}

