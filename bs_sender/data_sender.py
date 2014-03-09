__author__ = 'archmagece'

import psycopg2
import logging

import bs_sender.base_style
import bs_sender.query_util


class PgSender(bs_sender.base_style.BSSender):

    def __init__(self, connection_info, table_name, pk_fields_tuple=None):
        self.host = connection_info.host,
        self.port = connection_info.port,
        self.database = connection_info.database,
        self.username = connection_info.username,
        self.password = connection_info.password,
        self.table_name = table_name,
        self.pk_fields_tuple = pk_fields_tuple,
        self.autocommit = connection_info.autocommit

        self.connection = self.connect()
        #self.cursor = self.connection.cursor()
        pass

    def connect(self):
        connection = psycopg2.connect(database=self.database,
                                      user=self.username,
                                      password=self.password,
                                      host=self.host,
                                      port=self.port)
        if self.autocommit:
            self.connection.autocommit = self.autocommit
            # self.conn.set_session([isolation_level,] [readonly,] [deferrable,] [autocommit])
            # self.conn.set_isolation_level(n)
            self.connection.set_isolation_level(3)
        self.cursor = self.connection.cursor()
        if self.autocommit:
            self.cursor.execute("BEGIN")
        return connection

    def reconnect(self):
        try:
            self.cursor.execute("SELECT 1;")
        except Exception, e:
            if e.pgcode is None:
                try:
                    self.connect()
                except Exception, e:
                    return False
                pass
            pass
        return True

    def send_many(self, dict_list):
        pass

    def send_one(self, dict_value):
        insert_query = bs_sender.query_util.generate_insert_query_by_dict(self.table_name, dict_value)
        self.cursor.execute(insert_query)
        logging.debug(self.table_name + " send dict_value")
        pass

    def send_list(self, dict_list):
        for dict_value in dict_list:
            self.send_one(dict_value)
            pass
        logging.debug(self.table_name + " send send_list")
        pass

    def flush(self):
        pass

    def close(self):
        pass

    def cancel(self):
        pass
    pass