__author__ = 'archmagece'


class ConnectionInfo():

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        pass
    pass


class Sender():

    def __init__(self, connection_info):
        pass

    def reconnect(self):
        pass

    def send_one(self, json):
        pass

    def send_list(self, json_list):
        for json in json_list:
            self.send_one(json)
            pass
        pass

    def send_many(self):
        pass

    def flush(self):
        pass

    def close(self):
        pass
    pass