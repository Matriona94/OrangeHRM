import configparser


class ReadLoginConfig:
    def __init__(self):
        self.path = ".//tests/conf/configuration.ini"
        self.config = configparser.RawConfigParser()
        self.config.read(self.path)

    def get_login_info(self, key):
        return self.config.get('login info', key)
