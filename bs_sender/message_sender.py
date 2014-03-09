__author__ = 'archmagece'


import bs_sender.base_style
import bs_sender.query_util
from bs_sender.base_style import retry


class BSBokBoot(bs_sender.base_style.BSSender):

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

    @retry
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
