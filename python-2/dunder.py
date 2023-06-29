class CustomList:
    def __init__(self, items=None):
        self.items = items if items else []

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        print("custom set item")
        self.items[index] = value

    def __delitem__(self, index):
        print("deleting at index", index)
        del self.items[index]

    def __contains__(self, value):
        print("checking existence")
        return value in self.items

    def __len__(self):
        return len(self.items)

    def __call__(self, index, value):
        print(f"inserting value {value} at index {index}")
        self.items.insert(index, value)

    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")


CustomList([1,2,43,5,])(1,7)
print("")
with CustomList() as mylist:
    mylist(0, 10)
    mylist(1, 78)
    mylist(3, 4)

    print("len", len(mylist))
    print("has 4 ?", 4 in mylist)