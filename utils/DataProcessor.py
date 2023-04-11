from utils.Embedder import Embedder
from utils.JsonProcessor import JsonProcessor
from utils.TextProcessor import TextProcessor


class DataProcessor:
    def __init__(self, embedding_model: str) -> None:
        self.json_processor = JsonProcessor()
        self.text_processor = TextProcessor()
        self.embedder = Embedder(embedding_model)

    def process_json(self, json_string: str):
        return self.json_processor.process_json(json_string)

    def process_text(self, text: str):
        return self.text_processor.process_text(text)

    def generate_embedding(self, json_string: str):
        return self.json_processor.process_json(json_string)