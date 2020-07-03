from calendar import TextCalendar

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

class Page:
    """класс страница"""

    def __init__(self, text=None, max_sign=2000):
        self._text = '' if text is None else text
        self.max_sign = max_sign
 
    def __str__(self):
        return self._text

    def __eq__(self, obj):
        if isinstance(obj, Page) or isinstance(obj, str):
            return len(self._text) == len(obj)
        raise TypeError

    def __lt__(self, obj):  # <
        if isinstance(obj, Page) or isinstance(obj, str):
            return len(self._text) < len(obj)
        raise TypeError

    def __le__(self, obj):  # <=
        if isinstance(obj, Page) or isinstance(obj, str):
            return len(self._text) <= len(obj)
        raise TypeError

    def __ne__(self, obj):  # !=
        if isinstance(obj, Page) or isinstance(obj, str):
            return len(self._text) != len(obj)
        raise TypeError

    def __gt__(self, obj):  # >
        if isinstance(obj, Page) or isinstance(obj, str):
            return len(self._text) > len(obj)
        raise TypeError

    def __ge__(self, obj):  # >=
        if isinstance(obj, Page) or isinstance(obj, str):
            return len(self._text) >= len(obj)
        raise TypeError

    def __len__(self):
        return len(self._text)

    def __add__(self, obj):
        if (not isinstance(obj, Page)) and (not isinstance(obj, str)):
            raise TypeError
        if len(self._text) + len(obj) > self.max_sign:
            raise TooLongTextError
        self._text = self._text + str(obj)
        return self

    def __radd__(self, obj):
        if (not isinstance(obj, Page)) and (not isinstance(obj, str)):
            raise TypeError
        return str(obj) + self._text


class Book:
    """класс книга"""

    def __init__(self, title, content=None):
        self.title = title
        self._content = [] if content is None else content

    def __eq__(self, obj):
        if not isinstance(obj, Book):
            raise TypeError
        return len(self._content) == len(obj)

    def __lt__(self, obj):  # <
        if not isinstance(obj, Book):
            raise TypeError
        return len(self._content) < len(obj)

    def __le__(self, obj):  # <=
        if not isinstance(obj, Book):
            raise TypeError
        return len(self._content) <= len(obj)

    def __ne__(self, obj):  # !=
        if not isinstance(obj, Book):
            raise TypeError
        return len(self._content) != len(obj)

    def __gt__(self, obj):  # >
        if not isinstance(obj, Book):
            raise TypeError
        return len(self._content) > len(obj)

    def __ge__(self, obj):  # >=
        if not isinstance(obj, Book):
            raise TypeError
        return len(self._content) >= len(obj)

    def __getitem__(self, index):
        if index < 1 or index > len(self):
            raise PageNotFoundError
        return self._content[index-1]

    def __setitem__(self, index, value):
        if index < 1 or index > len(self):
            raise PageNotFoundError
        self._content[index-1] = value

    def __len__(self):
        return len(self._content)

class CalendarBookmark:
    """класс дескриптор - закладка для ежедневника"""

    def __init__(self):
        self.bookmark = 0

    def __get__(self, obj, obj_type):
        return self.bookmark

    def __set__(self, obj, value):
        if value < 1 or value > len(obj):
            raise PageNotFoundError
        self.bookmark = value


class CalendarBook(Book):
    """класс книги - ежедневник с закладкой"""
    def __init__(self, title, content=None):
        content = []
        _year = int(title)
        _cal = TextCalendar()
        for month in range(1, 13):
            content.append(Page(_cal.formatmonth(_year, month)))
            for day in _cal.itermonthdates(_year, month):
                if day.month == month:
                    content.append(Page(str(day)))

        super().__init__(title, content)

    bookmark = CalendarBookmark()
