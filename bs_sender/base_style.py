__author__ = 'archmagece'

from abc import ABCMeta, abstractmethod
import time

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


def retry(retry_cnt=10, delay_sec=5, exception=Exception, runtime_exception=RuntimeError, log=None):
    def decorator(fn):
        def retrier(*args, **kwargs):
            m_retry_cnt = retry_cnt
            m_delay_sec = delay_sec
            try_cnt = 0
            while try_cnt < m_retry_cnt:
                try:
                    return fn(*args, **kwargs)
                except exception as e:
                    msg = "retry error %s, retry in %d seconds" % (str(e), m_delay_sec)
                    if log:
                        log.exception(msg)
                    else:
                        print msg
                    time.sleep(delay_sec)
                    try_cnt += 1
            raise runtime_exception("runtime error")
        return retrier
    return decorator


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
    @retry
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
