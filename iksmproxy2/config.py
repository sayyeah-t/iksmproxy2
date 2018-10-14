import configparser

class Configuration:
    path = "iksmproxy2.conf"
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(self.path)

        self.default = config['DEFAULT']
        self.discord = config['DISCORD']
        self.slack = config['SLACK']
