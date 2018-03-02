#import discord
#from discord.ext import commands
import webcord
from iksmproxy2.config import Configuration

CONF = Configuration()

class DiscordDriver():
    def __init__(self):
        self.hook = webcord.Webhook(CONF.discord['webhook_url'])


    def send_data(self, data):
        print("Post to discord...")
        print("Data: " + data)
        content = CONF.discord['command_head'] + " " + data
        self.hook.send_message(content, CONF.discord['webhook_username'])
