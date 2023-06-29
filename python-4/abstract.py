from abc import ABC, abstractmethod

class AbstractExample(ABC):

    @abstractmethod
    def do_calc(self, a, b):
        pass



class DoAdd(AbstractExample):

    def do_calc(self, a, b):
        return a + b



class DoMultiply(AbstractExample):
    pass

    # def do_calc(self, a, b):
    #     return a * b


mul = DoMultiply().do_calc(40, 3)
print(mul)


'''
A real subclass knows its relationship with
the parent through its __bases__ attribute, 
and can thus implicitly delegate the
resolution of missing methods. A virtual subclass knows nothing abouth]
the class that registerd it, and nowhere in the sublcass there is something 
that links it to parent class.
'''
#Classes that can register other classes, thus becoming virtual parents of those, are called in Python Abstract Base Classes, or ABCs.
# Registering is just a promise



#ABCs can be instantiated, so they are after all not pure interfaces
class MyABC(metaclass=abc.ABCMeta):
  pass
 
m = MyABC()
# if only we use @abc.abstractmethod decorator,
# only then it is prevented from instantiation if method not implemented


# use of new
class MyClass():
    def __new__(cls, *args, **kwds):
        obj = super().__new__(cls, *args, **kwds)
        # [custom code here]
        return obj