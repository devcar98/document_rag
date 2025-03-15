import pytest
from fastapi.testclient import TestClient
import os
from DocumentRAG.EndPoints.run import app


client = TestClient(app)
def testing_upload():

    """
    The following Test case is used to Check the Upload Functionality of the Documents
    :return:
    """
    file_path = os.path.join((os.getcwd()),'testnovel.pdf')
    print('This is my file path....',file_path)
    if not os.path.exists(file_path):
        print(f"File does not exist at {file_path}")
    else:
        print(f"File exists at {file_path}")
    with open(file_path, "rb") as f:
        response = client.post(
            "/document/document/document_upload",  # The endpoint to hit
            files={"file": ("test.pdf", f, "application/pdf")},  # Correct file structure
            headers={
                "accept": "application/json",
                "user-id": "1234",
                "document-name": "Doc",
                "document-category": "Doc",
                "knowledge-base-param": "TEST",
            },
        )
    print(response.json())

def testing_qna():

    """
    This Test case is for the purpose of Asking the Questions

    """
    headers = {
        "accept": "application/json",
        "question": "Miss Sutherland comes to Sherlock Holmes to ask for his help finding what ?",
        "knowledge-base-param": "TEST",
    }

    # Simulate the GET request using TestClient
    response = client.get("/document/document/QuestionAnswer", headers=headers)

    # Print response for debugging (optional)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

    headers = {
        "accept": "application/json",
        "question": "What Sherlock Holmes and Dr Watson have been talking about in the beginning of the novel ?",
        "knowledge-base-param": "TEST",
    }

    # Simulate the GET request using TestClient
    response = client.get("/document/document/QuestionAnswer", headers=headers)
    # Print response for debugging (optional)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())