class FileReader:
    """simple class for reading from file"""
    def __init__(self, path):
        self.path = path
    def read(self):
        try:
            with open(self.path) as f:
                data = f.read()
                return data
        except FileNotFoundError:
            return("")
