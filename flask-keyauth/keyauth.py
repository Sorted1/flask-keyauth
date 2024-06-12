import requests
import json
from flask import session

class KeyAuthAPI:
    def __init__(self, name, ownerid):
        self.name = name
        self.ownerid = ownerid

    def init(self):
        if not self.name or len(self.ownerid) != 10:
            return "Go to <a href=\"https://keyauth.cc/app/\" target=\"blank\">https://keyauth.cc/app/</a> and click the <b>PHP</b> button in the App credentials code. Copy that & paste in <code style=\"background-color: #eee;border-radius: 3px;font-family: courier, monospace;padding: 0 3px;\">credentials.php</code>"

        data = {
            "type": "init",
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.req(data)

        if response == "KeyAuth_Invalid":
            return "Go to <a href=\"https://keyauth.cc/app/\" target=\"blank\">https://keyauth.cc/app/</a> and click the <b>PHP</b> button in the App credentials code. Copy that & paste in <code style=\"background-color: #eee;border-radius: 3px;font-family: courier, monospace;padding: 0 3px;\">credentials.php</code>"

        json_response = json.loads(response)

        if json_response.get('message') == "This program hash does not match, make sure you're using latest version":
            return "You must disable hash check at <a href=\"https://keyauth.cc/app/?page=app-settings\" target=\"blank\">https://keyauth.cc/app/?page=app-settings</a>"

        if not json_response.get('success'):
            return json_response.get('message')
        else:
            session['sessionid'] = json_response['sessionid']

    def login(self, username, password):
        data = {
            "type": "login",
            "username": username,
            "pass": password,
            "sessionid": session.get('sessionid'),
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.req(data)
        json_response = json.loads(response)

        if not json_response.get('success'):
            session.pop('sessionid', None)
            return json_response.get('message')
        else:
            session["user_data"] = json_response['info']
            return json_response.get('success')

    def register(self, username, password, key):
        data = {
            "type": "register",
            "username": username,
            "pass": password,
            "key": key,
            "sessionid": session.get('sessionid'),
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.req(data)
        json_response = json.loads(response)

        if not json_response.get('success'):
            session.pop('sessionid', None)
            return json_response.get('message')
        else:
            session["user_data"] = json_response['info']
            return json_response.get('success')

    def license(self, key):
        data = {
            "type": "license",
            "key": key,
            "sessionid": session.get('sessionid'),
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.req(data)
        json_response = json.loads(response)

        if not json_response.get('success'):
            session.pop('sessionid', None)
            return json_response.get('message')
        else:
            session["user_data"] = json_response['info']
            return json_response.get('success')

    def upgrade(self, username, key):
        data = {
            "type": "upgrade",
            "username": username,
            "key": key,
            "sessionid": session.get('sessionid'),
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.req(data)
        json_response = json.loads(response)

        if not json_response.get('success'):
            session.pop('sessionid', None)
            return json_response.get('message')
        else:
            return json_response.get('success')

    def var(self, varid):
        data = {
            "type": "var",
            "varid": varid,
            "sessionid": session.get('sessionid'),
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.req(data)
        json_response = json.loads(response)

        if not json_response.get('success'):
            session.pop('sessionid', None)
            return json_response.get('message')
        else:
            return json_response.get('message')

    def log(self, message):
        User = gethostname()
        data = {
            "type": "log",
            "pcuser": User,
            "message": message,
            "sessionid": session.get('sessionid'),
            "name": self.name,
            "ownerid": self.ownerid
        }

        self.req(data)

    def setvar(self, varname, data):
        data = {
            "type": "setvar",
            "var": varname,
            "data": data,
            "sessionid": session.get('sessionid'),
            "name": self.name,
            "ownerid": self.ownerid
        }

        self.req(data)

    def getvar(self, varid):
        data = {
            "type": "getvar",
            "var": varid,
            "sessionid": session.get('sessionid'),
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.req(data)
        json_response = json.loads(response)

        if not json_response.get('success'):
            return None
        else:
            return json_response.get('response')

    def webhook(self, webid, param, body="", conttype=""):
        data = {
            "type": "webhook",
            "webid": webid,
            "params": param,
            "body": body,
            "conttype": conttype,
            "sessionid": session.get('sessionid'),
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.req(data)
        json_response = json.loads(response)

        if not json_response.get('success'):
            return None
        else:
            return json_response.get('response')

    def fetchOnline(self):
        data = {
            "type": "fetchOnline",
            "sessionid": session.get('sessionid'),
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.req(data)
        json_response = json.loads(response)

        if not json_response.get('success'):
            return None
        else:
            return json_response.get('response')

    def checkBlack(self):
        data = {
            "type": "checkBlack",
            "sessionid": session.get('sessionid'),
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.req(data)
        json_response = json.loads(response)

        if not json_response.get('success'):
            return None
        else:
            return json_response.get('response')
    
    def ban(self, reason):
        data = {
            "type": "ban",
            "sessionid": session.get('sessionid'),
            "name": self.name,
            "ownerid": self.ownerid,
            "reason": reason
        }

        response = self.req(data)
        json_response = json.loads(response)

        if json_response.get('success'):
            return True
        else:
            return False

    def chatGet(self, channel):
        data = {
            "type": "chatget",
            "channel": channel,
            "sessionid": session.get('sessionid'),
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.req(data)
        json_response = json.loads(response)

        if not json_response.get('success'):
            return None
        else:
            return json_response.get('messages')

    def chatSend(self, message, channel):
        data = {
            "type": "chatsend",
            "message": message,
            "channel": channel,
            "sessionid": session.get('sessionid'),
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.req(data)
        json_response = json.loads(response)

        if not json_response.get('success'):
            return None
        else:
            return json_response.get('message')

    def req(self, data):
        response = requests.post("https://keyauth.win/api/1.2/", data=data, headers={"User-Agent": "KeyAuth"})
        return response.text
