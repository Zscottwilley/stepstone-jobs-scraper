thonimport json
from utils import save_json

class JsonExporter:
    def __init__(self, output_file):
        self.output_file = output_file

    def export(self, data):
        save_json(data, self.output_file)