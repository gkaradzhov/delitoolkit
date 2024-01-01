import torch
from sentence_transformers import SentenceTransformer

class SbertPredictor():
    def __init__(self, model='all-distilroberta-v1'):
        self.model = SentenceTransformer(model)
        self.model.eval()
    def tokenize_and_predict(self, text):
        with torch.no_grad():
            return self.model.encode(text)

    def encode(self, text):
        with torch.no_grad():
            return self.model.encode(text)
