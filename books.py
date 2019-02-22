from random import choice
from datetime import datetime

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
        return self in Book.on_loan

    def current_due_date(self):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

    def borrow(self):
        if self.lent_out():
            loaned = False
        else:
            due_date = self.current_due_date()
            Book.on_shelf.remove(self)
            Book.on_loan.append(self)
            loaned = True
        return loaned

    def return_to_library(self):
        if not self.lent_out():
            returned = False
        else:
            Book.on_loan.remove(self)
            Book.on_shelf.append(self)
            returned = True
        return returned



sapiens = Book.create('Sapiens', 'Yuval Noah Harari', "9780099590088")
py_for_dummies = Book.create('Python for Dummies', 'Stef Maruch', '9781118084847')
great_expectations = Book.create('Great Expectations', 'Charles Dickens', '9781517717704')
#--------------------------------------------------------------------------------------------
print(Book.browse().title)
#--------------------------------------------------------------------------------------------
# print(len(Book.on_shelf))
# print(len(Book.on_loan))
# print(sapiens.lent_out())
print(sapiens.borrow())
print(Book.on_shelf)
print(Book.on_loan)
print(sapiens.return_to_library())
print(Book.on_loan)
print(Book.on_shelf)
