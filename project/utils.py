from collections import defaultdict

KEYS = ["books", "newspapers", "magazines"]

class RestrictedDefaultDict(defaultdict):

    def __init__(self, default_factory=list):
        super().__init__(default_factory)

    def __setitem__(self, key, value):
        if key not in KEYS:
            raise KeyError(f"Invalid key: {key}")
        super().__setitem__(key, value)


def check_max_capacity(func):
    def wrapper(self, item):
        from library import Library
        if self.count < Library.max_capacity:
            return func(self, item)
        else:
            print("NO SLOTS FOR NEW ITEMS")
            return False
    
    return wrapper



def check_min_capacity(func):
    def wrapper(self, item):
        from library import Library
        if self.count > Library.min_capacity:
            return func(self, item)
        else:
            print("AT MIN CAPACITY")
            return False
    
    return wrapper


def gen_id():
    id = 1
    while True:
        yield str(id)
        id += 1