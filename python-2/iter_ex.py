#iterables can be iterated over by for loop or for...in loop
mylist = ["New Zealand", "England", "Netherlands"]
for team in mylist:
    print(team)


#Iterator is any object with __iter__ and __next__ methods
# __iter__ returns iterator object itself
teams = iter(mylist) #now is an iterator
print(next(teams))
print(next(teams))
print(next(teams))

# iterables return iterator when __iter__ is called