__author__ = 'archmagece'

from abc import ABCMeta, abstractmethod


#class BSSender(metaclass=ABCMeta):
class BSSender():
    __metaclass__ = ABCMeta
    @abstractmethod
    def __init__(self, tableName, pkFieldsTuple=None):
        pass

    @abstractmethod
    def create_connection(self):
        pass

    @abstractmethod
    def re_connect(self):
        pass

    @abstractmethod
    def send_many(self):
        pass

    @abstractmethod
    def send_list(self):
        pass

    @abstractmethod
    def send_one(self):
        pass

    @abstractmethod
    def flush(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def cancel(self):
        pass

    pass  #end of class BSSender

class BSBokBoot(BSSender):

    def __init__(self, tableName, pkFieldsTuple=None):
        pass

    def create_connection(self):
        pass

    def re_connect(self):
        pass

    def send_many(self):
        pass

    def send_list(self):
        pass

    def send_one(self):
        pass

    def flush(self):
        pass

    def close(self):
        pass

    def cancel(self):
        pass

    pass  #end of class BSSender