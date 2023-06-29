from library import Library
from items import Book, Newspaper, Magazine
from user import admin
from utils import gen_id
from borrow_proto import Borrowable

new_id = gen_id()

b1 = Book(next(new_id), "Book1", "me", "novel")
b2 = Book(next(new_id), "Book2", "me", "novel")
b3 = Book(next(new_id), "Book3", "me", "novel")
b11 = Book(next(new_id), "Book11", "me", "fiction")
b22 = Book(next(new_id), "Book22", "me", "fiction")
b33 = Book(next(new_id), "Book33", "me", "biography")

n1 = Newspaper(next(new_id), "TOI")
n2 = Newspaper(next(new_id), "The Hindu")


m1 = Magazine(next(new_id), "the economist", "finance")
m1 = Magazine(next(new_id), "vogue", "consumer")

# b3.info()

def borrow(item: Borrowable):
    item.borrow(admin)

def submit(item: Borrowable):
    item.return_back()

def details(lib):
    return lib.details()

def search_by_title(lib: 'Library', title: str):
    items = []
    items.extend(lib.get_books())
    items.extend(lib.get_magazines())
    items.extend(lib.get_newsp())
    return list(filter(lambda item: item.title == title, items))


lib_one = Library("#1")

lib_one.add_item(b1)
lib_one.add_item(b2)
lib_one.add_item(b3)
lib_one.add_item(n1)
lib_one.add_item(n2)
lib_one.add_item(m1)

print(search_by_title(lib_one, "Book1"))