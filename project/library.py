from items import Book
from library_item import LibraryItem
from pprint import pprint
from utils import check_max_capacity, check_min_capacity, RestrictedDefaultDict

class Library:
    max_capacity = 5
    min_capacity = 2

    def __init__(self, name: str):
        self.lib_items = RestrictedDefaultDict(list)
        self.count = 0
        self.name = name

    
    @check_max_capacity
    def add_item(self, item: LibraryItem):
        item_type = Library.get_type(item)
        self.lib_items[item_type].append(item)
        self.count += 1
        item.set_library_hook(self)
        return True

    @check_min_capacity
    def borrow_item(self, item: LibraryItem):
        item_type = Library.get_type(item)
        self.lib_items[item_type].remove(item)
        self.count -= 1
        return True
    

    @staticmethod
    def get_type(item: LibraryItem):
        return item.__class__.__name__.lower() + 's'
    
    
    def details(self):
        print("Name:", self.name)
        pprint(dict(self.lib_items))

    
    def get_books(self): 
        return self.lib_items["books"]

    def get_newsp(self): 
        return self.lib_items["newspapers"]

    def get_magazines(self): 
        return self.lib_items["magazines"]