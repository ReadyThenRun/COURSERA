#!usr/bin/env python3
# LinkedIn python design pattern Course CH03
# coder: shuai

from functools import wraps

def make_blink(func):
    """Defines the decorator"""

    #This makes the decorator transparent in terms of its name and docstring
    @wraps(func)
    def decorator(*args, **kwargs):
        ret = func(*args, **kwargs)
        #Add new functionality to the function being decorated
        return f"<blink>{ret}</blink>"
    return decorator

# Apply the decorator here !
@make_blink
def say_hello(name):
    ret = f"Hello {name}!"
    print(ret)
    return ret

if __name__=='__main__':
    print(say_hello('shuai'))
    # Hello shuai!
    # <blink>Hello shuai!</blink>
    print(say_hello)    
    # <function say_hello at 0x000001807CA11950>
    print(say_hello.__name__)   
    # say_hello
    print(say_hello.__doc__)    
    # None
    print(help(say_hello))  
    # Help on function say_hello in module __main__:
    