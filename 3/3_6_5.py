class BookIOErrors(Exception):
    pass


class PageNotFoundError(BookIOErrors):
    pass


class TooLongTextError(BookIOErrors):
    pass


class PermissionDeniedError(BookIOErrors):
    pass


class NotExistingExtensionError(BookIOErrors):
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
    bookmark = {}

    def __init__(self, author, year, title, content=None):
        """конструктор"""
        super().__init__(title, content)
        self.author = author
        self.year = year

    def read(self, page):
        """возвращает страницу"""
        if page >= self.size or page < 0:
            raise PageNotFoundError
        return self.content[page]

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""
        if page >= self.size or page < 0:
            raise PageNotFoundError
        if person in Novel.bookmark:
            Novel.bookmark[person].append(page)
        else:
            Novel.bookmark[person] = [page]

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
        if person not in Novel.bookmark:
            raise PageNotFoundError
        return Novel.bookmark[person][-1]

    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""
        if person in Novel.bookmark:
            del Novel.bookmark[person]

    def write(self, page, text):
        """делает запись текста text на страницу page """
        raise PermissionDeniedError


class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""

    def __init__(self, title, size=12, max_sign=2000, content=None):
        """конструктор"""
        super().__init__(title, content)
        if self.content == []:
            self.size = size
            self.content = [''] * size
        self.max_sign = max_sign
        
    def __getattr__(self, name):
        raise NotExistingExtensionError


    def read(self, page):
        """возвращает страницу с номером page"""
        if page >= self.size or page < 0:
            raise PageNotFoundError
        return self.content[page]

    def write(self, page, text):
        """делает запись текста text на страницу с номером page """
        if page >= self.size or page < 0:
            raise PageNotFoundError
        if len(self.content[page]) + len(text) > self.max_sign:
            raise TooLongTextError
        self.content[page] = f'{self.content[page]}{text}'


class Person:
    """класс описывающий человека и методы работы с книгой"""

    def __init__(self, name):
        """конструктор"""
        self.name = name

    def read(self, book, page):
        """читаем страницу с номером page в книге book"""
        return book.read(page)

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""
        book.write(page, text)

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""
        book.set_bookmark(self, page)

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""
        return book.get_bookmark(self)

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""
        book.del_bookmark(self)


class AdvancedPerson(Person):
    def search(self, book, name_page):
        """возвращает номер страницы name_page из книги book"""
        return book.search(name_page)

    def read(self, book, page):
        if isinstance(page, int):
            return book.read(page)
        if isinstance(page, str):
            page_number = book.search(page)
            return book.read(page_number)

    def write(self, book, page, text):
        if isinstance(page, int):
            return book.write(page, text)
        if isinstance(page, str):
            page_number = book.search(page)
            return book.write(page_number, text)


class NovelWithTable(Novel):
    """класс - книга с оглавлением"""

    # def __init__(self, title, content=None, table=None):
    def __init__(self, author, year, title, content=None, table=None):
        """конструктор"""
        super().__init__(author, year, title, content)
        self.table = table or {}

    def search(self, name_page):
        """поиск по оглавлению, возвращает номер страницы запрашиваемой главы"""
        if name_page not in self.table:
            raise PageNotFoundError
        return self.table[name_page]

    def add_chapter(self, chapter, page):
        """добавляет главу и номер страницы в оглавлении"""
        # if page >= self.size or page < 0:
        #     raise PageNotFoundError
        self.table[chapter] = page

    def remove_chapter(self, chapter):
        """удаляет запись о главе в оглавлении"""
        if chapter not in self.table:
            raise PageNotFoundError
        del self.table[chapter]
