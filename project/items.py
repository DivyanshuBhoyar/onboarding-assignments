from dataclasses import dataclass
from library_item import LibraryItem
from pprint import pprint
from user import User
from typing import Protocol

#book
@dataclass
class Book(LibraryItem):
    id: str
    title: str
    author: str
    category: str
    lib_ref = None    

    def info(self):
        print('Book item with info:')
        pprint(self.__dict__)

    
    def category(self):
        print(self.category)

    def set_library_hook(self, lib):
        self.lib_ref = lib
        print(f"item with id {self.id} is in library {lib.name} ")

    def borrow(self, user):
        if self.lib_ref.borrow_item(self):
            print(f"user <{user.name}> borrowed <{self.title}>")
        else: 
            print("could not borrow")

    def return_back(self):
        if self.lib_ref.add_item(self):
            print("returned")
        else:
            print("could not return")

    

@dataclass
class Newspaper(LibraryItem):
    id: str
    title: str
    lib_ref = None

    def info(self):
        print('newspaper with details:')
        pprint(self.__dict__)

    def category(self):
        return "Generic Newspaper"

    def set_library_hook(self, lib):
        self.lib_ref = lib
        print(f"item with id {self.id} is in library {lib.name} ")


@dataclass
class Magazine(LibraryItem):
    id: str
    title: str
    category: str
    lib_ref = None

    def info(self):
        print('Magazine item with info:')
        pprint(self.__dict__)

    def category(self):
        print(self.category)    

    def set_library_hook(self, lib):
        self.lib_ref = lib
        print(f"item with id {self.id} is in library {lib.name} ")

    def borrow(self, user):
        if self.lib_ref.borrow_item(self):
            print(f"user <{user.name}> borrowed <{self.title}>")
        else: 
            print("could not borrow")

    def return_back(self):
        if self.lib_ref.add_item(self):
            print("returned")
        else: 
            print("could not return")

