import os
from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        #directory = os.path.join(self.dest, path.relative_to(self.source))
        directory = self.dest + "/" + path.relative_to(self.source)
