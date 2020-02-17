
class BookIOErrors(Exception):
    '''Base error class'''
    pass
class PageNotFoundError(BookIOErrors):
    '''Page Not Found Error'''
    pass
class TooLongTextError(BookIOErrors):
    '''Too Long Text Error'''
    pass
class PermissionDeniedError(BookIOErrors):
    '''Permission Denied Error'''
    pass
class NotExistingExtensionError(BookIOErrors):
    '''Not Existing Extension Error'''
    pass


class Book:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def read(self, page):
        raise NotImplementedError

    def write(self, page, text):
        raise NotImplementedError


class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""

    def __init__(self, author, year, title, content = None):
        """конструктор"""
        super().__init__(title, content)
        self.author = author
        self.year = year

    def read(self, page):
        """возвращает страницу"""
        if len(self.content) < page or page <= 0:
                raise PageNotFoundError
        element = page-1
        print(self.content[element])

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""

    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""

    def write(self, page, text):
        """нельзя писать в книгу """
        raise PermissionDeniedError
        # print(f'page - {page}')
        # print(f'page-1 - {page-1}')
        # if len(self.content) < page or page <= 0:
        #         raise PageNotFoundError
        # element = page-1
        # print(f'el - {element}')
        # self.content[element] = text


class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""

    def __init__(self, title, size=12, max_sign=2000, content=None):
        """конструктор"""
        super().__init__(title, content)
        self.size = size
        self.max_sign = max_sign

    def read(self, page):
        """возвращает страницу с номером page"""
        if len(self.content) < page or page <= 0:
                raise PageNotFoundError
        element = page-1
        print(self.content[element])

    def write(self, page, text):
        """делает запись текста text на страницу с номером page """
        if len(self.content) < page or page <= 0:
                raise PageNotFoundError
        element = page-1
        self.content[element] = text


class Person:
    """класс описывающий человека и методы работы с книгой"""

    def __init__(self, name):
        """конструктор"""
        self.name = name

    def read(self, book, page):
        """читаем страницу с номером page в книге book"""
        book.read(page)

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""
        book.write(page, text)

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""

mynovel = Novel("some author", 1992, "some title", ['list1', 'list2', 'list3', 'list4'])
# mynovel = Novel("some author", 1992, "some title")
# print(mynovel.author)
# print(mynovel.year)
# print(mynovel.title)
# print(mynovel.content)
# print(mynovel.write(5, 'sometext'))
# print(mynovel.content)


mynovel.read(-3)

person = Person('Name')
person.read(mynovel, 0)