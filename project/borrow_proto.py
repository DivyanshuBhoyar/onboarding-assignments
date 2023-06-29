from typing import Protocol


class Borrowable(Protocol):

    def borrow(self, user):
        pass


    def return_back(self):
        pass