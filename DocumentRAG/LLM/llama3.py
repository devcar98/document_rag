import torch
from transformers import LlamaTokenizer, LlamaForCausalLM

class LLAMA:

    def __init__(self,):
        from llama_index.llms.ollama import Ollama

        self.llm = Ollama(model="llama3.1", request_timeout=60.0)

    def execute(self, prompt):
        response = self.llm.complete(prompt)
        return response

