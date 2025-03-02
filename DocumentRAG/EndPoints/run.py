import sys
import os
import uvicorn
import subprocess

from fastapi import FastAPI
from DocumentRAG.EndPoints.document_preprocess_routes import router_preprocess

app = FastAPI()
app.include_router(router_preprocess,prefix='/document')
ollama_process = subprocess.Popen(["ollama", "run", "llama3.1"],)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5049,workers=1)