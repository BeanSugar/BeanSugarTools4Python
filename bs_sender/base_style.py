__author__ = 'archmagece'

from abc import ABCMeta, abstractmethod


class ConnectionInfo():
    def __init__(self, host, port, database, username, password, autocommit=True):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.autocommit = autocommit
        pass
    pass


#class BSSender(metaclass=ABCMeta):
class BSSender():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, connection_info, table_name, pk_fields_tuple=None):
        self.host = connection_info.host
        self.port = connection_info.port
        self.database = connection_info.database
        self.username = connection_info.username
        self.password = connection_info.password
        self.autocommit = connection_info.autocommit

        self.table_name = table_name
        self.pk_fields_tuple = pk_fields_tuple
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def reconnect(self):
        pass

    @abstractmethod
    def send_many(self, json_list):
        pass

    @abstractmethod
    def send_one(self, json):
        pass

    @abstractmethod
    def send_list(self, json_list):
        for json in json_list:
            self.send_one(json)
            pass
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
    pass  # end of class BSSender


class BSBokBoot(BSSender):

    def __init__(self, connection_info, table_name, pk_fields_tuple=None):
        self.host = connection_info.host
        self.port = connection_info.port
        self.database = connection_info.database
        self.username = connection_info.username
        self.password = connection_info.password
        self.autocommit = connection_info.autocommit

        self.table_name = table_name
        self.pk_fields_tuple = pk_fields_tuple
        pass

    def connect(self):
        pass

    def reconnect(self):
        pass

    def send_many(self, json_list):
        pass

    def send_one(self, json):
        pass

    def send_list(self, json_list):
        for json in json_list:
            self.send_one(json)
            pass
        pass

    def flush(self):
        pass

    def close(self):
        pass

    def cancel(self):
        pass
    pass  # end of class BSSender