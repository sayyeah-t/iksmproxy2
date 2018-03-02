from iksmproxy2.config import Configuration
from iksmproxy2.notificator.driver import Notificator
import subprocess


CONF = Configuration()


class ProxyWorker():

    def __init__(self):
        self.loop = True
        self.iksm_session = ""
        self.notificator = Notificator()

    def run(self):
        cmd = "mitmdump -s print_cookie.py"
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while(self.loop):
            try:
                line = proc.stdout.readline().decode('utf-8')
                if line.find("iksm_session") == 0:
                    self.extract_iksm_session(line)
                    #print(self.iksm_session)
                    if self.iksm_changed:
                        self.notificate()
            except KeyboardInterrupt:
                break
        proc.terminate()


    def stop(self):
        self.loop = False


    def extract_iksm_session(self, msg):
        self.iksm_changed = False
        datalist = msg.split("; ")
        for data in datalist:
            if "iksm_session" in data:
                iksm_session_new = data.split("=")[1]
        if self.iksm_session != iksm_session_new:
            self.iksm_session = iksm_session_new
            self.iksm_changed = True


    def notificate(self):
        self.notificator.push_message(self.iksm_session)
