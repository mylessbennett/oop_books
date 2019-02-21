from random import choice
class Book:
    """ Keeps track of books on shelf and books on loan and their due dates """

    on_shelf = []
    on_loan = []

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    @classmethod
    def create(cls, title, author, isbn):
        new_book = Book(title, author, isbn)
        cls.on_shelf.append(new_book)
        return new_book

    @classmethod
    def browse(cls):
        random_book = choice(cls.on_shelf)
        return random_book

    def lent_out(self):
        return self in Book.on_shelf

sapiens = Book.create('Sapiens', 'Yuval Noah Harari', "9780099590088")
py_for_dummies = Book.create('Python for Dummies', 'Stef Maruch', '9781118084847')
great_expectations = Book.create('Great Expectations', 'Charles Dickens', '9781517717704')
#--------------------------------------------------------------------------------------------
print(Book.browse().title)

print(len(Book.on_shelf))
print(len(Book.on_loan))
print(sapiens.lent_out())
