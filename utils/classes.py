import pandas as pd
import os


class FileDataset():
    def __init__(self, file_path, delimiter=","):
        self.file_path = file_path
        self.delimiter = delimiter
        self.data = self._load_data()

    def _load_data(self):
        if os.path.splitext(self.file_path)[-1] == ".csv":
            data = pd.read_csv(self.file_path, delimiter=self.delimiter, header=0)
        else:
            raise ValueError(f"File format not supported: {self.file_path}")
        return data

    def preprocess(self):
        pass


