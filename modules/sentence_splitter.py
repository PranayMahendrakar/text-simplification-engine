"""sentence_splitter module"""
from .base import LlamaClient
class SentenceSplitter:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You simplify complex text while preserving meaning and accuracy."
    def process(self, text: str, target_level: str = "high school") -> str:
        return self.client.generate(f"Simplify this text for {target_level} level:\n\n{text}\n\nPreserve key information while making it accessible.", self.system_prompt)
