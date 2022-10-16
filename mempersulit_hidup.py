import socket

class __abcd__(object):
    def __init__(self):
        self.list = open('text.txt','r').read().splitlines()

class __efgh__():
    def __init__(
            self,
            host : str ,
            ):
        self.host = host

class __complations__(__abcd__,__efgh__):
    def __init__(self):
        super().__init__()
        super(__abcd__,
              self
              ).__init__(host=self.list)

class converter():
    def __init__(
            self,
            target : str = [],
        ):
        self.target = target
        self.sock = socket.gethostbyname(f"{self.target}")

    def __repr__(self):
        return self.sock

ap = __complations__()
for c in ap.list:
    print(converter(target='%s'%(c)))

