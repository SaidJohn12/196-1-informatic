class Book:
    def __init__(self, title, author, isbn, year, pages):
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")

        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.pages = pages

        self._is_available = True
        self._last_read_pages = 0

    @property
    def is_available(self):
        return self._is_available

    @property
    def last_read_pages(self):
        return self._last_read_pages

    def borrow(self):
        if not self._is_available:
            raise ValueError("Книга уже выдана")
        self._is_available = False

    def give_back(self, pages_read):
        if self._is_available:
            raise ValueError("Книга и так на полке")
        if not (0 <= pages_read <= self.pages):
            raise ValueError(f"Количество прочитанных страниц должно быть от 0 до {self.pages}")

        self._is_available = True
        self._last_read_pages = pages_read

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.year < other.year

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.isbn!r}, {self.year}, {self.pages})"


class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.pages_read = 0


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def find_by_isbn(self, isbn):
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None

    def find_by_author(self, author):
        return [book for book in self._books if book.author == author]

    def lend(self, isbn, reader):
        book = self.find_by_isbn(isbn)
        if book is None:
            raise KeyError("Такой книги нет в фонде")

        if not book.is_available:
            raise ValueError("Книга уже выдана")

        book.borrow()
        reader.books.append(book)

    def take_back(self, isbn, reader, pages_read):
        book = self.find_by_isbn(isbn)

        if book not in reader.books:
            raise ValueError("У читателя нет этой книги")

        try:
            book.give_back(pages_read)
        except ValueError as e:
            raise ValueError(e)

        reader.books.remove(book)
        reader.pages_read += pages_read

    def available(self):
        return [book for book in self._books if book.is_available]

    def unfinished(self):
        result = []
        for book in self._books:
            if book.is_available:
                last_read = book.last_read_pages
                if 0 < last_read < book.pages:
                    result.append(book)
        return result

    def __len__(self):
        return len(self._books)