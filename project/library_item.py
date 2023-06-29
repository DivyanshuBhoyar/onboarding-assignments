from abc import ABC, abstractmethod, abstractproperty


class LibraryItem(ABC):

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def category(self):
        pass

    @abstractmethod
    def set_library_hook(self, lib):
        pass