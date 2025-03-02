from DocumentRAG.EndPoints.DocumentRecord.record_document_logging import  RecordDocuments

class ReadDocuments:

    def __init__(self):
        try:

            read_document_obj = RecordDocuments()
            self.data = read_document_obj.read_records()
            self.data = self.data.to_dict(orient='records')
        except Exception as err:
            print('Unable to read the csv', err)
