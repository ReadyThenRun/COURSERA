#!usr/bin/env python3
# -*- coding utf-8 -*-
# reference: "https://realpython.com/primer-on-python-decorators/"
# coder: shuai

# A function returns a value based on the given arguments.
def add_one(number):
    return number+1

# In Python, functions are first-class objects;
# functions can be passed around and used as arguments;

def sayHello(name):
    return f"Hello, {name}"
def beAwesome(name):
    return f"Hi {name}, together we are the awesomest!"
def greetToBob(greetFunc):
    return greetFunc("bob")
'''
execute:
print(greetToBob(sayHello))
print(greetToBob(beAwesome))
----------------------------
Output:
Hello, bob
Hi bob, together we are the awesomest!
'''
def greetTo(greetFunc,name):
    return greetFunc(name)
'''
execute:
print(greetTo(sayHello, 'James'))
print(greetTo(beAwesome,'James'))
----------------------------
Output:
Hello, James
Hi James, together we are the awesomest!
'''
    
# Inner Functions are defined inside other functions.
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()  # only exist as local variables.
    first_child()   # only exist as local variables.
'''
execute:
parent()
---------------------
output:
Printing from the parent() function
Printing from the second_child() function
Printing from the first_child() function
'''
# Returning Functions From Functions

def parent(num):
    def first_child():
        return "Hi, I am Emma"
    def second_child():
        return "Call me Liam"
    if num == 1:
        return first_child  # returning a reference
    else:
        return second_child # returning a reference
'''
execute:
fc = parent(1)
sc = parent(2)
print(fc())
print(sc())
-------------------
output:
Hi, I am Emma
Call me Liam
'''
'''
execute:
print( parent(1)() )
print( parent(2)() )
-------------------
output:
Hi, I am Emma
Call me Liam
'''

### Simple Decorators

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

'''
execute:
say_whee()
----------------------
output:
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
'''
# decorators wrap a function, modifying its behavior.
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)

'''

'''

### Syntactic Sugar!
# use decorators in a simpler way with the @ symbol;

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

'''
@my_decorator
===
say_whee = my_decorator(say_whee)
'''

### Reusing Decorators
# Recall that a decorator is just a regular Python function.
'''
'''

### Decorating Functions With Arguments




### Returning Values From Decorated Functions


### introspection:
# is the ability of an object to know about its own attributes at runtime.
'''
>>> print
<built-in function print>
>>> print.__name__
'print'
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
'''
### using  @functools.wraps decorator which
# will preserve information about the original function;
'''
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
'''

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
'''
execute:
waste_some_time(1000)
----------------------
output:
Finished 'waste_some_time' in 2.9685 secs
'''
''' check introspection
>>> waste_some_time
<function waste_some_time at 0x000001423944F048>
>>> waste_some_time.__name__
'waste_some_time'
>>> help(waste_some_time)
Help on function waste_some_time in module __main__:

waste_some_time(num_times)
'''
# real example: Registering Plugins
import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
'''
execute:
print(randomly_greet('Bob'))
-----------------------
Using 'say_hello'
Hello Bob
-----
Using 'be_awesome'
Yo Bob, together we are the awesomest!
'''

if __name__ == '__main__':


    

