from functools import wraps
import time
'''
def decorator_func(outer_funct):
    @wraps(outer_funct)
    def wrapper_func():
        return outer_funct()
    return wrapper_func

def display():
    print('Wrapper function ran')
    
dec_func= decorator_func(display)
dec_func()

def dec_it(func):
    @wraps(func)
    def inner():
        print("Before {}".format(func.__name__))
        func()
        print("After {}".format(func.__name__))
    return inner
    
@dec_it
def hello():
    print("func called")
    
#hello=dec_it(hello) manual decorator
hello() #Syntactic Sugar

def sqr_it(funct):
    @wraps(funct)
    def wrapper_func(*args,**kwargs):
        result=funct(*args,**kwargs)
        return result*result
    return wrapper_func
def double(funct):
    @wraps(funct)
    def wrapper_func(*args,**kwargs):
        result= funct(*args,**kwargs)
        return result*2
    return wrapper_func

@sqr_it
@double
def driver(a,b):
    return a+b

print(driver(3,5))

def calc(func):
    @wraps(func)
    def wrapper_func(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print("Finished in {:.3f} secs".format(end-start))
        return result
    return wrapper_func

@calc
def prnt(n):
    new=[]
    for i in range(n):
        new.append(i)
    return new

prnt(10)

#properties in python

class Person():
    def __init__(self,value):
        self.name = value
    def get_name(self):
        print('Getting Name...')
        return self.name
    def set_name(self,value):
        print('Setting Name to...',value)
        self.name=value
    def del_name(self):
        print('deleting Name...')
        del self.name
    result=property(get_name,set_name,del_name)
    
P=Person('Shivam Kumar')

P.result='Shubham kumar'
'''
#property as decorator
class Person():
    def __init__(self, value):
        self.namee = value
    
    @property
    def func(self):
        print('Getting name:')
        return self.namee

    @func.setter
    def func(self, value):
        print('Setting name to', value)
        self.namee = value
        
    @func.deleter
    def func(self):
        print('Deleting name')
        del self.namee

P=Person('Shivam Kumar')
P.func='Shubham kumar'








 