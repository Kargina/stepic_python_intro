import tempfile
from datetime import datetime
import os


class File:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path

    def __add__(self, obj):
        current_time = datetime.now().strftime('%Y%m%d%H%M%S%f')
        temp_dir = tempfile.gettempdir()
        path_new_file = os.path.join(temp_dir, current_time)
        new_obj = File(path_new_file)
        with open(self.path) as f:
            with open(new_obj.path, "w") as f1:
                for line in f:
                    f1.write(line)
        with open(obj.path) as f:
            with open(new_obj.path, "a") as f1:
                for line in f:
                    f1.write(line)
        return new_obj

    def __iter__(self):
        self.__iter_current_line = 0
        with open(self.path) as f:
            self.__iter_content = f.readlines()
        for id, item in enumerate(self.__iter_content):
            self.__iter_content[id] = item.rstrip('\n')
        return self
        
    def __next__(self):
        if self.__iter_current_line >= len(self.__iter_content):
            raise StopIteration
        __curr_str = self.__iter_content[self.__iter_current_line]
        self.__iter_current_line += 1
        return __curr_str

    def write(self, text):
        with open(self.path, 'w') as f:
            f.write(text)
