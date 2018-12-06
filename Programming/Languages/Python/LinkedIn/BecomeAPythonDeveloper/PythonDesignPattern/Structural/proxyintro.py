#!usr/bin/env python3
# ref:
# coder: shuai
# Python design pattern： proxy

from abc import abstractmethod
'''
Adapter provides a different interface to its subject;
Proxy provides the same interface;
Decorator provides an enhanced interface.
'''
class UserService:
    @abstractmethod
    def get_info(self, uid):
        pass


class UserServiceImpl(UserService):
    def get_info(self, uid):
        if uid == 1:
            return "Jim"
        elif uid == 2:
            return "Geroge"
        elif uid == 3:
            return "Flash"
        else:
            return None

class UserServiceProxy(UserService):
    def __init__(self):
        self.userService = UserServiceImpl()
        # Proxy pattern, execute important process before access objects
        print("<add import proccessing here>\nRemote Service B is Connected..")

    def get_info(self, uid):
        return self.userService.get_info(uid)

if __name__=='__main__':
    proxy = UserServiceProxy()
    print(proxy.get_info(2))
    print(proxy.get_info(5))
