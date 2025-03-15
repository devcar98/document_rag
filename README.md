# Document Upload & Preprocessing Flow

## API Endpoint
- **Endpoint:** `POST /document/document_upload`
- **Description:** This endpoint is used to upload a document for preprocessing.
- **Headers:**
  - `user_id`: Identifies the user uploading the file.
  - `document_name`: The name of the document.
  - `document_category`: The category to which the document belongs.
  - `knowledge_base_param`: Parameter to segregate documents within different knowledge bases.
- **File:** The file being uploaded (only PDF files are supported).

---

## Flow of the Document Upload & Preprocessing

### 1. **User Uploads a Document**
   - The user triggers a POST request to `/document/document_upload` with the necessary headers and file.
   - The `user_id`, `document_name`, `document_category`, `knowledge_base_param`, and the `file` are sent in the request.

### 2. **Store File in the Working Directory**
   - Once the file is uploaded, it is read and stored in the working directory of the codebase.

### 3. **File Type Validation**
   - The system checks if the uploaded file is a PDF.
     - **If Not a PDF:** The process stops or returns an error message.
     - **If PDF:** Proceed to the next step.

### 4. **Text Extraction from PDF**
   - If the file is a valid PDF, the text is extracted from the document, with each page's text stored in a list.

### 5. **Text Cleaning - Stage 1: Lowercase Conversion**
   - The text extracted from the PDF is converted to lowercase for uniformity and to avoid case-sensitive issues.

### 6. **Create Document Store (using Haystack)**
   - The cleaned text is stored into a **Document Store** using components from the Haystack library. This step helps prepare the data for further processing.

### 7. **Text Cleaning - Stage 2: Junk Removal**
   - Additional cleaning steps are applied to remove irrelevant content:
     - Removal of extra spaces.
     - Removal of empty lines.
     - Removal of repeated substrings.

### 8. **Chunking the Document**
   - The cleaned document is then chunked into smaller sections for easier processing. The system performs two types of chunking:
     - **Sentence-Level Chunking**
     - **Paragraph-Level Chunking**
   - **Note:** To prevent loss of content, the chunks are created with overlapping sections.

### 9. **Create Vector Embeddings**
   - After chunking, the system creates vector embeddings using the **all-MiniLM-L6-v2** model provided by the Haystack Embedder Wrapper.

### 10. **Store Vector Embeddings in Chroma DB**
   - The generated vector embeddings are stored in a lightweight **Chroma DB**, which serves as the vector database for storing embeddings.
   - The `knowledge_base_param` from the request headers is used to segregate the embeddings within different knowledge bases.

### 11. **Log Document Information**
   - Finally, the system logs the document's name and its associated knowledge base. This log serves as a reference to track which document belongs to which knowledge base.

---

## Overview of the Document Flow

1. **User Uploads Document**  
   `POST /document/document_upload`

2. **Store File in Working Directory**

3. **Validate PDF Format**  
   - **If Not PDF:** Return Error  
   - **If PDF:** Proceed to Next Step

4. **Extract Text from PDF (Page-Level)**

5. **Text Cleaning - Stage 1: Lowercase Conversion**

6. **Create Document Store (using Haystack)**

7. **Text Cleaning - Stage 2: Junk Removal**  
   - Remove Extra Spaces  
   - Remove Empty Lines  
   - Remove Repeated Substrings

8. **Chunking (Sentence/Paragraph Level with Overlap)**

9. **Create Vector Embeddings (Using all-MiniLM-L6-v2)**

10. **Store Vectors in Chroma DB**  
    - Segregate by `knowledge_base_param`

11. **Log Document Information**  
    - Document Name & Knowledge Base

---

## 2. Documentation QnA API Flow

### API Endpoint
- **Endpoint:** `GET /document/document_qna`
- **Description:** This endpoint allows the user to ask a question related to a document, and the system will provide an answer based on the document's content.

### Headers:
- `question`: The question asked by the user (mandatory).
- `knowledge_base_param`: The knowledge base parameter used to segregate different knowledge bases.
- `document_name`: The name of the document for which the question is being asked.

---

### Flow of the Document QnA API

#### 1. **User Asks a Question**
   - The user submits a question along with the `knowledge_base_param` and `document_name` in the request headers.
   - The `document_qna` function is invoked.

#### 2. **Initialization of LLM Model**
   - The pipeline uses the **LLAMA 3.1 model** (pre-installed and initialized beforehand) for answering the questions.
   - This model is the core component responsible for processing and generating answers based on the context.

#### 3. **Match the Question with Vector Embeddings**
   - The system queries the **Chroma DB** to match the question with the relevant **vector embeddings** in the knowledge base.
   - The system retrieves the top **50 results** based on the vector similarity.

#### 4. **Create the Prompt**
   - After fetching the results, the system constructs a prompt to pass to the LLM (LLAMA 3.1 model). The format of the prompt is as follows:

I am giving you Some Context: Context: {results['documents'][0]} and a Question: {self.question}

Kindly answer the given question based on the Context Given to you, do not try to add information from your end.

graphql
Copy

#### 5. **Pass the Prompt to the LLM**
- The prompt is sent to the **LLAMA 3.1 model** for generating the response. The model processes the context and the question to generate a relevant answer.

#### 6. **Return the Answer to the User**
- The system returns the response to the user in the following format:

```json
{
  "text": "According to the context, binary search is mentioned as having a run time of o(log n), which means it's one of the fastest algorithms. However, there is no detailed explanation of what binary search is in the given text.",
  "additional_kwargs": {
    "tool_calls": []
  },
  "raw": {
    "model": "llama3.1",
    "created_at": "2025-03-02T07:38:25.269091Z",
    "done": true,
    "done_reason": "stop",
    "total_duration": 44375778583,
    "load_duration": 8036651250,
    "prompt_eval_count": 3900,
    "prompt_eval_duration": 32034000000,
    "eval_count": 47,
    "eval_duration": 4280000000,
    "message": {
      "role": "assistant",
      "content": "According to the context, binary search is mentioned as having a run time of o(log n), which means it's one of the fastest algorithms. However, there is no detailed explanation of what binary search is in the given text.",
      "images": null,
      "tool_calls": null
    },
    "usage": {
      "prompt_tokens": 3900,
      "completion_tokens": 47,
      "total_tokens": 3947
    }
  },
  "logprobs": null,
  "delta": null
}
```

## 3. Document Map API Flow

### API Endpoint
- **Endpoint:** `GET /documents/document_map`
- **Description:** This endpoint is used to read the CSV file containing the mapping of document names and their corresponding knowledge bases.

### Flow of the Document Map API

#### 1. **User Makes GET Request**
   - The user sends a `GET` request to `/documents/document_map`.
   - This request triggers the `document_map` function to be invoked.

#### 2. **Read CSV File**
   - The `ReadDocuments` class is invoked to read the CSV file.
   - The CSV contains the mapping of **document names** and their corresponding **knowledge base**.

#### 3. **Return Data**
   - The `ReadDocuments` class processes the CSV and returns the data, which contains the mapping between document names and their respective knowledge bases.

#### 4. **Response Format**
   - The data is returned to the user, typically in JSON format, containing the document names and associated knowledge base details.

---

### Overview of the Document Map API Flow

1. **User Requests Document Mapping**  
   - The user sends a `GET` request to `/documents/document_map`.
   
2. **Reading the CSV File**  
   - The system uses the `ReadDocuments` class to read the CSV file containing document name and knowledge base mappings.

3. **Return Data**  
   - The data, which contains document names and knowledge base associations, is returned as a response.

---

### Conclusion

This `GET /documents/document_map` API provides an easy way to retrieve the mapping between documents and their associated knowledge bases, using a CSV file as the source for this mapping.
