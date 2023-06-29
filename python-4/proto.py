from typing import Protocol, runtime_checkable

@runtime_checkable
class Animal(Protocol):

    def speak(self) -> str:
        pass

class Dog:

    def speak(self) -> str:
        return "Woof!"

d = Dog()
print(isinstance(d, Animal)) 


'''
for static type checking
'''

class Webserver(Protocol):

    def respond(self) -> str:
        pass

    def log(self) -> str:
        pass


class FastapiServer:

    def log(self) -> str:
        print("logging...")



server1 = FastapiServer()

# no error
#  mypy will complain here as well 
# bcoz repond() method is missing
def pingServer(server: Webserver):
    server.log()
pingServer(server1)


class GoHttpServer:
    def log(self) -> str:
        print('logging in go/net/http')

    def respond(self) -> str:
        return "hello world"

server2 = GoHttpServer()

pingServer(server2)
# no error, no mypy error as well