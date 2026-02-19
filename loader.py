import pandas as pd
from pathlib import Path


class ExcelLoader:

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def load(self) -> pd.DataFrame:
        return pd.read_excel(self.file_path)