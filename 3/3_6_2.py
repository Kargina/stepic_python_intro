class Matrix:
    MAX_SIZE = 1000  

    def __init__(self, max_size=None):
        self.size = max_size
        if max_size is None:
            self._matrix = [None]
        else:
            self._matrix = [[None] * max_size] * max_size

    def __str__(self):
        if self._matrix == [None]:
            return("None")
        matrix_str = ""
        for row in self._matrix:
            matrix_str += ' '.join([str(elem) for elem in row])
            matrix_str += '\n'
        matrix_str = matrix_str.rstrip('\n')
        return matrix_str
        


    def append(self, element=None):
        pass

    def pop(self):
        pass

    @classmethod
    def from_iter(cls, iter_obj, max_size=None):
        pass

test = Matrix(3)
print(test)
test.append(1)