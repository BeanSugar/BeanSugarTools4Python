__author__ = 'archmagece'

import bs_data_sender

import psycopg2


class PgSender(bs_data_sender.Sender):

    def __init__(self, table_name, db_name, username,
                 password, db_host, db_port, pk_field_tuple=None, autocommit=True):
        self.table_name = table_name
        self.pk_field_tuple = pk_field_tuple

        self.settings = {
            "database": db_name,
            "user": username,
            "password": password,
            "host": db_host,
            "port": db_port,
            "autocommit": autocommit
        }
        #self.connection = self.connect()
        #self.cursor = self.connection.cursor()
        pass

    def create_connection(self):
        self.connection = psycopg2.connect(database=self.settings["database"],
                                user=self.settings["user"],
                                password=self.settings["password"],
                                host=self.settings["host"],
                                port=self.settings["port"])
        if self.settings["autocommit"]:
            self.connection.autocommit = False
            # self.conn.set_session([isolation_level,] [readonly,] [deferrable,] [autocommit])
            # self.conn.set_isolation_level(n)
            self.connection.set_isolation_level(3)
        self.cursor = self.connection.cursor()
        if self.settings["autocommit"]:
            self.cur.execute("BEGIN")
        pass

    def reconnect(self):
        try:
            self.cursor.execute("SELECT 1;")
        except Exception, e:
            if e.pgcode is None:
                try:
                    self.create_connection()
                except Exception, e:
                    return False
            pass
        return True

    def send_one(self):
        sqlQueryInsert = generateQueryUsingDict(self.tableName, dictValue)
        # print sqlQueryInsert
        self.cur.execute(sqlQueryInsert)
        log.debug(self.tableName + " sendResultDict")
        pass

    def send_list(self):
        pass

    def send_many(self):
        pass

    def flust(self):
        pass

    def close(self):
        pass
    pass