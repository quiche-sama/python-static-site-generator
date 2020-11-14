from typing import List
from pathlib import Path


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        if extension in self.extensions:
            return True
        else:
            return False

    def parse(self, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, "r") as file:
            return file.read()


test
