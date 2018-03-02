from iksmproxy2.config import Configuration
from iksmproxy2.notificator.drivers.discord_driver import DiscordDriver

CONF = Configuration()


class Notificator:
    def __init__(self):
        if CONF.default['notificattion_driver'] == 'discord':
            print("setup discord driver")
            self.driver = DiscordDriver()


    def push_message(self, message):
        self.driver.send_data(message)
