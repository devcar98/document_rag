from fastapi import APIRouter, Form, UploadFile, File
from pydantic import BaseModel
from fastapi import Header, Body
from DocumentRAG.ServiceClass.upload_document import DocumentUpload
from DocumentRAG.ServiceClass.question_answer import QuestionAnswer
from DocumentRAG.ServiceClass.read_current_documents import ReadDocuments

router_preprocess = APIRouter()


# If you want to use a request body instead of form data, create a Pydantic model for the request
class DocumentRequest(BaseModel):
    user_id: str
    document_name: str
    document_category: str
    knowledge_base_param: str



@router_preprocess.get('/documents/document_map')
def document_map():
    read_docs = ReadDocuments()
    return read_docs.data



@router_preprocess.get("/document/QuestionAnswer")
def document_qna(
        question: str= Header(...,description="Mandatory Question"),
        knowledge_base_param = Header(...,description="Knowledge Base Param used for the Purpose of Seggregation"),
        document_name = Header(...,description="Document Name, it would be used to ")):
    print('The Function to Call the Class for Questions answering has been invoked')
    final_result = QuestionAnswer(question, document_name, knowledge_base_param).execute()
    return final_result


@router_preprocess.post("/document/document_upload")
def document_preprocess(
        user_id: str = Header(..., description="User ID to record the User who is uploading the file."),
        document_name: str = Header(..., description= "A Mandatory Name of the Document"),
        document_category: str = Header(description= "Category to which the Document belongs."),
        knowledge_base_param: str = Header(...,description ="Knowledge Base Paramter to Seggregate Different Knowledge Bases"),
        file: UploadFile = File(...),  # If you're uploading a file
):
    DocumentUpload(file,
                   document_name,
                   document_category,
                   knowledge_base_param).execute()


    # Example logic (you can replace with actual processing logic)
    return {
        "user_id": user_id,
        "document_name": document_name,
        "document_category": document_category,
        "knowledge_base_param": knowledge_base_param,
    }