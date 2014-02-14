__author__ = 'archmagece'


import bs_sender.base_style


class BSPgSender(bs_sender.base_style.BSSender):

    def __init__((self, tableName, pkFieldsTuple=None, p_database=config.dbName, p_user=config.dbUser,
                 p_password=config.dbPass, p_host=config.dbHost, p_port=config.dbPort, p_autocommit=True):
        self.tableName = tableName
        self.pkFieldsTuple = pkFieldsTuple

        self.settings = {
            "database": p_database,
            "user": p_user,
            "password": p_password,
            "host": p_host,
            "port": p_port,
            "autocommit": p_autocommit
        }

        self.createConnection()
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