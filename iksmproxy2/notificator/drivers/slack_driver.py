import requests
import json
from iksmproxy2.config import Configuration

CONF = Configuration()

class SlackDriver():
    def __init__(self):
        self.s = requests.session()


    def send_data(self, data):
        print("Post to Slack...")
        print("Data: " + data)

        content = CONF.slack['command_head'] + " " + data
        payload = {"text": content}
        r = self.s.post(CONF.slack['webhook_url'], data=json.dumps(payload))
        print(r.text.encode("utf-8"))
