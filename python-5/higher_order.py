'''
The properties of higher-order functions include:

Storing a function inside a variable.
Having a function act as an instance of an object type.
Returning a function as a result of another function.
Passing a function as a parameter or argument inside another function.
Storing Python higher-order functions in data structures such as lists, hash tables, etc
'''

def greet(language):
    def english(name):
        return f'Hello, {name}'

    def french(name):
        return f'Bonjour, {name}'

    if language == 'eng':
        return english
    else:
        return french
