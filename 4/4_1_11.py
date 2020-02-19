class File:
    def __init__(self, path):
        self.path = path
    def __add__(self, other_file):
        '''
        В этом случае создается новый файл и файловый объект, 
        в котором содержимое второго файла добавляется к содержимому первого файла. 
        Новый файл должен создаваться в директории, полученной с помощью tempfile.gettempdir. 
        Для получения нового пути можно использовать os.path.join.
        '''
        pass
    def __str__(self):
        return self.path
    def write(self, text):
        with open(self.path, 'w') as f:
            f.write(text)

myfile1 = File('temp1.log')
print(myfile1)
myfile2 = File('temp2.log')
print(myfile2)
myfile1.write('111')
myfile2.write('222')

